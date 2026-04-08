#!/usr/bin/env python3
"""
Godot GDScript API Reference Extractor
Parses Godot HTML docs and produces condensed GDScript-specific Markdown skill files.
"""

import os
import re
import sys
from pathlib import Path
from bs4 import BeautifulSoup, Tag


# ─── Domain bucketing ─────────────────────────────────────────────────────────
# Maps output skill filename → list of class name prefixes/exact names.
# Classes not matched by any rule go to "misc".
DOMAIN_RULES = [
    (
        "core",
        [
            "Object",
            "Node",
            "SceneTree",
            "Resource",
            "RefCounted",
            "MainLoop",
            "WeakRef",
            "ClassDB",
            "Engine",
            "OS",
            "Marshalls",
            "MessageQueue",
            "Performance",
            "WorkerThreadPool",
            "Semaphore",
            "Mutex",
            "Thread",
            "EngineDebugger",
            "ResourceLoader",
            "ResourceSaver",
            "ResourceUID",
        ],
    ),
    (
        "nodes_2d",
        [
            "Node2D",
            "Sprite2D",
            "AnimatedSprite2D",
            "Camera2D",
            "CanvasItem",
            "CanvasLayer",
            "CanvasModulate",
            "CollisionObject2D",
            "CollisionPolygon2D",
            "CollisionShape2D",
            "CPUParticles2D",
            "GPUParticles2D",
            "Light2D",
            "LightOccluder2D",
            "Line2D",
            "Marker2D",
            "MeshInstance2D",
            "MultiMeshInstance2D",
            "NavigationAgent2D",
            "NavigationLink2D",
            "NavigationObstacle2D",
            "NavigationRegion2D",
            "Path2D",
            "PathFollow2D",
            "Polygon2D",
            "RayCast2D",
            "RemoteTransform2D",
            "Skeleton2D",
            "StaticBody2D",
            "TileMap",
            "TileMapLayer",
            "TouchScreenButton",
            "VisibleOnScreenEnabler2D",
            "VisibleOnScreenNotifier2D",
            "AnimatableBody2D",
            "CharacterBody2D",
            "RigidBody2D",
            "Joint2D",
            "DampedSpringJoint2D",
            "GrooveJoint2D",
            "PinJoint2D",
        ],
    ),
    (
        "nodes_3d",
        [
            "Node3D",
            "Camera3D",
            "MeshInstance3D",
            "DirectionalLight3D",
            "OmniLight3D",
            "SpotLight3D",
            "Light3D",
            "ReflectionProbe",
            "GpuParticles3D",
            "CpuParticles3D",
            "Decal",
            "FogVolume",
            "WorldEnvironment",
            "LightmapGI",
            "LightmapProbe",
            "VoxelGI",
            "Skeleton3D",
            "BoneAttachment3D",
            "Marker3D",
            "Path3D",
            "PathFollow3D",
            "RemoteTransform3D",
            "VisualInstance3D",
            "GeometryInstance3D",
            "MultiMeshInstance3D",
            "AnimatableBody3D",
            "CharacterBody3D",
            "RigidBody3D",
            "StaticBody3D",
            "VehicleBody3D",
            "VehicleWheel3D",
            "SoftBody3D",
            "NavigationAgent3D",
            "NavigationLink3D",
            "NavigationObstacle3D",
            "NavigationRegion3D",
            "RayCast3D",
            "ShapeCast3D",
            "SpringArm3D",
            "XR",
        ],
    ),
    (
        "physics",
        [
            "PhysicsServer2D",
            "PhysicsServer3D",
            "PhysicsBody2D",
            "PhysicsBody3D",
            "PhysicsDirectBodyState2D",
            "PhysicsDirectBodyState3D",
            "PhysicsDirectSpaceState2D",
            "PhysicsDirectSpaceState3D",
            "PhysicsMaterial",
            "PhysicsPointQueryParameters2D",
            "PhysicsPointQueryParameters3D",
            "PhysicsRayQueryParameters2D",
            "PhysicsRayQueryParameters3D",
            "PhysicsShapeQueryParameters2D",
            "PhysicsShapeQueryParameters3D",
            "PhysicsTestMotionParameters2D",
            "PhysicsTestMotionParameters3D",
            "PhysicsTestMotionResult2D",
            "PhysicsTestMotionResult3D",
            "Shape2D",
            "Shape3D",
            "CollisionShape2D",
            "CollisionShape3D",
            "CollisionPolygon2D",
            "CollisionPolygon3D",
            "Joint3D",
            "Generic6DOFJoint3D",
            "HingeJoint3D",
            "PinJoint3D",
            "SliderJoint3D",
            "ConeTwistJoint3D",
            "Area2D",
            "Area3D",
        ],
    ),
    (
        "ui_controls",
        [
            "Control",
            "Button",
            "Label",
            "LineEdit",
            "TextEdit",
            "RichTextLabel",
            "Panel",
            "PanelContainer",
            "Container",
            "BoxContainer",
            "HBoxContainer",
            "VBoxContainer",
            "GridContainer",
            "MarginContainer",
            "ScrollContainer",
            "TabContainer",
            "SplitContainer",
            "HSplitContainer",
            "VSplitContainer",
            "CenterContainer",
            "AspectRatioContainer",
            "FlowContainer",
            "SubViewportContainer",
            "TextureRect",
            "ColorRect",
            "Tree",
            "ItemList",
            "OptionButton",
            "MenuButton",
            "CheckBox",
            "CheckButton",
            "LinkButton",
            "TextureButton",
            "BaseButton",
            "Range",
            "Slider",
            "HSlider",
            "VSlider",
            "ScrollBar",
            "HScrollBar",
            "VScrollBar",
            "ProgressBar",
            "SpinBox",
            "ColorPicker",
            "ColorPickerButton",
            "FileDialog",
            "AcceptDialog",
            "ConfirmationDialog",
            "Popup",
            "PopupMenu",
            "PopupPanel",
            "Window",
            "Tooltip",
            "GraphEdit",
            "GraphNode",
            "GraphFrame",
            "TabBar",
            "CodeEdit",
            "VideoStreamPlayer",
        ],
    ),
    (
        "rendering",
        [
            "RenderingServer",
            "RenderingDevice",
            "Viewport",
            "SubViewport",
            "Environment",
            "CameraAttributes",
            "Sky",
            "Fog",
            "Material",
            "ShaderMaterial",
            "BaseMaterial3D",
            "StandardMaterial3D",
            "ORMMaterial3D",
            "CanvasItemMaterial",
            "ParticleProcessMaterial",
            "Shader",
            "VisualShader",
            "VisualShaderNode",
            "Mesh",
            "ArrayMesh",
            "ImmediateMesh",
            "PrimitiveMesh",
            "BoxMesh",
            "CapsuleMesh",
            "CylinderMesh",
            "PlaneMesh",
            "QuadMesh",
            "SphereMesh",
            "RibbonTrailMesh",
            "TubeTrailMesh",
            "MultiMesh",
            "SurfaceTool",
            "MeshDataTool",
            "CompositorEffect",
            "Compositor",
            "RDShaderFile",
        ],
    ),
    (
        "audio",
        [
            "AudioStreamPlayer",
            "AudioStreamPlayer2D",
            "AudioStreamPlayer3D",
            "AudioServer",
            "AudioBusLayout",
            "AudioEffect",
            "AudioStream",
            "AudioStreamGenerator",
            "AudioStreamGeneratorPlayback",
            "AudioStreamMicrophone",
            "AudioStreamPlayback",
            "AudioStreamWav",
            "AudioStreamOggVorbis",
            "AudioStreamMP3",
            "AudioEffectAmplify",
            "AudioEffectBandLimitFilter",
            "AudioEffectBandPassFilter",
            "AudioEffectCapture",
            "AudioEffectChorus",
            "AudioEffectCompressor",
            "AudioEffectDelay",
            "AudioEffectDistortion",
            "AudioEffectEQ",
            "AudioEffectFilter",
            "AudioEffectHighPassFilter",
            "AudioEffectHighShelfFilter",
            "AudioEffectLimiter",
            "AudioEffectLowPassFilter",
            "AudioEffectLowShelfFilter",
            "AudioEffectNotchFilter",
            "AudioEffectPanner",
            "AudioEffectPhaser",
            "AudioEffectPitchShift",
            "AudioEffectRecord",
            "AudioEffectReverb",
            "AudioEffectSpectrumAnalyzer",
            "AudioEffectStereoEnhance",
        ],
    ),
    (
        "input",
        [
            "Input",
            "InputEvent",
            "InputEventKey",
            "InputEventMouse",
            "InputEventMouseButton",
            "InputEventMouseMotion",
            "InputEventJoypad",
            "InputEventJoypadButton",
            "InputEventJoypadMotion",
            "InputEventAction",
            "InputEventGesture",
            "InputEventMagnifyGesture",
            "InputEventPanGesture",
            "InputEventMIDI",
            "InputEventScreenDrag",
            "InputEventScreenTouch",
            "InputEventWithModifiers",
            "InputMap",
            "ShortCut",
        ],
    ),
    (
        "math_types",
        [
            "Vector2",
            "Vector2i",
            "Vector3",
            "Vector3i",
            "Vector4",
            "Vector4i",
            "Transform2D",
            "Transform3D",
            "Basis",
            "Quaternion",
            "AABB",
            "Rect2",
            "Rect2i",
            "Plane",
            "Color",
            "Projection",
            "RID",
        ],
    ),
    (
        "resources",
        [
            "Texture",
            "Texture2D",
            "Texture3D",
            "TextureLayered",
            "CompressedTexture2D",
            "ImageTexture",
            "PortableCompressedTexture2D",
            "AtlasTexture",
            "AnimatedTexture",
            "CameraTexture",
            "GradientTexture1D",
            "GradientTexture2D",
            "NoiseTexture2D",
            "PlaceholderTexture2D",
            "ViewportTexture",
            "Image",
            "Gradient",
            "Curve",
            "Curve2D",
            "Curve3D",
            "Font",
            "FontFile",
            "FontVariation",
            "SystemFont",
            "BitMap",
            "TileSet",
            "TileSetAtlasSource",
            "TileSetScenesCollectionSource",
            "TileSetSource",
            "TileData",
            "StyleBox",
            "StyleBoxEmpty",
            "StyleBoxFlat",
            "StyleBoxLine",
            "StyleBoxTexture",
            "Theme",
            "PackedScene",
            "SceneState",
            "Script",
            "GDScript",
            "CSharpScript",
            "ScriptExtension",
            "Animation",
            "AnimationLibrary",
            "Noise",
            "FastNoiseLite",
            "OccluderInstance3D",
            "Occluder3D",
        ],
    ),
    (
        "networking",
        [
            "HTTPClient",
            "HTTPRequest",
            "WebSocketPeer",
            "WebSocketMultiplayerPeer",
            "ENetMultiplayerPeer",
            "ENetConnection",
            "ENetPacketPeer",
            "MultiplayerAPI",
            "MultiplayerPeer",
            "SceneMultiplayer",
            "StreamPeer",
            "StreamPeerBuffer",
            "StreamPeerExtension",
            "StreamPeerGZIP",
            "StreamPeerTCP",
            "StreamPeerTLS",
            "TCPServer",
            "PacketPeer",
            "PacketPeerDTLS",
            "PacketPeerExtension",
            "PacketPeerStream",
            "PacketPeerUDP",
            "DTLSServer",
            "UDPServer",
            "IP",
            "TLSOptions",
            "X509Certificate",
            "CryptoKey",
            "Crypto",
            "HMAC",
            "AESContext",
            "HashingContext",
        ],
    ),
    (
        "animation",
        [
            "AnimationPlayer",
            "AnimationTree",
            "AnimationMixer",
            "AnimationNode",
            "AnimationRootNode",
            "AnimationNodeAdd2",
            "AnimationNodeAdd3",
            "AnimationNodeAnimation",
            "AnimationNodeBlend2",
            "AnimationNodeBlend3",
            "AnimationNodeBlendSpace1D",
            "AnimationNodeBlendSpace2D",
            "AnimationNodeBlendTree",
            "AnimationNodeExtension",
            "AnimationNodeOneShot",
            "AnimationNodeOutput",
            "AnimationNodeStateMachine",
            "AnimationNodeStateMachinePlayback",
            "AnimationNodeStateMachineTransition",
            "AnimationNodeSub2",
            "AnimationNodeSync",
            "AnimationNodeTimeScale",
            "AnimationNodeTimeSeek",
            "AnimationNodeTransition",
            "Tween",
            "Tweener",
            "MethodTweener",
            "PropertyTweener",
            "CallbackTweener",
            "IntervalTweener",
            "SkeletonModificationStack2D",
            "SkeletonModification2D",
            "SkeletonIK3D",
            "SkeletonModifier3D",
            "AimModifier3D",
            "LookAtModifier3D",
        ],
    ),
    (
        "filesystem",
        [
            "FileAccess",
            "DirAccess",
            "ProjectSettings",
            "EditorSettings",
            "ConfigFile",
            "JSON",
            "XMLParser",
            "ZIPReader",
            "ZIPPacker",
            "PCKPacker",
            "ResourceImporter",
        ],
    ),
    (
        "editor",
        [
            "Editor",  # prefix match — catches all Editor* classes
        ],
    ),
]


# ─── Helpers ──────────────────────────────────────────────────────────────────


def get_text_clean(tag) -> str:
    if tag is None:
        return ""
    return re.sub(r"\s+", " ", tag.get_text()).strip()


def extract_gdscript_code_blocks(soup: BeautifulSoup) -> list[str]:
    """Return list of GDScript code block texts from sphinx tabs."""
    blocks = []
    # GDScript tab panels have name="R0RTY3JpcHQ=" (base64 of "GDScript")
    for panel in soup.find_all("div", attrs={"name": "R0RTY3JpcHQ="}):
        code = panel.find("pre")
        if code:
            blocks.append(code.get_text())
    # Also grab standalone highlight-gdscript blocks (no tab)
    for block in soup.find_all("div", class_="highlight-gdscript"):
        # skip if inside a tab panel (already captured above)
        if not block.find_parent("div", attrs={"name": "R0RTY3JpcHQ="}):
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
    title_tag = soup.find("h1")
    if not title_tag:
        return None
    class_name = get_text_clean(title_tag)
    class_name = class_name.replace("¶", "").strip()

    # ── Inheritance ──
    inherits = ""
    inherited_by = []
    for p in soup.select("p.class-info, p"):
        txt = get_text_clean(p)
        if txt.startswith("Inherits:"):
            inherits = txt.replace("Inherits:", "").strip()
        elif txt.startswith("Inherited By:"):
            inherited_by = [
                s.strip() for s in txt.replace("Inherited By:", "").split(",")
            ]

    # ── Brief description ──
    brief = ""
    brief_section = soup.find("section", id="description") or soup.find(
        "div", class_="brief-description"
    )
    if brief_section:
        first_p = brief_section.find("p")
        if first_p:
            brief = get_text_clean(first_p)
    if not brief:
        article = soup.find("article") or soup.find("div", class_="rst-content")
        if article:
            paras = article.find_all("p")
            for p in paras:
                txt = get_text_clean(p)
                if (
                    txt
                    and not txt.startswith("Inherits")
                    and not txt.startswith("Inherited")
                ):
                    brief = txt
                    break

    # ── Properties ──
    properties = []
    prop_table = soup.find("table", class_=re.compile(r"properties"))
    if not prop_table:
        prop_section = soup.find("section", id="properties")
        if prop_section:
            prop_table = prop_section.find("table")
    if prop_table:
        for row in prop_table.find_all("tr"):
            cells = row.find_all(["td", "th"])
            if len(cells) >= 2:
                prop_type = get_text_clean(cells[0]).replace("¶", "").strip()
                prop_name = get_text_clean(cells[1]).replace("¶", "").strip()
                default = (
                    get_text_clean(cells[2]).replace("¶", "").strip()
                    if len(cells) > 2
                    else ""
                )
                if prop_type and prop_name and prop_name not in ("Name", "Default"):
                    properties.append(
                        {
                            "type": prop_type,
                            "name": prop_name,
                            "default": default,
                        }
                    )

    # ── Methods ──
    methods = []
    method_section = soup.find("section", id="methods")
    if not method_section:
        method_section = soup.find("section", id="method-descriptions")
    method_table = None
    if method_section:
        method_table = method_section.find("table")
    if method_table:
        for row in method_table.find_all("tr"):
            cells = row.find_all(["td", "th"])
            if len(cells) >= 2:
                ret_type = get_text_clean(cells[0]).replace("¶", "").strip()
                sig = get_text_clean(cells[1]).replace("¶", "").strip()
                if ret_type and sig:
                    methods.append(
                        {"return_type": ret_type, "signature": sig, "description": ""}
                    )

    # Add one-line descriptions from method-descriptions section
    desc_section = soup.find("section", id="method-descriptions")
    if desc_section:
        for item in desc_section.find_all(["dt", "section"]):
            method_id = item.get("id", "")
            if not method_id:
                continue
            first_p = item.find_next("p")
            desc = get_text_clean(first_p) if first_p else ""
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

    # ── GDScript code examples ──
    gdscript_examples = extract_gdscript_code_blocks(soup)

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
        "gdscript_examples": gdscript_examples,
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
            lines.append(
                f"- `{e['name']}`"
                + (f": {', '.join(e['values'][:5])}" if e["values"] else "")
            )

    if cls["constants"]:
        lines.append("")
        lines.append("**Constants**")
        for c in cls["constants"][:20]:
            lines.append(f"- `{c}`")

    if cls["gdscript_examples"]:
        lines.append("")
        lines.append("**GDScript Examples**")
        for example in cls["gdscript_examples"][:2]:  # max 2 examples per class
            snippet = example.strip()
            if len(snippet) > 600:
                snippet = snippet[:600] + "\n# ..."
            lines.append("```gdscript")
            lines.append(snippet)
            lines.append("```")

    lines.append("")
    return "\n".join(lines)


# ─── Main ─────────────────────────────────────────────────────────────────────


def main():
    docs_dir = Path(__file__).parent / "godot-docs-html-stable"
    classes_dir = docs_dir / "classes"
    output_dir = Path(__file__).parent / "references"
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

        full_content = "\n".join(render_class_markdown(c) for c in classes)
        total_tokens = len(full_content) // 4

        if total_tokens <= TOKEN_SPLIT_THRESHOLD:
            content = (
                f"# Godot 4 GDScript API Reference — {domain.replace('_', ' ').title()}\n\n> GDScript-only reference. {len(classes)} classes.\n\n"
                + full_content
            )
            out_file = output_dir / f"godot_gdscript_{domain}.md"
            out_file.write_text(content, encoding="utf-8")
            tokens = len(content) // 4
            size_kb = len(content) // 1024
            written.append((out_file.name, len(classes), size_kb, tokens))
            print(
                f"  Wrote {out_file.name} ({len(classes)} classes, {size_kb} KB, ~{tokens:,} tokens)"
            )
        else:
            # Split into alphabetical chunks
            chunk: list[dict] = []
            chunk_tokens = 0
            part = 1
            for cls in classes:
                cls_md = render_class_markdown(cls)
                cls_tokens = len(cls_md) // 4
                if chunk and chunk_tokens + cls_tokens > TOKEN_SPLIT_THRESHOLD:
                    content = (
                        f"# Godot 4 GDScript API Reference — {domain.replace('_', ' ').title()} (Part {part})\n\n> GDScript-only reference. {len(chunk)} classes.\n\n"
                        + "\n".join(render_class_markdown(c) for c in chunk)
                    )
                    out_file = output_dir / f"godot_gdscript_{domain}_part{part}.md"
                    out_file.write_text(content, encoding="utf-8")
                    tokens = len(content) // 4
                    size_kb = len(content) // 1024
                    written.append((out_file.name, len(chunk), size_kb, tokens))
                    print(
                        f"  Wrote {out_file.name} ({len(chunk)} classes, {size_kb} KB, ~{tokens:,} tokens)"
                    )
                    part += 1
                    chunk = [cls]
                    chunk_tokens = cls_tokens
                else:
                    chunk.append(cls)
                    chunk_tokens += cls_tokens
            if chunk:
                suffix = f" (Part {part})" if part > 1 else ""
                fname_suffix = f"_part{part}" if part > 1 else ""
                content = (
                    f"# Godot 4 GDScript API Reference — {domain.replace('_', ' ').title()}{suffix}\n\n> GDScript-only reference. {len(chunk)} classes.\n\n"
                    + "\n".join(render_class_markdown(c) for c in chunk)
                )
                out_file = output_dir / f"godot_gdscript_{domain}{fname_suffix}.md"
                out_file.write_text(content, encoding="utf-8")
                tokens = len(content) // 4
                size_kb = len(content) // 1024
                written.append((out_file.name, len(chunk), size_kb, tokens))
                print(
                    f"  Wrote {out_file.name} ({len(chunk)} classes, {size_kb} KB, ~{tokens:,} tokens)"
                )
        return written

    # Write skill files
    all_files = []
    for domain, classes in sorted(by_domain.items()):
        all_files.extend(write_domain(domain, classes))

    # Write index
    index_lines = [
        "# Godot 4 GDScript API Reference — Index\n",
        "This index lists all available GDScript-specific Godot 4 API skill files.\n",
        "Load the relevant skill file(s) when answering questions about Godot GDScript development.\n\n",
        "## Skill Files\n",
    ]
    for fname, count, size_kb, tokens in sorted(all_files):
        domain_label = (
            fname.replace("godot_gdscript_", "")
            .replace(".md", "")
            .replace("_", " ")
            .title()
        )
        index_lines.append(
            f"- **{domain_label}** (`{fname}`) — {count} classes, ~{tokens:,} tokens"
        )
    index_lines.append("")
    index_lines.append("## Usage\n")
    index_lines.append(
        "When a user asks about a Godot class or concept, identify the domain and load the appropriate file."
    )
    index_lines.append(
        "All method and property names are snake_case (GDScript convention)."
    )
    index_lines.append(
        "Types use GDScript built-in names (e.g., `String`, `int`, `float`, `Array`, `Dictionary`, `Callable`, `Variant`).\n"
    )

    index_path = output_dir / "godot_gdscript_index.md"
    index_path.write_text("\n".join(index_lines), encoding="utf-8")
    print(f"\nWrote index: {index_path}")
    print("\nDone.")


if __name__ == "__main__":
    main()
