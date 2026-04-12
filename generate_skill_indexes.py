#!/usr/bin/env python3
"""Generate searchable keyword indexes and section-level TOCs for Godot skill files.

Produces two files per skill:
  1. references/KEYWORD_INDEX.md  — maps specific terms to files where they appear
  2. references/tutorials/tutorials_index.md  — enhanced with per-file section headers

Run from the repo root:
    python generate_skill_indexes.py
"""

import os
import re
from pathlib import Path
from collections import defaultdict

# ---------- CONFIG ----------

SKILLS = [
    {
        "name": "GDScript",
        "dir": "godot-gdscript-api",
        "prefix": "godot_gdscript",
        "lang_terms": [
            # GDScript annotations
            "@icon", "@tool", "@export", "@export_range", "@export_enum",
            "@export_file", "@export_dir", "@export_multiline", "@export_node_path",
            "@export_flags", "@export_color_no_alpha", "@export_placeholder",
            "@export_exp_easing", "@export_group", "@export_subgroup",
            "@export_category", "@export_flags_2d_physics", "@export_flags_3d_physics",
            "@export_flags_2d_render", "@export_flags_3d_render",
            "@export_flags_2d_navigation", "@export_flags_3d_navigation",
            "@export_storage", "@export_custom", "@export_tool_button",
            "@onready", "@static_unload", "@warning_ignore", "@rpc",
            # GDScript keywords / patterns (only distinctive ones, not ubiquitous like var/func/const)
            "class_name", "preload", "signal ", "enum ",
            "match ", "await ", "super(", "setget",
            # Built-in functions
            "load(", "preload(", "push_error(", "push_warning(",
            "typeof(",
            # Common API patterns
            "add_child", "remove_child", "queue_free", "get_node",
            "get_tree", "instantiate", "emit_signal", ".emit(",
            ".connect(", "ResourceLoader", "ResourceSaver",
            "EditorPlugin", "EditorScript",
            "add_import_plugin", "add_inspector_plugin",
            "add_node_3d_gizmo_plugin", "add_autoload_singleton",
            "plugin.cfg", "addons/",
            # Node lifecycle
            "_ready", "_process", "_physics_process", "_enter_tree",
            "_exit_tree", "_input", "_unhandled_input", "_notification",
            "_init",
            # Common types searched
            "PackedScene", "PackedArray", "Dictionary", "Array",
            "StringName", "NodePath", "Callable", "Signal",
            "Tween", "Timer", "AnimationPlayer", "AnimationTree",
            "CharacterBody2D", "CharacterBody3D", "RigidBody2D", "RigidBody3D",
            "Area2D", "Area3D", "RayCast2D", "RayCast3D",
            "TileMap", "TileSet", "NavigationAgent",
            # Editor classes
            "EditorInspectorPlugin", "EditorProperty", "EditorNode3DGizmo",
            "EditorImportPlugin", "EditorExportPlugin",
            "VisualShaderNodeCustom",
        ],
    },
    {
        "name": "C#",
        "dir": "godot-csharp-api",
        "prefix": "godot_csharp",
        "lang_terms": [
            # C# attributes
            "[Export]", "[ExportGroup]", "[ExportSubgroup]", "[ExportCategory]",
            "[Tool]", "[GlobalClass]", "[Signal]", "[ExportToolButton]",
            # C# patterns
            "partial class", "GodotObject", "SceneTree",
            "GetNode", "AddChild", "RemoveChild", "QueueFree",
            "EmitSignal", "Connect(", "ResourceLoader", "ResourceSaver",
            "GD.Print", "GD.PushError", "GD.PushWarning",
            "PackedScene", "Instantiate",
            "EditorPlugin", "EditorScript",
            "_Ready", "_Process", "_PhysicsProcess", "_EnterTree",
            "_ExitTree", "_Input", "_UnhandledInput",
            "Tween", "Timer", "AnimationPlayer", "AnimationTree",
            "CharacterBody2D", "CharacterBody3D",
            "EditorInspectorPlugin", "EditorProperty",
            "VisualShaderNodeCustom",
            "plugin.cfg", "addons/",
        ],
    },
]


def find_files(base_dir: Path):
    """Return (api_files, tutorial_files) as lists of Path objects."""
    refs = base_dir / "references"
    api_files = sorted(f for f in refs.glob("*.md") if f.name != "KEYWORD_INDEX.md")
    tut_dir = refs / "tutorials"
    tutorial_files = sorted(tut_dir.glob("tutorials_*.md")) if tut_dir.exists() else []
    return api_files, tutorial_files


def extract_sections(filepath: Path) -> list[str]:
    """Extract H2 (##) section headers from a markdown file."""
    sections = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("## "):
                title = line[3:].strip()
                # Skip doc-comment artifacts that leaked into H2
                if len(title) < 120 and not title.startswith("@") and not title.startswith("["):
                    sections.append(title)
    return sections


def build_keyword_index(all_files: list[Path], terms: list[str], base_dir: Path) -> dict:
    """Map each term to the files containing it."""
    index = defaultdict(set)
    file_contents = {}

    for fp in all_files:
        try:
            file_contents[fp] = fp.read_text(encoding="utf-8")
        except Exception:
            continue

    for term in terms:
        for fp, content in file_contents.items():
            if term in content:
                rel = fp.relative_to(base_dir / "references")
                index[term].add(str(rel))

    return index


def write_keyword_index(index: dict, output_path: Path, skill_name: str, max_files: int = 30):
    """Write the keyword index as a markdown file. Skip terms matching > max_files files."""
    # Filter out overly-common terms
    index = {k: v for k, v in index.items() if len(v) <= max_files}

    lines = [
        f"# {skill_name} Keyword Index\n",
        "",
        "Quick-lookup index mapping specific terms, annotations, and patterns to the files that contain them.",
        "Use this to find the right file(s) to load when searching for a specific term.\n",
        "",
    ]

    # Group terms by category
    categories = {
        "Annotations / Decorators": [t for t in index if t.startswith("@") or t.startswith("[")],
        "Language Keywords": [t for t in index if t in {
            "class_name", "extends", "preload", "signal", "enum", "match",
            "await", "super", "is", "as", "in", "setget", "set:", "get:",
            "var", "const", "func", "partial class", "GodotObject",
        }],
        "Lifecycle Methods": [t for t in index if t.startswith("_") and "(" not in t],
        "Common API Calls": [],  # catch-all for the rest
    }

    categorized = set()
    for terms in categories.values():
        categorized.update(terms)
    categories["Common API Calls"] = [t for t in index if t not in categorized]

    for cat_name, terms in categories.items():
        if not terms:
            continue
        lines.append(f"## {cat_name}\n")
        lines.append("")
        lines.append("| Term | Files |")
        lines.append("|------|-------|")
        for term in sorted(terms, key=str.lower):
            files = sorted(index[term])
            files_str = ", ".join(f"`{f}`" for f in files)
            escaped_term = term.replace("|", "\\|")
            lines.append(f"| `{escaped_term}` | {files_str} |")
        lines.append("")

    output_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"  Written: {output_path} ({len(index)} terms)")


def write_enhanced_tutorial_index(tutorial_files: list[Path], output_path: Path, skill_name: str):
    """Write tutorials_index.md with per-file section headers."""
    lines = [
        f"# {skill_name} Tutorials — Section Index\n",
        "",
        "This index lists all tutorial files with their section headers.",
        "Use this to locate specific topics without loading full files.\n",
        "",
    ]

    for fp in tutorial_files:
        if fp.name == "tutorials_index.md":
            continue
        sections = extract_sections(fp)
        size_kb = fp.stat().st_size // 1024
        lines.append(f"## `{fp.name}` ({size_kb} KB)\n")
        if sections:
            for s in sections:
                lines.append(f"- {s}")
        else:
            lines.append("- *(no major sections)*")
        lines.append("")

    output_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"  Written: {output_path} ({len(tutorial_files)} files indexed)")


def main():
    repo_root = Path(__file__).parent

    for skill in SKILLS:
        base_dir = repo_root / skill["dir"]
        if not base_dir.exists():
            print(f"Skipping {skill['name']}: {base_dir} not found")
            continue

        print(f"\n=== {skill['name']} Skill ===")

        api_files, tutorial_files = find_files(base_dir)
        all_files = api_files + tutorial_files

        # 1. Keyword index
        index = build_keyword_index(all_files, skill["lang_terms"], base_dir)
        kw_path = base_dir / "references" / "KEYWORD_INDEX.md"
        write_keyword_index(index, kw_path, f"Godot 4 {skill['name']}")

        # 2. Enhanced tutorial index
        tut_dir = base_dir / "references" / "tutorials"
        if tut_dir.exists():
            tut_index_path = tut_dir / "tutorials_index.md"
            write_enhanced_tutorial_index(tutorial_files, tut_index_path, f"Godot 4 {skill['name']}")


if __name__ == "__main__":
    main()
