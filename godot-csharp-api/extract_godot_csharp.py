#!/usr/bin/env python3
"""
Godot C# API Reference Extractor
Parses Godot HTML docs and produces condensed C#-specific Markdown skill files.
"""

import os
import re
import sys
import json
from pathlib import Path
from bs4 import BeautifulSoup, Tag

# ─── snake_case → PascalCase conversion ─────────────────────────────────────
def snake_to_pascal(name: str) -> str:
    """Convert snake_case identifier to PascalCase."""
    if not name or name.startswith('_'):
        # private/virtual methods: _ready → _Ready
        if name.startswith('_'):
            rest = name[1:]
            return '_' + snake_to_pascal(rest) if rest else name
        return name
    return ''.join(word.capitalize() for word in name.split('_'))


def convert_signature_to_csharp(sig: str, ret_type: str) -> tuple[str, str]:
    """
    Convert a GDScript-style method signature to C# style.
    e.g. 'get_child(idx: int) const' → 'GetChild(int idx)'
         'add_child(node: Node, force_readable_name: bool = false)'
    Returns (csharp_return_type, csharp_signature)
    """
    # Split method name from params
    m = re.match(r'^([\w_]+)\s*\((.*)\)\s*(.*)', sig)
    if not m:
        return map_type(ret_type), sig

    method_name = m.group(1)
    params_raw = m.group(2).strip()
    modifiers = m.group(3).strip()  # const, vararg, static, etc.

    csharp_method = snake_to_pascal(method_name)
    csharp_ret = map_type(ret_type)

    # Parse parameters
    csharp_params = []
    if params_raw and params_raw != '...':
        # Split by comma but respect nested brackets
        depth = 0
        current = []
        parts = []
        for ch in params_raw:
            if ch in '([{':
                depth += 1
                current.append(ch)
            elif ch in ')]}' :
                depth -= 1
                current.append(ch)
            elif ch == ',' and depth == 0:
                parts.append(''.join(current).strip())
                current = []
            else:
                current.append(ch)
        if current:
            parts.append(''.join(current).strip())

        for part in parts:
            part = part.strip()
            if not part or part == '...':
                continue
            # param format: "name: Type = default" or "name: Type"
            default = ''
            if '=' in part:
                param_part, default_part = part.split('=', 1)
                default = default_part.strip()
            else:
                param_part = part
            if ':' in param_part:
                pname, ptype = param_part.split(':', 1)
                pname = pname.strip()
                ptype = map_type(ptype.strip())
            else:
                pname = param_part.strip()
                ptype = 'Variant'
            cs_pname = snake_to_pascal(pname) if pname else pname
            # keep param names camelCase not PascalCase conventionally,
            # but Godot docs use them as-is - just convert for readability
            # Actually C# convention is camelCase for params
            cs_pname_camel = pname  # keep original snake or convert to camelCase
            if '_' in pname:
                words = pname.split('_')
                cs_pname_camel = words[0] + ''.join(w.capitalize() for w in words[1:])
            if default:
                # normalize default values
                default = default.replace('false', 'false').replace('true', 'true').replace('null', 'null')
                csharp_params.append(f'{ptype} {cs_pname_camel} = {default}')
            else:
                csharp_params.append(f'{ptype} {cs_pname_camel}')

    suffix = ''
    if 'static' in modifiers:
        suffix = ' [static]'
    elif 'virtual' in modifiers:
        suffix = ' [virtual]'
    elif 'const' in modifiers:
        suffix = ''

    params_str = ', '.join(csharp_params)
    csharp_sig = f'{csharp_method}({params_str}){suffix}'
    return csharp_ret, csharp_sig


def convert_property_name(name: str) -> str:
    """Convert snake_case property name to PascalCase for C#."""
    return snake_to_pascal(name)


# ─── Type mapping: Godot/GDScript names → C# equivalents ──────────────────────
TYPE_MAP = {
    "String":     "string",
    "bool":       "bool",
    "int":        "int",
    "float":      "float",
    "void":       "void",
    "Array":      "Godot.Collections.Array",
    "Dictionary": "Godot.Collections.Dictionary",
    "Callable":   "Callable",
    "Signal":     "Signal",
}

# ─── Domain bucketing ─────────────────────────────────────────────────────────
# Maps output skill filename → list of class name prefixes/exact names.
# Classes not matched by any rule go to "misc".
DOMAIN_RULES = [
    ("core", [
        "Object", "Node", "SceneTree", "Resource", "RefCounted", "MainLoop",
        "WeakRef", "ClassDB", "Engine", "OS", "Marshalls", "MessageQueue",
        "Performance", "WorkerThreadPool", "Semaphore", "Mutex", "Thread",
        "EngineDebugger", "ResourceLoader", "ResourceSaver", "ResourceUID",
    ]),
    ("nodes_2d", [
        "Node2D", "Sprite2D", "AnimatedSprite2D", "Camera2D", "CanvasItem",
        "CanvasLayer", "CanvasModulate", "CollisionObject2D", "CollisionPolygon2D",
        "CollisionShape2D", "CPUParticles2D", "GPUParticles2D", "Light2D",
        "LightOccluder2D", "Line2D", "Marker2D", "MeshInstance2D",
        "MultiMeshInstance2D", "NavigationAgent2D", "NavigationLink2D",
        "NavigationObstacle2D", "NavigationRegion2D", "Path2D", "PathFollow2D",
        "Polygon2D", "RayCast2D", "RemoteTransform2D", "Skeleton2D",
        "StaticBody2D", "TileMap", "TileMapLayer", "TouchScreenButton",
        "VisibleOnScreenEnabler2D", "VisibleOnScreenNotifier2D",
        "AnimatableBody2D", "CharacterBody2D", "RigidBody2D",
        "Joint2D", "DampedSpringJoint2D", "GrooveJoint2D", "PinJoint2D",
    ]),
    ("nodes_3d", [
        "Node3D", "Camera3D", "MeshInstance3D", "DirectionalLight3D",
        "OmniLight3D", "SpotLight3D", "Light3D", "ReflectionProbe",
        "GpuParticles3D", "CpuParticles3D", "Decal", "FogVolume",
        "WorldEnvironment", "LightmapGI", "LightmapProbe", "VoxelGI",
        "Skeleton3D", "BoneAttachment3D", "Marker3D", "Path3D",
        "PathFollow3D", "RemoteTransform3D", "VisualInstance3D",
        "GeometryInstance3D", "MultiMeshInstance3D", "AnimatableBody3D",
        "CharacterBody3D", "RigidBody3D", "StaticBody3D", "VehicleBody3D",
        "VehicleWheel3D", "SoftBody3D", "NavigationAgent3D",
        "NavigationLink3D", "NavigationObstacle3D", "NavigationRegion3D",
        "RayCast3D", "ShapeCast3D", "SpringArm3D", "XR",
    ]),
    ("physics", [
        "PhysicsServer2D", "PhysicsServer3D", "PhysicsBody2D", "PhysicsBody3D",
        "PhysicsDirectBodyState2D", "PhysicsDirectBodyState3D",
        "PhysicsDirectSpaceState2D", "PhysicsDirectSpaceState3D",
        "PhysicsMaterial", "PhysicsPointQueryParameters2D",
        "PhysicsPointQueryParameters3D", "PhysicsRayQueryParameters2D",
        "PhysicsRayQueryParameters3D", "PhysicsShapeQueryParameters2D",
        "PhysicsShapeQueryParameters3D", "PhysicsTestMotionParameters2D",
        "PhysicsTestMotionParameters3D", "PhysicsTestMotionResult2D",
        "PhysicsTestMotionResult3D",
        "Shape2D", "Shape3D", "CollisionShape2D", "CollisionShape3D",
        "CollisionPolygon2D", "CollisionPolygon3D",
        "Joint3D", "Generic6DOFJoint3D", "HingeJoint3D", "PinJoint3D",
        "SliderJoint3D", "ConeTwistJoint3D",
        "Area2D", "Area3D",
    ]),
    ("ui_controls", [
        "Control", "Button", "Label", "LineEdit", "TextEdit", "RichTextLabel",
        "Panel", "PanelContainer", "Container", "BoxContainer", "HBoxContainer",
        "VBoxContainer", "GridContainer", "MarginContainer", "ScrollContainer",
        "TabContainer", "SplitContainer", "HSplitContainer", "VSplitContainer",
        "CenterContainer", "AspectRatioContainer", "FlowContainer",
        "SubViewportContainer", "TextureRect", "ColorRect", "Tree",
        "ItemList", "OptionButton", "MenuButton", "CheckBox", "CheckButton",
        "LinkButton", "TextureButton", "BaseButton", "Range", "Slider",
        "HSlider", "VSlider", "ScrollBar", "HScrollBar", "VScrollBar",
        "ProgressBar", "SpinBox", "ColorPicker", "ColorPickerButton",
        "FileDialog", "AcceptDialog", "ConfirmationDialog", "Popup",
        "PopupMenu", "PopupPanel", "Window", "Tooltip",
        "GraphEdit", "GraphNode", "GraphFrame", "TabBar",
        "CodeEdit", "VideoStreamPlayer",
    ]),
    ("rendering", [
        "RenderingServer", "RenderingDevice", "Viewport", "SubViewport",
        "Environment", "CameraAttributes", "Sky", "Fog", "Material",
        "ShaderMaterial", "BaseMaterial3D", "StandardMaterial3D",
        "ORMMaterial3D", "CanvasItemMaterial", "ParticleProcessMaterial",
        "Shader", "VisualShader", "VisualShaderNode",
        "Mesh", "ArrayMesh", "ImmediateMesh", "PrimitiveMesh",
        "BoxMesh", "CapsuleMesh", "CylinderMesh", "PlaneMesh",
        "QuadMesh", "SphereMesh", "RibbonTrailMesh", "TubeTrailMesh",
        "MultiMesh", "SurfaceTool", "MeshDataTool",
        "CompositorEffect", "Compositor", "RDShaderFile",
    ]),
    ("audio", [
        "AudioStreamPlayer", "AudioStreamPlayer2D", "AudioStreamPlayer3D",
        "AudioServer", "AudioBusLayout", "AudioEffect", "AudioStream",
        "AudioStreamGenerator", "AudioStreamGeneratorPlayback",
        "AudioStreamMicrophone", "AudioStreamPlayback", "AudioStreamWav",
        "AudioStreamOggVorbis", "AudioStreamMP3",
        "AudioEffectAmplify", "AudioEffectBandLimitFilter",
        "AudioEffectBandPassFilter", "AudioEffectCapture",
        "AudioEffectChorus", "AudioEffectCompressor", "AudioEffectDelay",
        "AudioEffectDistortion", "AudioEffectEQ", "AudioEffectFilter",
        "AudioEffectHighPassFilter", "AudioEffectHighShelfFilter",
        "AudioEffectLimiter", "AudioEffectLowPassFilter",
        "AudioEffectLowShelfFilter", "AudioEffectNotchFilter",
        "AudioEffectPanner", "AudioEffectPhaser", "AudioEffectPitchShift",
        "AudioEffectRecord", "AudioEffectReverb", "AudioEffectSpectrumAnalyzer",
        "AudioEffectStereoEnhance",
    ]),
    ("input", [
        "Input", "InputEvent", "InputEventKey", "InputEventMouse",
        "InputEventMouseButton", "InputEventMouseMotion", "InputEventJoypad",
        "InputEventJoypadButton", "InputEventJoypadMotion", "InputEventAction",
        "InputEventGesture", "InputEventMagnifyGesture", "InputEventPanGesture",
        "InputEventMIDI", "InputEventScreenDrag", "InputEventScreenTouch",
        "InputEventWithModifiers", "InputMap", "ShortCut",
    ]),
    ("math_types", [
        "Vector2", "Vector2i", "Vector3", "Vector3i", "Vector4", "Vector4i",
        "Transform2D", "Transform3D", "Basis", "Quaternion",
        "AABB", "Rect2", "Rect2i", "Plane", "Color",
        "Projection", "RID",
    ]),
    ("resources", [
        "Texture", "Texture2D", "Texture3D", "TextureLayered", "CompressedTexture2D",
        "ImageTexture", "PortableCompressedTexture2D", "AtlasTexture",
        "AnimatedTexture", "CameraTexture", "GradientTexture1D",
        "GradientTexture2D", "NoiseTexture2D", "PlaceholderTexture2D",
        "ViewportTexture", "Image", "Gradient", "Curve", "Curve2D", "Curve3D",
        "Font", "FontFile", "FontVariation", "SystemFont", "BitMap",
        "TileSet", "TileSetAtlasSource", "TileSetScenesCollectionSource",
        "TileSetSource", "TileData", "StyleBox", "StyleBoxEmpty",
        "StyleBoxFlat", "StyleBoxLine", "StyleBoxTexture",
        "Theme", "PackedScene", "SceneState", "Script",
        "GDScript", "CSharpScript", "ScriptExtension",
        "Animation", "AnimationLibrary",
        "Noise", "FastNoiseLite",
        "OccluderInstance3D", "Occluder3D",
    ]),
    ("networking", [
        "HTTPClient", "HTTPRequest", "WebSocketPeer", "WebSocketMultiplayerPeer",
        "ENetMultiplayerPeer", "ENetConnection", "ENetPacketPeer",
        "MultiplayerAPI", "MultiplayerPeer", "SceneMultiplayer",
        "StreamPeer", "StreamPeerBuffer", "StreamPeerExtension",
        "StreamPeerGZIP", "StreamPeerTCP", "StreamPeerTLS",
        "TCPServer", "PacketPeer", "PacketPeerDTLS", "PacketPeerExtension",
        "PacketPeerStream", "PacketPeerUDP", "DTLSServer",
        "UDPServer", "IP", "TLSOptions", "X509Certificate",
        "CryptoKey", "Crypto", "HMAC", "AESContext", "HashingContext",
    ]),
    ("animation", [
        "AnimationPlayer", "AnimationTree", "AnimationMixer",
        "AnimationNode", "AnimationRootNode", "AnimationNodeAdd2",
        "AnimationNodeAdd3", "AnimationNodeAnimation", "AnimationNodeBlend2",
        "AnimationNodeBlend3", "AnimationNodeBlendSpace1D",
        "AnimationNodeBlendSpace2D", "AnimationNodeBlendTree",
        "AnimationNodeExtension", "AnimationNodeOneShot", "AnimationNodeOutput",
        "AnimationNodeStateMachine", "AnimationNodeStateMachinePlayback",
        "AnimationNodeStateMachineTransition", "AnimationNodeSub2",
        "AnimationNodeSync", "AnimationNodeTimeScale", "AnimationNodeTimeSeek",
        "AnimationNodeTransition",
        "Tween", "Tweener", "MethodTweener", "PropertyTweener",
        "CallbackTweener", "IntervalTweener",
        "SkeletonModificationStack2D", "SkeletonModification2D",
        "SkeletonIK3D", "SkeletonModifier3D",
        "AimModifier3D", "LookAtModifier3D",
    ]),
    ("filesystem", [
        "FileAccess", "DirAccess", "ProjectSettings", "EditorSettings",
        "ConfigFile", "JSON", "XMLParser", "ZIPReader", "ZIPPacker",
        "PCKPacker", "ResourceImporter",
    ]),
    ("editor", [
        "Editor",  # prefix match — catches all Editor* classes
    ]),
]

# ─── Helpers ──────────────────────────────────────────────────────────────────

def map_type(t: str) -> str:
    return TYPE_MAP.get(t, t)


def get_text_clean(tag) -> str:
    if tag is None:
        return ""
    return re.sub(r'\s+', ' ', tag.get_text()).strip()


def extract_csharp_code_blocks(soup: BeautifulSoup) -> list[str]:
    """Return list of C# code block texts from sphinx tabs."""
    blocks = []
    # C# tab panels have name="QyM=" (base64 of "C#")
    for panel in soup.find_all("div", attrs={"name": "QyM="}):
        code = panel.find("pre")
        if code:
            blocks.append(code.get_text())
    # Also grab standalone highlight-csharp blocks (no tab)
    for block in soup.find_all("div", class_="highlight-csharp"):
        # skip if inside a tab panel (already captured above)
        if not block.find_parent("div", attrs={"name": "QyM="}):
            pre = block.find("pre")
            if pre:
                blocks.append(pre.get_text())
    return blocks


def domain_for_class(class_name: str) -> str:
    for domain, names in DOMAIN_RULES:
        for n in names:
            if domain == "editor" and class_name.startswith("Editor"):
                return "editor"
            if class_name == n:
                return domain
            # prefix match for families (e.g. "AnimationNode" matches "AnimationNodeAdd2")
            if class_name.startswith(n) and len(n) >= 6:
                return domain
    return "misc"


def parse_class_page(html_path: Path) -> dict | None:
    """Parse a single class HTML file, return structured dict."""
    with open(html_path, encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    # ── Class name ──
    # The main article title
    title_tag = soup.find("h1")
    if not title_tag:
        return None
    class_name = get_text_clean(title_tag)
    # Strip trailing "¶" permalink char
    class_name = class_name.replace("¶", "").strip()

    # ── Inheritance ──
    inherits = ""
    inherited_by = []
    for p in soup.select("p.class-info, p"):
        txt = get_text_clean(p)
        if txt.startswith("Inherits:"):
            inherits = txt.replace("Inherits:", "").strip()
        elif txt.startswith("Inherited By:"):
            inherited_by = [s.strip() for s in txt.replace("Inherited By:", "").split(",")]

    # ── Brief description ──
    brief = ""
    brief_section = soup.find("section", id="description") or soup.find("div", class_="brief-description")
    if brief_section:
        first_p = brief_section.find("p")
        if first_p:
            brief = get_text_clean(first_p)
    # Fallback: first <p> after the title in the article body
    if not brief:
        article = soup.find("article") or soup.find("div", class_="rst-content")
        if article:
            paras = article.find_all("p")
            for p in paras:
                txt = get_text_clean(p)
                if txt and not txt.startswith("Inherits") and not txt.startswith("Inherited"):
                    brief = txt
                    break

    # ── Properties ──
    properties = []
    prop_table = soup.find("table", class_=re.compile(r"properties"))
    if not prop_table:
        # Try finding the Properties section
        prop_section = soup.find("section", id="properties")
        if prop_section:
            prop_table = prop_section.find("table")
    if prop_table:
        for row in prop_table.find_all("tr"):
            cells = row.find_all(["td", "th"])
            if len(cells) >= 2:
                prop_type = map_type(get_text_clean(cells[0]).replace("¶", "").strip())
                prop_name_raw = get_text_clean(cells[1]).replace("¶", "").strip()
                prop_name = convert_property_name(prop_name_raw)
                default = get_text_clean(cells[2]).replace("¶", "").strip() if len(cells) > 2 else ""
                if prop_type and prop_name and prop_name not in ("Name", "Default"):
                    properties.append({
                        "type": prop_type,
                        "name": prop_name,
                        "default": default,
                    })

    # ── Methods ──
    methods = []
    method_section = soup.find("section", id="methods")
    if not method_section:
        method_section = soup.find("section", id="method-descriptions")
    # Try the method table first (signatures table in header)
    method_table = None
    if method_section:
        method_table = method_section.find("table")
    if method_table:
        for row in method_table.find_all("tr"):
            cells = row.find_all(["td", "th"])
            if len(cells) >= 2:
                ret_type_raw = get_text_clean(cells[0]).replace("¶", "").strip()
                sig_raw = get_text_clean(cells[1]).replace("¶", "").strip()
                if ret_type_raw and sig_raw:
                    csharp_ret, csharp_sig = convert_signature_to_csharp(sig_raw, ret_type_raw)
                    methods.append({"return_type": csharp_ret, "signature": csharp_sig, "description": ""})

    # Add one-line descriptions from method-descriptions section
    desc_section = soup.find("section", id="method-descriptions")
    if desc_section:
        for item in desc_section.find_all(["dt", "section"]):
            # Each method detail block
            method_id = item.get("id", "")
            if not method_id:
                continue
            # Find matching method in list and add description
            first_p = item.find_next("p")
            desc = get_text_clean(first_p) if first_p else ""
            # Match by method name fragment
            for m in methods:
                sig_name = m["signature"].split("(")[0].strip()
                if sig_name and sig_name.lower() in method_id.lower():
                    if not m["description"]:
                        m["description"] = desc[:200]
                    break

    # ── Signals ──
    signals = []
    signal_section = soup.find("section", id="signals")
    if signal_section:
        for item in signal_section.find_all("dt"):
            sig = get_text_clean(item).replace("¶", "").strip()
            if sig:
                signals.append(sig)

    # ── Enums ──
    enums = []
    enum_section = soup.find("section", id="enumerations")
    if enum_section:
        current_enum = None
        for tag in enum_section.find_all(["dt", "dd"]):
            if tag.name == "dt":
                txt = get_text_clean(tag).replace("¶", "").strip()
                if "enum " in txt.lower() or txt.startswith("enum"):
                    current_enum = {"name": txt, "values": []}
                    enums.append(current_enum)
                elif current_enum is not None:
                    current_enum["values"].append(txt)

    # ── Constants ──
    constants = []
    const_section = soup.find("section", id="constants")
    if const_section:
        for item in const_section.find_all("dt"):
            txt = get_text_clean(item).replace("¶", "").strip()
            if txt:
                constants.append(txt)

    # ── C# code examples ──
    csharp_examples = extract_csharp_code_blocks(soup)

    return {
        "class_name": class_name,
        "inherits": inherits,
        "inherited_by": inherited_by,
        "brief": brief,
        "properties": properties,
        "methods": methods,
        "signals": signals,
        "enums": enums,
        "constants": constants,
        "csharp_examples": csharp_examples,
    }


# ─── Markdown rendering ───────────────────────────────────────────────────────

def render_class_markdown(cls: dict) -> str:
    lines = []
    lines.append(f"### {cls['class_name']}")

    meta = []
    if cls["inherits"]:
        meta.append(f"Inherits: **{cls['inherits']}**")
    if cls["inherited_by"]:
        top_children = cls["inherited_by"][:6]
        suffix = ", ..." if len(cls["inherited_by"]) > 6 else ""
        meta.append(f"Inherited by: {', '.join(top_children)}{suffix}")
    if meta:
        lines.append("*" + " | ".join(meta) + "*")

    if cls["brief"]:
        lines.append("")
        lines.append(cls["brief"])

    if cls["properties"]:
        lines.append("")
        lines.append("**Properties**")
        for p in cls["properties"][:30]:  # cap for size
            default = f" = `{p['default']}`" if p["default"] else ""
            lines.append(f"- `{p['type']} {p['name']}`{default}")

    if cls["methods"]:
        lines.append("")
        lines.append("**Methods**")
        for m in cls["methods"][:40]:  # cap for size
            desc = f" — {m['description']}" if m.get("description") else ""
            lines.append(f"- `{m['return_type']} {m['signature']}`{desc}")

    if cls["signals"]:
        lines.append("")
        lines.append("**Signals**")
        for s in cls["signals"][:20]:
            lines.append(f"- `{s}`")

    if cls["enums"]:
        lines.append("")
        lines.append("**Enums**")
        for e in cls["enums"][:10]:
            lines.append(f"- `{e['name']}`" + (f": {', '.join(e['values'][:5])}" if e["values"] else ""))

    if cls["constants"]:
        lines.append("")
        lines.append("**Constants**")
        for c in cls["constants"][:20]:
            lines.append(f"- `{c}`")

    if cls["csharp_examples"]:
        lines.append("")
        lines.append("**C# Examples**")
        for example in cls["csharp_examples"][:2]:  # max 2 examples per class
            snippet = example.strip()
            if len(snippet) > 600:
                snippet = snippet[:600] + "\n// ..."
            lines.append("```csharp")
            lines.append(snippet)
            lines.append("```")

    lines.append("")
    return "\n".join(lines)


# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    docs_dir = Path(__file__).parent
    classes_dir = docs_dir / "classes"
    output_dir = docs_dir / "godot_csharp_skills"
    output_dir.mkdir(exist_ok=True)

    html_files = sorted(classes_dir.glob("class_*.html"))
    print(f"Found {len(html_files)} class HTML files")

    # Parse all classes
    by_domain: dict[str, list[dict]] = {}
    errors = []
    for i, html_file in enumerate(html_files):
        if i % 100 == 0:
            print(f"  Parsing {i}/{len(html_files)}...")
        try:
            cls = parse_class_page(html_file)
            if cls is None:
                continue
            domain = domain_for_class(cls["class_name"])
            by_domain.setdefault(domain, []).append(cls)
        except Exception as e:
            errors.append((html_file.name, str(e)))

    if errors:
        print(f"\nWARNING: {len(errors)} parse errors:")
        for fname, err in errors[:10]:
            print(f"  {fname}: {err}")

    # Domain summary
    print("\nDomain distribution:")
    for domain in sorted(by_domain.keys()):
        count = len(by_domain[domain])
        print(f"  {domain:20s} {count:4d} classes")

    TOKEN_SPLIT_THRESHOLD = 55_000

    def write_domain(domain: str, classes: list[dict]) -> list[tuple]:
        """Write one or more skill files for a domain. Returns list of (fname, count, kb, tokens)."""
        classes.sort(key=lambda c: c["class_name"])
        written = []

        # Estimate total tokens
        full_content = "\n".join(render_class_markdown(c) for c in classes)
        total_tokens = len(full_content) // 4

        if total_tokens <= TOKEN_SPLIT_THRESHOLD:
            content = f"# Godot 4 C# API Reference — {domain.replace('_', ' ').title()}\n\n> C#-only reference. {len(classes)} classes.\n\n" + full_content
            out_file = output_dir / f"godot_csharp_{domain}.md"
            out_file.write_text(content, encoding="utf-8")
            tokens = len(content) // 4
            size_kb = len(content) // 1024
            written.append((out_file.name, len(classes), size_kb, tokens))
            print(f"  Wrote {out_file.name} ({len(classes)} classes, {size_kb} KB, ~{tokens:,} tokens)")
        else:
            # Split into alphabetical chunks
            chunk: list[dict] = []
            chunk_tokens = 0
            part = 1
            for cls in classes:
                cls_md = render_class_markdown(cls)
                cls_tokens = len(cls_md) // 4
                if chunk and chunk_tokens + cls_tokens > TOKEN_SPLIT_THRESHOLD:
                    # Write current chunk
                    content = f"# Godot 4 C# API Reference — {domain.replace('_', ' ').title()} (Part {part})\n\n> C#-only reference. {len(chunk)} classes.\n\n" + "\n".join(render_class_markdown(c) for c in chunk)
                    out_file = output_dir / f"godot_csharp_{domain}_part{part}.md"
                    out_file.write_text(content, encoding="utf-8")
                    tokens = len(content) // 4
                    size_kb = len(content) // 1024
                    written.append((out_file.name, len(chunk), size_kb, tokens))
                    print(f"  Wrote {out_file.name} ({len(chunk)} classes, {size_kb} KB, ~{tokens:,} tokens)")
                    part += 1
                    chunk = [cls]
                    chunk_tokens = cls_tokens
                else:
                    chunk.append(cls)
                    chunk_tokens += cls_tokens
            if chunk:
                suffix = f" (Part {part})" if part > 1 else ""
                fname_suffix = f"_part{part}" if part > 1 else ""
                content = f"# Godot 4 C# API Reference — {domain.replace('_', ' ').title()}{suffix}\n\n> C#-only reference. {len(chunk)} classes.\n\n" + "\n".join(render_class_markdown(c) for c in chunk)
                out_file = output_dir / f"godot_csharp_{domain}{fname_suffix}.md"
                out_file.write_text(content, encoding="utf-8")
                tokens = len(content) // 4
                size_kb = len(content) // 1024
                written.append((out_file.name, len(chunk), size_kb, tokens))
                print(f"  Wrote {out_file.name} ({len(chunk)} classes, {size_kb} KB, ~{tokens:,} tokens)")
        return written

    # Write skill files
    all_files = []
    for domain, classes in sorted(by_domain.items()):
        all_files.extend(write_domain(domain, classes))

    # Write index
    index_lines = [
        "# Godot 4 C# API Reference — Index\n",
        "This index lists all available C#-specific Godot 4 API skill files.\n",
        "Load the relevant skill file(s) when answering questions about Godot C# development.\n\n",
        "## Skill Files\n",
    ]
    for fname, count, size_kb, tokens in sorted(all_files):
        domain_label = fname.replace("godot_csharp_", "").replace(".md", "").replace("_", " ").title()
        index_lines.append(f"- **{domain_label}** (`{fname}`) — {count} classes, ~{tokens:,} tokens")
    index_lines.append("")
    index_lines.append("## Usage\n")
    index_lines.append("When a user asks about a Godot class or concept, identify the domain and load the appropriate file.")
    index_lines.append("All code examples are C# only. All method names are PascalCase.")
    index_lines.append("Types use Godot's C# bindings (e.g., `Godot.Collections.Array`, `StringName`, `NodePath`).\n")

    index_path = output_dir / "godot_csharp_index.md"
    index_path.write_text("\n".join(index_lines), encoding="utf-8")
    print(f"\nWrote index: {index_path}")
    print("\nDone.")


if __name__ == "__main__":
    main()
