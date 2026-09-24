#!/usr/bin/env python3
"""原创 VSCode 主题配色生成脚本。"""

import json, os

THEMES_DIR = os.path.join(os.path.dirname(__file__), "themes")
os.makedirs(THEMES_DIR, exist_ok=True)

# ============================================================
# 原创主题定义
# 每个主题包含: name, type, bg, fg, accent, 以及语义色
# 语义色: comment, string, number, keyword, function, type,
#          variable, param, property, constant, tag, attr,
#          punct, operator, decorator, link, error, added,
#          deleted, modified
# ============================================================

ORIGINAL_THEMES = [
    # ----------------------------------------------------------
    # 1. Abyss Blue - 深海蓝调
    # ----------------------------------------------------------
    {
        "key": "abyss-blue",
        "label": "Abyss Blue",
        "type": "dark",
        "bg": "#0B1929", "bg_alt": "#081421", "bg_panel": "#0E1B2E",
        "fg": "#B0C4DE", "fg_dim": "#5A7A9A", "fg_bright": "#D0E0F0",
        "accent": "#4FC3F7", "accent2": "#26C6DA",
        "border": "#1A2F45", "selection": "#1A3A5C",
        "semantic": {
            "comment": "#3A5A7A", "string": "#7EEDAF", "number": "#FFB74D",
            "keyword": "#5C9CCF", "function": "#4FC3F7", "type": "#26C6DA",
            "variable": "#B0C4DE", "param": "#FFB74D", "property": "#80DEEA",
            "constant": "#FFB74D", "tag": "#5C9CCF", "attr": "#7EEDAF",
            "punct": "#5A7A9A", "operator": "#5C9CCF", "decorator": "#26C6DA",
            "link": "#4FC3F7", "error": "#FF6B6B", "added": "#7EEDAF",
            "deleted": "#FF6B6B", "modified": "#FFB74D",
        }
    },
    # ----------------------------------------------------------
    # 2. Twilight Bloom - 暮光紫粉
    # ----------------------------------------------------------
    {
        "key": "twilight-bloom",
        "label": "Twilight Bloom",
        "type": "dark",
        "bg": "#1E1428", "bg_alt": "#170F1F", "bg_panel": "#241830",
        "fg": "#C8B8D8", "fg_dim": "#6A5A7A", "fg_bright": "#E8D8F0",
        "accent": "#C77DFF", "accent2": "#E0AAFF",
        "border": "#332040", "selection": "#3D2850",
        "semantic": {
            "comment": "#5A4A6A", "string": "#A8E6CF", "number": "#FFD3B6",
            "keyword": "#C77DFF", "function": "#E0AAFF", "type": "#B388EB",
            "variable": "#C8B8D8", "param": "#FFD3B6", "property": "#D8A0E0",
            "constant": "#FFD3B6", "tag": "#C77DFF", "attr": "#A8E6CF",
            "punct": "#6A5A7A", "operator": "#C77DFF", "decorator": "#B388EB",
            "link": "#E0AAFF", "error": "#FF8FA3", "added": "#A8E6CF",
            "deleted": "#FF8FA3", "modified": "#FFD3B6",
        }
    },
    # ----------------------------------------------------------
    # 3. Aurora Glow - 极光绿
    # ----------------------------------------------------------
    {
        "key": "aurora-glow",
        "label": "Aurora Glow",
        "type": "dark",
        "bg": "#0A1F1C", "bg_alt": "#061613", "bg_panel": "#0D2622",
        "fg": "#A8D8C8", "fg_dim": "#4A7A6A", "fg_bright": "#C8F0E0",
        "accent": "#00E676", "accent2": "#64FFDA",
        "border": "#143028", "selection": "#1A3D34",
        "semantic": {
            "comment": "#3A6A5A", "string": "#FFF59D", "number": "#FFAB91",
            "keyword": "#00E676", "function": "#64FFDA", "type": "#4DB6AC",
            "variable": "#A8D8C8", "param": "#FFAB91", "property": "#80CBC4",
            "constant": "#FFAB91", "tag": "#00E676", "attr": "#FFF59D",
            "punct": "#4A7A6A", "operator": "#00E676", "decorator": "#4DB6AC",
            "link": "#64FFDA", "error": "#FF5252", "added": "#69F0AE",
            "deleted": "#FF5252", "modified": "#FFF59D",
        }
    },
    # ----------------------------------------------------------
    # 4. Desert Sand - 沙漠暖棕
    # ----------------------------------------------------------
    {
        "key": "desert-sand",
        "label": "Desert Sand",
        "type": "dark",
        "bg": "#2B2018", "bg_alt": "#221A14", "bg_panel": "#33261C",
        "fg": "#D4C4A8", "fg_dim": "#7A6A50", "fg_bright": "#EDE0C8",
        "accent": "#E8A87C", "accent2": "#C38D5E",
        "border": "#3D3020", "selection": "#4A3828",
        "semantic": {
            "comment": "#6A5A40", "string": "#A8C090", "number": "#E8A87C",
            "keyword": "#C38D5E", "function": "#E8A87C", "type": "#D4A574",
            "variable": "#D4C4A8", "param": "#F0C896", "property": "#C0A880",
            "constant": "#E8A87C", "tag": "#C38D5E", "attr": "#A8C090",
            "punct": "#7A6A50", "operator": "#C38D5E", "decorator": "#D4A574",
            "link": "#E8A87C", "error": "#D4644A", "added": "#A8C090",
            "deleted": "#D4644A", "modified": "#F0C896",
        }
    },
    # ----------------------------------------------------------
    # 5. Mint Fresh - 薄荷青
    # ----------------------------------------------------------
    {
        "key": "mint-fresh",
        "label": "Mint Fresh",
        "type": "light",
        "bg": "#F0F7F4", "bg_alt": "#E4F0EA", "bg_panel": "#E8F5EF",
        "fg": "#2D4A3E", "fg_dim": "#7A9A8A", "fg_bright": "#1A3328",
        "accent": "#00A86B", "accent2": "#20B2AA",
        "border": "#C0D8CC", "selection": "#C8E6D5",
        "semantic": {
            "comment": "#8AAA9A", "string": "#5A8A3A", "number": "#C06030",
            "keyword": "#00A86B", "function": "#00805A", "type": "#207060",
            "variable": "#2D4A3E", "param": "#C06030", "property": "#3A7A5A",
            "constant": "#C06030", "tag": "#00A86B", "attr": "#5A8A3A",
            "punct": "#6A8A7A", "operator": "#00A86B", "decorator": "#207060",
            "link": "#00805A", "error": "#C43030", "added": "#5A8A3A",
            "deleted": "#C43030", "modified": "#C06030",
        }
    },
    # ----------------------------------------------------------
    # 6. Lava Flow - 熔岩橙红
    # ----------------------------------------------------------
    {
        "key": "lava-flow",
        "label": "Lava Flow",
        "type": "dark",
        "bg": "#1F0E0A", "bg_alt": "#180A06", "bg_panel": "#281410",
        "fg": "#E8C8B8", "fg_dim": "#7A5040", "fg_bright": "#F5E0D0",
        "accent": "#FF6B35", "accent2": "#FF9F1C",
        "border": "#3D1E14", "selection": "#4A2818",
        "semantic": {
            "comment": "#6A4030", "string": "#FFD23F", "number": "#FF9F1C",
            "keyword": "#FF6B35", "function": "#FF9F1C", "type": "#F0A060",
            "variable": "#E8C8B8", "param": "#FFB347", "property": "#E0A080",
            "constant": "#FF9F1C", "tag": "#FF6B35", "attr": "#FFD23F",
            "punct": "#7A5040", "operator": "#FF6B35", "decorator": "#F0A060",
            "link": "#FF9F1C", "error": "#E63946", "added": "#FFD23F",
            "deleted": "#E63946", "modified": "#FFB347",
        }
    },
    # ----------------------------------------------------------
    # 7. Sakura Night - 樱花夜
    # ----------------------------------------------------------
    {
        "key": "sakura-night",
        "label": "Sakura Night",
        "type": "dark",
        "bg": "#1A1014", "bg_alt": "#130C10", "bg_panel": "#221820",
        "fg": "#E0C0CC", "fg_dim": "#7A5A66", "fg_bright": "#F0D8E0",
        "accent": "#FF6B9D", "accent2": "#FFB3C6",
        "border": "#332028", "selection": "#3D2832",
        "semantic": {
            "comment": "#5A4048", "string": "#C8F0D0", "number": "#FFC8A0",
            "keyword": "#FF6B9D", "function": "#FFB3C6", "type": "#E89090",
            "variable": "#E0C0CC", "param": "#FFC8A0", "property": "#D8A0B0",
            "constant": "#FFC8A0", "tag": "#FF6B9D", "attr": "#C8F0D0",
            "punct": "#7A5A66", "operator": "#FF6B9D", "decorator": "#E89090",
            "link": "#FFB3C6", "error": "#FF4757", "added": "#C8F0D0",
            "deleted": "#FF4757", "modified": "#FFC8A0",
        }
    },
    # ----------------------------------------------------------
    # 8. Steel Blue - 钢铁蓝
    # ----------------------------------------------------------
    {
        "key": "steel-blue",
        "label": "Steel Blue",
        "type": "dark",
        "bg": "#1C232E", "bg_alt": "#141A22", "bg_panel": "#232B38",
        "fg": "#B0BEC5", "fg_dim": "#546E7A", "fg_bright": "#CFD8DC",
        "accent": "#4A90D9", "accent2": "#62B5E5",
        "border": "#2E3B47", "selection": "#37474F",
        "semantic": {
            "comment": "#546E7A", "string": "#88C0A0", "number": "#E0A060",
            "keyword": "#4A90D9", "function": "#62B5E5", "type": "#7EC0E5",
            "variable": "#B0BEC5", "param": "#E0A060", "property": "#90A4AE",
            "constant": "#E0A060", "tag": "#4A90D9", "attr": "#88C0A0",
            "punct": "#607D8B", "operator": "#4A90D9", "decorator": "#7EC0E5",
            "link": "#62B5E5", "error": "#EF5350", "added": "#88C0A0",
            "deleted": "#EF5350", "modified": "#E0A060",
        }
    },
]


def hex_with_alpha(hex_color, alpha_hex):
    """给 hex 色加 alpha 通道，如 #4FC3F7 + 80 = #4FC3F780"""
    return hex_color + alpha_hex


def build_colors(t):
    """构建 UI colors 字典"""
    s = t["semantic"]
    is_dark = t["type"] == "dark"
    bg = t["bg"]
    bg_alt = t["bg_alt"]
    bg_panel = t["bg_panel"]
    fg = t["fg"]
    fg_dim = t["fg_dim"]
    fg_bright = t["fg_bright"]
    accent = t["accent"]
    accent2 = t["accent2"]
    border = t["border"]
    selection = t["selection"]

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
        "widget.shadow": "#00000060" if is_dark else "#00000020",
    }


def build_token_colors(t):
    """构建 tokenColors 列表"""
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


# ============================================================
# 生成所有主题
# ============================================================
generated = []
for t in ORIGINAL_THEMES:
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
    generated.append(t)
    print(f"  + {t['key']}.json  ({t['label']}, {t['type']})")

print(f"\n共生成 {len(generated)} 个原创主题")
