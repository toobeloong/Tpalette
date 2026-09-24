#!/usr/bin/env python3
"""赛博朋克风格原创 VSCode 主题生成脚本。"""

import json, os

THEMES_DIR = os.path.join(os.path.dirname(__file__), "themes")
os.makedirs(THEMES_DIR, exist_ok=True)

CYBERPUNK_THEMES = [
    # ----------------------------------------------------------
    # 1. Neon Pulse - 经典霓虹粉青
    # ----------------------------------------------------------
    {
        "key": "neon-pulse",
        "label": "Neon Pulse",
        "type": "dark",
        "bg": "#0A0A12", "bg_alt": "#06060C", "bg_panel": "#0E0E1A",
        "fg": "#E0E0F0", "fg_dim": "#5050A0", "fg_bright": "#F0F0FF",
        "accent": "#FF2D95", "accent2": "#00F0FF",
        "border": "#1A1A2E", "selection": "#2A1A3E",
        "semantic": {
            "comment": "#4A4A7A", "string": "#00FF9F", "number": "#FFB300",
            "keyword": "#FF2D95", "function": "#00F0FF", "type": "#B026FF",
            "variable": "#E0E0F0", "param": "#FFB300", "property": "#00F0FF",
            "constant": "#FFB300", "tag": "#FF2D95", "attr": "#00FF9F",
            "punct": "#5050A0", "operator": "#FF2D95", "decorator": "#B026FF",
            "link": "#00F0FF", "error": "#FF0040", "added": "#00FF9F",
            "deleted": "#FF0040", "modified": "#FFB300",
        }
    },
    # ----------------------------------------------------------
    # 2. Matrix Rain - 黑客帝国绿
    # ----------------------------------------------------------
    {
        "key": "matrix-rain",
        "label": "Matrix Rain",
        "type": "dark",
        "bg": "#000A00", "bg_alt": "#000600", "bg_panel": "#001400",
        "fg": "#00FF41", "fg_dim": "#008F11", "fg_bright": "#39FF14",
        "accent": "#00FF41", "accent2": "#39FF14",
        "border": "#003300", "selection": "#004D00",
        "semantic": {
            "comment": "#005A0E", "string": "#7FFF00", "number": "#FFD700",
            "keyword": "#00FF41", "function": "#39FF14", "type": "#00CC33",
            "variable": "#00FF41", "param": "#FFD700", "property": "#7FFF00",
            "constant": "#FFD700", "tag": "#00FF41", "attr": "#7FFF00",
            "punct": "#008F11", "operator": "#00FF41", "decorator": "#00CC33",
            "link": "#39FF14", "error": "#FF3333", "added": "#7FFF00",
            "deleted": "#FF3333", "modified": "#FFD700",
        }
    },
    # ----------------------------------------------------------
    # 3. Chrome Sunset - 铬金日落（橙紫）
    # ----------------------------------------------------------
    {
        "key": "chrome-sunset",
        "label": "Chrome Sunset",
        "type": "dark",
        "bg": "#0D0221", "bg_alt": "#08011A", "bg_panel": "#150530",
        "fg": "#F0D0FF", "fg_dim": "#6A3A8A", "fg_bright": "#FFE0FF",
        "accent": "#FF6B00", "accent2": "#B026FF",
        "border": "#2A0A45", "selection": "#3D1050",
        "semantic": {
            "comment": "#5A2A7A", "string": "#00E5FF", "number": "#FFD000",
            "keyword": "#FF6B00", "function": "#FF9500", "type": "#B026FF",
            "variable": "#F0D0FF", "param": "#FFD000", "property": "#E070FF",
            "constant": "#FFD000", "tag": "#FF6B00", "attr": "#00E5FF",
            "punct": "#6A3A8A", "operator": "#FF6B00", "decorator": "#B026FF",
            "link": "#FF9500", "error": "#FF1744", "added": "#00E5FF",
            "deleted": "#FF1744", "modified": "#FFD000",
        }
    },
    # ----------------------------------------------------------
    # 4. Electric Violet - 电紫
    # ----------------------------------------------------------
    {
        "key": "electric-violet",
        "label": "Electric Violet",
        "type": "dark",
        "bg": "#0C0C1A", "bg_alt": "#08080F", "bg_panel": "#101025",
        "fg": "#D0D0FF", "fg_dim": "#5050A0", "fg_bright": "#E8E8FF",
        "accent": "#8A2BE2", "accent2": "#BF40FF",
        "border": "#1E1E3A", "selection": "#2A2A50",
        "semantic": {
            "comment": "#4A4A7A", "string": "#00FFC8", "number": "#FFD700",
            "keyword": "#8A2BE2", "function": "#BF40FF", "type": "#9D4EDD",
            "variable": "#D0D0FF", "param": "#FFD700", "property": "#C77DFF",
            "constant": "#FFD700", "tag": "#8A2BE2", "attr": "#00FFC8",
            "punct": "#5050A0", "operator": "#8A2BE2", "decorator": "#9D4EDD",
            "link": "#BF40FF", "error": "#FF0055", "added": "#00FFC8",
            "deleted": "#FF0055", "modified": "#FFD700",
        }
    },
    # ----------------------------------------------------------
    # 5. Hologram - 全息青绿
    # ----------------------------------------------------------
    {
        "key": "hologram",
        "label": "Hologram",
        "type": "dark",
        "bg": "#001011", "bg_alt": "#000A0B", "bg_panel": "#001A1C",
        "fg": "#7FDBFF", "fg_dim": "#2A6A7A", "fg_bright": "#B0F0FF",
        "accent": "#00E5FF", "accent2": "#00FFB0",
        "border": "#003540", "selection": "#004D5C",
        "semantic": {
            "comment": "#1A5A6A", "string": "#FF00FF", "number": "#FFD600",
            "keyword": "#00E5FF", "function": "#00FFB0", "type": "#39CCCC",
            "variable": "#7FDBFF", "param": "#FFD600", "property": "#00FFB0",
            "constant": "#FFD600", "tag": "#00E5FF", "attr": "#FF00FF",
            "punct": "#2A6A7A", "operator": "#00E5FF", "decorator": "#39CCCC",
            "link": "#00FFB0", "error": "#FF4136", "added": "#00FFB0",
            "deleted": "#FF4136", "modified": "#FFD600",
        }
    },
    # ----------------------------------------------------------
    # 6. Blood Moon - 血月红黑
    # ----------------------------------------------------------
    {
        "key": "blood-moon",
        "label": "Blood Moon",
        "type": "dark",
        "bg": "#0A0000", "bg_alt": "#050000", "bg_panel": "#140000",
        "fg": "#FFB0B0", "fg_dim": "#7A2A2A", "fg_bright": "#FFD0D0",
        "accent": "#DC143C", "accent2": "#FF2400",
        "border": "#2A0000", "selection": "#3D0808",
        "semantic": {
            "comment": "#5A1A1A", "string": "#FFD700", "number": "#FF8C00",
            "keyword": "#DC143C", "function": "#FF2400", "type": "#FF6347",
            "variable": "#FFB0B0", "param": "#FF8C00", "property": "#E04050",
            "constant": "#FF8C00", "tag": "#DC143C", "attr": "#FFD700",
            "punct": "#7A2A2A", "operator": "#DC143C", "decorator": "#FF6347",
            "link": "#FF2400", "error": "#FF0000", "added": "#FFD700",
            "deleted": "#FF0000", "modified": "#FF8C00",
        }
    },
]


def build_colors(t):
    s = t["semantic"]
    bg = t["bg"]; bg_alt = t["bg_alt"]; bg_panel = t["bg_panel"]
    fg = t["fg"]; fg_dim = t["fg_dim"]; fg_bright = t["fg_bright"]
    accent = t["accent"]; accent2 = t["accent2"]
    border = t["border"]; selection = t["selection"]

    return {
        "editor.background": bg,
        "editor.foreground": fg,
        "editorLineNumber.foreground": fg_dim,
        "editorLineNumber.activeForeground": accent,
        "editor.selectionBackground": selection,
        "editor.selectionHighlightBackground": selection + "80",
        "editor.findMatchBackground": accent + "80",
        "editor.findMatchHighlightBackground": accent + "40",
        "editorCursor.foreground": fg_bright,
        "editor.lineHighlightBackground": bg_panel,
        "editorIndentGuide.background": border,
        "editorIndentGuide.activeBackground": fg_dim,
        "editorBracketMatch.border": accent + "80",
        "editorGutter.background": bg,
        "editorWidget.background": bg_alt,
        "editorWidget.border": border,
        "editorSuggestWidget.background": bg_alt,
        "editorSuggestWidget.border": border,
        "editorSuggestWidget.selectedBackground": selection,
        "editorHoverWidget.background": bg_alt,
        "editorHoverWidget.border": border,
        "editorGroup.border": border,
        "editorGroupHeader.tabsBackground": bg_alt,
        "tab.activeBackground": bg,
        "tab.activeForeground": fg_bright,
        "tab.inactiveBackground": bg_alt,
        "tab.inactiveForeground": fg_dim,
        "tab.border": border,
        "tab.activeBorderTop": accent,
        "sideBar.background": bg_alt,
        "sideBar.foreground": fg,
        "sideBar.border": border,
        "sideBarTitle.foreground": fg_bright,
        "sideBarSectionHeader.background": bg,
        "list.activeSelectionBackground": selection,
        "list.activeSelectionForeground": fg_bright,
        "list.inactiveSelectionBackground": selection + "80",
        "list.hoverBackground": bg_panel,
        "list.foreground": fg,
        "activityBar.background": bg_alt,
        "activityBar.foreground": fg,
        "activityBar.activeBorder": accent,
        "activityBarBadge.background": accent,
        "activityBarBadge.foreground": bg_alt,
        "statusBar.background": bg_alt,
        "statusBar.foreground": fg,
        "statusBar.debuggingBackground": s["error"],
        "titleBar.activeBackground": bg_alt,
        "titleBar.activeForeground": fg,
        "menu.background": bg_alt,
        "menu.foreground": fg,
        "menu.selectionBackground": selection,
        "menu.separatorBackground": border,
        "button.background": accent,
        "button.foreground": bg_alt,
        "button.hoverBackground": accent2,
        "input.background": bg_alt,
        "input.border": border,
        "input.foreground": fg_bright,
        "input.placeholderForeground": fg_dim,
        "dropdown.background": bg_alt,
        "dropdown.border": border,
        "dropdown.foreground": fg,
        "scrollbarSlider.background": fg_dim + "40",
        "scrollbarSlider.hoverBackground": fg_dim + "60",
        "scrollbarSlider.activeBackground": fg_dim + "80",
        "panel.background": bg_alt,
        "panel.border": border,
        "panelTitle.activeBorder": accent,
        "panelTitle.activeForeground": fg_bright,
        "panelTitle.inactiveForeground": fg_dim,
        "terminal.background": bg,
        "terminal.foreground": fg,
        "terminal.border": border,
        "gitDecoration.addedResourceForeground": s["added"],
        "gitDecoration.modifiedResourceForeground": s["modified"],
        "gitDecoration.deletedResourceForeground": s["deleted"],
        "gitDecoration.untrackedResourceForeground": s["added"],
        "gitDecoration.ignoredResourceForeground": fg_dim,
        "gitDecoration.conflictResourceForeground": s["modified"],
        "badge.background": accent,
        "badge.foreground": bg_alt,
        "progressBar.background": accent,
        "focusBorder": accent + "80",
        "foreground": fg,
        "descriptionForeground": fg_dim,
        "errorForeground": s["error"],
        "icon.foreground": fg_dim,
        "selection.background": selection,
        "textLink.foreground": s["link"],
        "textLink.activeForeground": accent2,
        "widget.shadow": "#00000060",
    }


def build_token_colors(t):
    s = t["semantic"]
    token_defs = [
        ("Comment", ["comment", "punctuation.definition.comment"], s["comment"], "italic"),
        ("String", ["string", "string.quoted"], s["string"], None),
        ("Number", ["constant.numeric", "constant.language"], s["number"], None),
        ("Boolean / Null", ["constant.language.boolean", "constant.language.null"], s["number"], None),
        ("Keyword", ["keyword", "keyword.control", "keyword.operator.new"], s["keyword"], None),
        ("Storage / Modifier", ["storage", "storage.type", "storage.modifier"], s["keyword"], None),
        ("Function", ["entity.name.function", "support.function"], s["function"], None),
        ("Class / Type", ["entity.name.type", "entity.name.class", "support.type", "support.class"], s["type"], None),
        ("Variable", ["variable", "variable.other"], s["variable"], None),
        ("Variable Parameter", ["variable.parameter", "variable.parameter.function"], s["param"], None),
        ("Property", ["variable.other.property", "variable.other.object.property"], s["property"], None),
        ("Constant", ["variable.other.constant", "constant.other"], s["constant"], None),
        ("Tag", ["entity.name.tag", "meta.tag"], s["tag"], None),
        ("Attribute", ["entity.other.attribute-name", "meta.attribute"], s["attr"], None),
        ("Punctuation", ["punctuation", "meta.brace"], s["punct"], None),
        ("Operator", ["keyword.operator", "keyword.operator.logical", "keyword.operator.arithmetic"], s["operator"], None),
        ("Decorator / Annotation", ["meta.decorator", "entity.name.function.decorator", "punctuation.decorator"], s["decorator"], None),
        ("Namespace / Module", ["entity.name.namespace", "entity.name.module"], s["type"], None),
        ("Enum", ["entity.name.enum", "variable.other.enummember"], s["string"], None),
        ("JSON Key", ["meta.object-literal.key", "support.type.property-name.json"], s["property"], None),
        ("CSS Property", ["support.type.property-name.css", "support.type.property-name.scss"], s["property"], None),
        ("CSS Value", ["support.constant.property-value.css", "constant.numeric.css"], s["constant"], None),
        ("HTML Tag Name", ["entity.name.tag.html", "entity.name.tag.xhtml"], s["tag"], None),
        ("Markdown Heading", ["markup.heading", "entity.name.section.markdown"], s["type"], "bold"),
        ("Markdown Bold", ["markup.bold"], s["variable"], "bold"),
        ("Markdown Italic", ["markup.italic"], s["param"], "italic"),
        ("Markdown Link", ["markup.underline.link"], s["link"], None),
        ("Markdown Code", ["markup.raw.code", "markup.fenced_code.block"], s["string"], None),
        ("Regex", ["string.regexp"], s["string"], None),
        ("URL", ["markup.underline.link.http", "markup.underline.link.https"], s["link"], None),
        ("Invalid / Error", ["invalid", "invalid.illegal"], s["error"], "underline"),
        ("Diff Added", ["markup.inserted", "diff.inserted"], s["added"], None),
        ("Diff Deleted", ["markup.deleted", "diff.deleted"], s["deleted"], None),
        ("Diff Modified", ["markup.changed", "diff.changed"], s["modified"], None),
    ]
    token_colors = []
    for name, scope, fg, style in token_defs:
        settings = {"foreground": fg}
        if style:
            settings["fontStyle"] = style
        token_colors.append({"name": name, "scope": scope, "settings": settings})
    return token_colors


for t in CYBERPUNK_THEMES:
    theme_json = {
        "name": t["label"],
        "type": t["type"],
        "semanticHighlighting": True,
        "colors": build_colors(t),
        "tokenColors": build_token_colors(t),
    }
    filepath = os.path.join(THEMES_DIR, f"{t['key']}.json")
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(theme_json, f, indent=2, ensure_ascii=False)
    print(f"  + {t['key']}.json  ({t['label']})")

print(f"\n共生成 {len(CYBERPUNK_THEMES)} 个赛博朋克主题")
