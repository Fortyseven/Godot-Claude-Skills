#!/usr/bin/env python3
"""
Godot Tutorial Extractor
Parses Godot HTML tutorial docs and produces condensed Markdown files
for both the GDScript and C# skills, with language-specific code blocks.
Converts internal links to relative skill file references.
"""

import re
import sys
from pathlib import Path
from bs4 import BeautifulSoup, NavigableString, Tag

# ─── Domain rules (copied from existing extraction scripts) ───────────────────
# Used to resolve class doc links → skill file references.
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

# Build flat lookup: class_name → domain
_CLASS_DOMAIN_CACHE: dict[str, str] = {}


def domain_for_class(class_name: str) -> str:
    if class_name in _CLASS_DOMAIN_CACHE:
        return _CLASS_DOMAIN_CACHE[class_name]
    for domain, names in DOMAIN_RULES:
        for n in names:
            if domain == "editor" and class_name.startswith("Editor"):
                _CLASS_DOMAIN_CACHE[class_name] = "editor"
                return "editor"
            if class_name == n:
                _CLASS_DOMAIN_CACHE[class_name] = domain
                return domain
            if class_name.startswith(n) and len(n) >= 6:
                _CLASS_DOMAIN_CACHE[class_name] = domain
                return domain
    _CLASS_DOMAIN_CACHE[class_name] = "misc"
    return "misc"


# ─── Tutorial category from file path ────────────────────────────────────────

TUTORIAL_CATEGORIES = [
    "2d",
    "3d",
    "animation",
    "assets_pipeline",
    "audio",
    "best_practices",
    "editor",
    "export",
    "i18n",
    "inputs",
    "io",
    "math",
    "migrating",
    "navigation",
    "networking",
    "performance",
    "physics",
    "platform",
    "plugins",
    "rendering",
    "scripting",
    "shaders",
    "ui",
    "xr",
]


def category_from_path(rel_path: str) -> str:
    """Get tutorial category from path relative to tutorials/."""
    parts = Path(rel_path).parts
    if len(parts) >= 1 and parts[0] in TUTORIAL_CATEGORIES:
        return parts[0]
    return "general"


# Map tutorial categories to related API reference domains for cross-linking
CATEGORY_TO_API_DOMAINS = {
    "2d": ["nodes_2d", "physics"],
    "3d": ["nodes_3d", "physics", "rendering"],
    "animation": ["animation"],
    "audio": ["audio"],
    "inputs": ["input"],
    "io": ["filesystem"],
    "math": ["math_types"],
    "navigation": ["nodes_2d", "nodes_3d"],
    "networking": ["networking"],
    "physics": ["physics"],
    "rendering": ["rendering"],
    "shaders": ["rendering"],
    "ui": ["ui_controls"],
    "xr": ["nodes_3d"],
}


# ─── Link resolution ─────────────────────────────────────────────────────────

# Pattern: ../../classes/class_characterbody2d.html#...
CLASS_LINK_RE = re.compile(r".*?/classes/class_(\w+)\.html")
# Pattern: ../2d/2d_movement.html or ../../tutorials/2d/2d_movement.html
TUTORIAL_LINK_RE = re.compile(r".*?tutorials/(\w+)/.*\.html")
# Pattern for relative tutorial links within same or neighbor dir
RELATIVE_TUTORIAL_RE = re.compile(r"^\.\.?/(\w+)/.*\.html|^(\w+\.html)")


def resolve_class_link(href: str, link_text: str, lang: str) -> str:
    """Convert a class doc link to a skill file reference."""
    m = CLASS_LINK_RE.match(href)
    if m:
        raw_name = m.group(1)
        # class_name from href is lowercase, but link_text has proper casing
        class_name = link_text.strip()
        if class_name:
            domain = domain_for_class(class_name)
            prefix = "godot_gdscript" if lang == "gdscript" else "godot_csharp"
            domain_file = f"{prefix}_{domain}.md"
            return f"[{class_name}](../{domain_file})"
    return f"`{link_text.strip()}`"


def resolve_tutorial_link(href: str, link_text: str, current_category: str) -> str:
    """Convert a tutorial cross-link to a relative file reference."""
    # Try full tutorial path pattern
    m = TUTORIAL_LINK_RE.match(href)
    if m:
        target_cat = m.group(1)
        if target_cat in TUTORIAL_CATEGORIES:
            return f"[{link_text.strip()}](tutorials_{target_cat}.md)"
    return f"[{link_text.strip()}]()"


def resolve_link(href: str, link_text: str, lang: str, current_category: str) -> str:
    """Resolve an internal link to the appropriate reference."""
    text = link_text.strip()
    if not text:
        return ""
    if not href:
        return text

    # External links — keep as-is
    if href.startswith("http://") or href.startswith("https://"):
        return f"[{text}]({href})"

    # Class doc links
    if "/classes/class_" in href:
        return resolve_class_link(href, text, lang)

    # Tutorial cross-links
    if "/tutorials/" in href or TUTORIAL_LINK_RE.match(href):
        m = TUTORIAL_LINK_RE.match(href)
        if m:
            target_cat = m.group(1)
            if target_cat in TUTORIAL_CATEGORIES:
                return f"[{text}](tutorials_{target_cat}.md)"

    # Relative links to other tutorials in same/sibling dirs
    # e.g. ../2d/2d_movement.html, 2d_movement.html, ../physics/...
    for cat in TUTORIAL_CATEGORIES:
        if (
            f"/{cat}/" in href
            or href.startswith(f"{cat}/")
            or href.startswith(f"../{cat}/")
        ):
            return f"[{text}](tutorials_{cat}.md)"

    # Section anchor links within same page
    if href.startswith("#"):
        return f"**{text}**"

    # Getting started, about, or other non-tutorial internal links
    if "/getting_started/" in href:
        return f"{text} (see Getting Started docs)"
    if "/about/" in href:
        return f"{text} (see About docs)"

    # Fallback: just use the text
    return text


# ─── HTML → Markdown extraction ──────────────────────────────────────────────


def get_text_clean(tag) -> str:
    if tag is None:
        return ""
    return re.sub(r"\s+", " ", tag.get_text()).strip()


def extract_code_blocks(soup: BeautifulSoup, lang: str) -> list[str]:
    """Extract code blocks for the specified language."""
    blocks = []
    if lang == "gdscript":
        tab_name = "R0RTY3JpcHQ="  # base64 of "GDScript"
        highlight_class = "highlight-gdscript"
    else:
        tab_name = "QyM="  # base64 of "C#"
        highlight_class = "highlight-csharp"

    # Tabbed code blocks
    for panel in soup.find_all("div", attrs={"name": tab_name}):
        code = panel.find("pre")
        if code:
            blocks.append(code.get_text())

    # Standalone code blocks (not inside a tab)
    for block in soup.find_all("div", class_=highlight_class):
        if not block.find_parent("div", attrs={"name": tab_name}):
            pre = block.find("pre")
            if pre:
                blocks.append(pre.get_text())

    return blocks


def convert_element_to_markdown(
    element, lang: str, category: str, depth: int = 0
) -> str:
    """Recursively convert an HTML element to condensed markdown."""
    if isinstance(element, NavigableString):
        text = str(element)
        # Collapse whitespace in inline text
        return re.sub(r"\s+", " ", text)

    if not isinstance(element, Tag):
        return ""

    tag_name = element.name

    # Skip unwanted elements
    if tag_name in ("script", "style", "nav", "footer", "header"):
        return ""
    if element.get("class") and any(
        c in element.get("class", [])
        for c in [
            "headerlink",
            "wy-breadcrumbs",
            "wy-nav-side",
            "wy-nav-top",
            "rst-footer-buttons",
            "sphinx-contrib-video-container",
        ]
    ):
        return ""

    # Skip images and videos
    if tag_name in ("img", "video", "source", "figure"):
        return ""

    # Skip figure captions (they describe images we're stripping)
    if tag_name == "figcaption":
        return ""
    if tag_name == "figure":
        return ""

    # Headings
    if tag_name in ("h1", "h2", "h3", "h4", "h5", "h6"):
        level = int(tag_name[1])
        text = get_text_clean(element).replace("¶", "").strip()
        if not text:
            return ""
        prefix = "#" * min(
            level + 1, 6
        )  # shift down one level since we use ## for tutorial title
        return f"\n\n{prefix} {text}\n\n"

    # Links
    if tag_name == "a":
        href = element.get("href", "")
        text = get_text_clean(element)
        if not text:
            return ""
        return resolve_link(href, text, lang, category)

    # Code (inline)
    if tag_name == "code":
        text = get_text_clean(element)
        if text:
            return f"`{text}`"
        return ""

    # Bold / emphasis
    if tag_name in ("strong", "b"):
        text = get_text_clean(element)
        return f"**{text}**" if text else ""
    if tag_name in ("em", "i"):
        text = get_text_clean(element)
        return f"*{text}*" if text else ""

    # Sphinx tabs container — handle specially
    if (
        tag_name == "div"
        and element.get("class")
        and "sphinx-tabs" in element.get("class", [])
    ):
        # Extract only the code block for our language
        code_blocks = extract_code_blocks(element, lang)
        if code_blocks:
            lang_label = "gdscript" if lang == "gdscript" else "csharp"
            result = []
            for block in code_blocks:
                snippet = block.strip()
                if len(snippet) > 800:
                    snippet = (
                        snippet[:800] + "\n# ..."
                        if lang == "gdscript"
                        else snippet[:800] + "\n// ..."
                    )
                result.append(f"\n```{lang_label}\n{snippet}\n```\n")
            return "\n".join(result)
        return ""

    # Standalone code highlight blocks (non-tabbed)
    if tag_name == "div" and element.get("class"):
        classes = element.get("class", [])
        target_highlight = (
            "highlight-gdscript" if lang == "gdscript" else "highlight-csharp"
        )
        other_highlight = (
            "highlight-csharp" if lang == "gdscript" else "highlight-gdscript"
        )

        if target_highlight in classes:
            pre = element.find("pre")
            if pre:
                snippet = pre.get_text().strip()
                lang_label = "gdscript" if lang == "gdscript" else "csharp"
                if len(snippet) > 800:
                    snippet = snippet[:800] + (
                        "\n# ..." if lang == "gdscript" else "\n// ..."
                    )
                return f"\n```{lang_label}\n{snippet}\n```\n"

        # Skip code blocks for the other language
        if other_highlight in classes:
            return ""

        # Also handle highlight-python, highlight-cfg, highlight-ini, etc.
        for cls in classes:
            if cls.startswith("highlight-") and cls not in (
                target_highlight,
                other_highlight,
            ):
                pre = element.find("pre")
                if pre:
                    snippet = pre.get_text().strip()
                    ext = cls.replace("highlight-", "")
                    if len(snippet) > 800:
                        snippet = snippet[:800] + "\n# ..."
                    return f"\n```{ext}\n{snippet}\n```\n"

    # Admonitions (tip, note, warning, etc.)
    if tag_name == "div" and element.get("class"):
        classes = element.get("class", [])
        for adm_type in (
            "tip",
            "note",
            "warning",
            "important",
            "seealso",
            "attention",
            "danger",
        ):
            if f"admonition-{adm_type}" in " ".join(classes) or adm_type in classes:
                title_tag = element.find("p", class_="admonition-title")
                title = get_text_clean(title_tag) if title_tag else adm_type.title()
                body_parts = []
                for child in element.children:
                    if (
                        isinstance(child, Tag)
                        and child.get("class")
                        and "admonition-title" in child.get("class", [])
                    ):
                        continue
                    part = convert_element_to_markdown(child, lang, category, depth + 1)
                    if part.strip():
                        body_parts.append(part.strip())
                body = " ".join(body_parts)
                if body:
                    return f"\n\n> **{title}:** {body}\n\n"
                return ""

    # Paragraphs
    if tag_name == "p":
        parts = []
        for child in element.children:
            parts.append(convert_element_to_markdown(child, lang, category, depth + 1))
        text = "".join(parts).strip()
        if text:
            return f"\n\n{text}\n\n"
        return ""

    # Lists
    if tag_name == "ul":
        items = []
        for li in element.find_all("li", recursive=False):
            item_text = ""
            for child in li.children:
                item_text += convert_element_to_markdown(
                    child, lang, category, depth + 1
                )
            item_text = item_text.strip()
            if item_text:
                items.append(f"- {item_text}")
        if items:
            return "\n\n" + "\n".join(items) + "\n\n"
        return ""

    if tag_name == "ol":
        items = []
        for i, li in enumerate(element.find_all("li", recursive=False), 1):
            item_text = ""
            for child in li.children:
                item_text += convert_element_to_markdown(
                    child, lang, category, depth + 1
                )
            item_text = item_text.strip()
            if item_text:
                items.append(f"{i}. {item_text}")
        if items:
            return "\n\n" + "\n".join(items) + "\n\n"
        return ""

    # Definition lists (dt/dd)
    if tag_name == "dl":
        items = []
        for child in element.children:
            if isinstance(child, Tag):
                if child.name == "dt":
                    text = get_text_clean(child).replace("¶", "").strip()
                    if text:
                        items.append(f"\n**{text}**")
                elif child.name == "dd":
                    text = ""
                    for sub in child.children:
                        text += convert_element_to_markdown(
                            sub, lang, category, depth + 1
                        )
                    text = text.strip()
                    if text:
                        items.append(f": {text}")
        if items:
            return "\n" + "\n".join(items) + "\n"
        return ""

    # Tables — render as simple markdown
    if tag_name == "table":
        rows = []
        for tr in element.find_all("tr"):
            cells = tr.find_all(["th", "td"])
            row = [get_text_clean(c).replace("|", "\\|") for c in cells]
            if row:
                rows.append("| " + " | ".join(row) + " |")
            # Add separator after header row
            if tr.find("th") and len(rows) == 1:
                rows.append("| " + " | ".join(["---"] * len(cells)) + " |")
        if rows:
            return "\n\n" + "\n".join(rows) + "\n\n"
        return ""

    # Generic container — recurse into children
    parts = []
    for child in element.children:
        parts.append(convert_element_to_markdown(child, lang, category, depth + 1))
    return "".join(parts)


def clean_markdown(text: str) -> str:
    """Clean up generated markdown: collapse blank lines, trim."""
    # Collapse 3+ newlines to 2
    text = re.sub(r"\n{3,}", "\n\n", text)
    # Remove trailing whitespace on lines
    text = re.sub(r"[ \t]+$", "", text, flags=re.MULTILINE)
    # Remove leading/trailing blank lines
    text = text.strip()
    return text


# ─── Tutorial parsing ────────────────────────────────────────────────────────


def parse_tutorial(html_path: Path, lang: str, category: str) -> dict | None:
    """Parse a tutorial HTML file and return structured data."""
    with open(html_path, encoding="utf-8") as f:
        soup = BeautifulSoup(f, "lxml")

    # Find main content
    content = soup.find("div", attrs={"itemprop": "articleBody"})
    if not content:
        content = soup.find("div", role="main")
    if not content:
        return None

    # Get title
    h1 = content.find("h1")
    if not h1:
        return None
    title = get_text_clean(h1).replace("¶", "").strip()
    if not title:
        return None

    # Remove the h1 so we don't duplicate it
    h1.decompose()

    # Convert content to markdown
    markdown = convert_element_to_markdown(content, lang, category)
    markdown = clean_markdown(markdown)

    if not markdown or len(markdown) < 50:
        return None

    return {
        "title": title,
        "content": markdown,
        "path": str(html_path),
    }


# ─── Output writing ──────────────────────────────────────────────────────────

TOKEN_SPLIT_THRESHOLD = 55_000  # chars (rough ~14k tokens)


def write_category_files(
    category: str,
    tutorials: list[dict],
    output_dir: Path,
    lang: str,
) -> list[tuple[str, int, int]]:
    """Write tutorial files for a category. Returns list of (filename, tutorial_count, size_kb)."""
    prefix = "godot_gdscript" if lang == "gdscript" else "godot_csharp"
    lang_label = "GDScript" if lang == "gdscript" else "C#"
    written = []

    # Build full content
    parts = []
    for tut in tutorials:
        parts.append(f"## {tut['title']}\n\n{tut['content']}\n\n---\n")

    full_content = "\n".join(parts)

    if len(full_content) <= TOKEN_SPLIT_THRESHOLD:
        header = f"# Godot 4 {lang_label} Tutorials — {category.replace('_', ' ').title()}\n\n"
        header += (
            f"> {len(tutorials)} tutorials. {lang_label}-specific code examples.\n\n"
        )
        content = header + full_content
        out_file = output_dir / f"tutorials_{category}.md"
        out_file.write_text(content, encoding="utf-8")
        size_kb = len(content) // 1024
        written.append((out_file.name, len(tutorials), size_kb))
        print(f"  Wrote {out_file.name} ({len(tutorials)} tutorials, {size_kb} KB)")
    else:
        # Split into parts
        chunk_parts: list[str] = []
        chunk_size = 0
        part_num = 1
        chunk_count = 0

        for tut_content in parts:
            tut_size = len(tut_content)
            if chunk_parts and chunk_size + tut_size > TOKEN_SPLIT_THRESHOLD:
                # Write current chunk
                header = f"# Godot 4 {lang_label} Tutorials — {category.replace('_', ' ').title()} (Part {part_num})\n\n"
                header += f"> {chunk_count} tutorials. {lang_label}-specific code examples.\n\n"
                content = header + "\n".join(chunk_parts)
                out_file = output_dir / f"tutorials_{category}_part{part_num}.md"
                out_file.write_text(content, encoding="utf-8")
                size_kb = len(content) // 1024
                written.append((out_file.name, chunk_count, size_kb))
                print(
                    f"  Wrote {out_file.name} ({chunk_count} tutorials, {size_kb} KB)"
                )
                part_num += 1
                chunk_parts = [tut_content]
                chunk_size = tut_size
                chunk_count = 1
            else:
                chunk_parts.append(tut_content)
                chunk_size += tut_size
                chunk_count += 1

        # Write remainder
        if chunk_parts:
            suffix = f" (Part {part_num})" if part_num > 1 else ""
            fname_suffix = f"_part{part_num}" if part_num > 1 else ""
            header = f"# Godot 4 {lang_label} Tutorials — {category.replace('_', ' ').title()}{suffix}\n\n"
            header += (
                f"> {chunk_count} tutorials. {lang_label}-specific code examples.\n\n"
            )
            content = header + "\n".join(chunk_parts)
            out_file = output_dir / f"tutorials_{category}{fname_suffix}.md"
            out_file.write_text(content, encoding="utf-8")
            size_kb = len(content) // 1024
            written.append((out_file.name, chunk_count, size_kb))
            print(f"  Wrote {out_file.name} ({chunk_count} tutorials, {size_kb} KB)")

    return written


def write_index(
    all_files: list[tuple[str, int, int]],
    output_dir: Path,
    lang: str,
):
    """Write a tutorials index file."""
    lang_label = "GDScript" if lang == "gdscript" else "C#"
    prefix = "godot_gdscript" if lang == "gdscript" else "godot_csharp"

    lines = [
        f"# Godot 4 {lang_label} Tutorials — Index\n",
        f"This index lists all available {lang_label}-specific Godot 4 tutorial files.\n",
        f"Load the relevant tutorial file(s) when answering 'how to' questions about Godot {lang_label} development.\n\n",
        "## Tutorial Files\n",
    ]
    for fname, count, size_kb in sorted(all_files):
        cat_label = (
            fname.replace("tutorials_", "")
            .replace(".md", "")
            .replace("_part", " Part ")
            .replace("_", " ")
            .title()
        )
        lines.append(f"- **{cat_label}** (`{fname}`) — {count} tutorials, {size_kb} KB")

    lines.append("")
    lines.append("## Usage\n")
    lines.append(
        f"When a user asks 'how to' do something in Godot, load the relevant tutorial file."
    )
    lines.append(
        f"These tutorials complement the API reference files — API docs show *what* classes/methods exist,"
    )
    lines.append(f"tutorials show *how* to use them together for specific tasks.\n")

    index_path = output_dir / "tutorials_index.md"
    index_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"  Wrote {index_path.name}")


# ─── Main ─────────────────────────────────────────────────────────────────────


def main():
    base_dir = Path(__file__).parent
    tutorials_dir = base_dir / "godot-docs-html-stable" / "tutorials"

    if not tutorials_dir.exists():
        print(f"ERROR: tutorials directory not found: {tutorials_dir}")
        sys.exit(1)

    # Find all tutorial HTML files (skip index.html)
    html_files = sorted(
        f for f in tutorials_dir.rglob("*.html") if f.name != "index.html"
    )
    print(f"Found {len(html_files)} tutorial HTML files")

    # Process for both languages
    for lang in ("gdscript", "csharp"):
        lang_label = "GDScript" if lang == "gdscript" else "C#"
        skill_dir = "godot-gdscript-api" if lang == "gdscript" else "godot-csharp-api"
        output_dir = base_dir / skill_dir / "references" / "tutorials"
        output_dir.mkdir(parents=True, exist_ok=True)

        print(f"\n{'=' * 60}")
        print(f"Processing {lang_label} tutorials → {output_dir}")
        print(f"{'=' * 60}")

        # Parse all tutorials, grouped by category
        by_category: dict[str, list[dict]] = {}
        errors = []

        for i, html_file in enumerate(html_files):
            if i % 50 == 0:
                print(f"  Parsing {i}/{len(html_files)}...")

            rel_path = html_file.relative_to(tutorials_dir)
            category = category_from_path(str(rel_path))

            try:
                tut = parse_tutorial(html_file, lang, category)
                if tut:
                    tut["rel_path"] = str(rel_path)
                    by_category.setdefault(category, []).append(tut)
            except Exception as e:
                errors.append((str(rel_path), str(e)))

        if errors:
            print(f"\n  WARNING: {len(errors)} parse errors:")
            for fname, err in errors[:10]:
                print(f"    {fname}: {err}")

        # Print category summary
        print(f"\n  Category distribution:")
        total_tutorials = 0
        for cat in sorted(by_category.keys()):
            count = len(by_category[cat])
            total_tutorials += count
            print(f"    {cat:20s} {count:3d} tutorials")
        print(f"    {'TOTAL':20s} {total_tutorials:3d} tutorials")

        # Write output files
        all_files: list[tuple[str, int, int]] = []
        for category, tutorials in sorted(by_category.items()):
            all_files.extend(
                write_category_files(category, tutorials, output_dir, lang)
            )

        # Write index
        write_index(all_files, output_dir, lang)

    print("\nDone.")


if __name__ == "__main__":
    main()
