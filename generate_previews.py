#!/usr/bin/env python3
"""为所有主题生成配色预览图（PNG），输出到 previews/ 目录。"""

import json, os, math
from PIL import Image, ImageDraw, ImageFont

THEMES_DIR = os.path.join(os.path.dirname(__file__), "themes")
PREVIEWS_DIR = os.path.join(os.path.dirname(__file__), "previews")
os.makedirs(PREVIEWS_DIR, exist_ok=True)

# 尝试加载等宽字体
def load_font(size):
    paths = [
        "/System/Library/Fonts/Menlo.ttc",
        "/System/Library/Fonts/Monaco.ttf",
        "/System/Library/Fonts/Courier.ttc",
        "/System/Library/Fonts/Helvetica.ttc",
    ]
    for p in paths:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except:
                pass
    return ImageFont.load_default()

FONT_CODE = load_font(14)
FONT_LABEL = load_font(13)
FONT_TITLE = load_font(18)
FONT_SMALL = load_font(11)

# 模拟代码片段
CODE_LINES = [
    ("// Cyberpunk Theme Preview", "comment"),
    ("import { neon } from 'future'", "keyword"),
    ("", ""),
    ("export class City {", "type"),
    ("  name: string = 'Night City'", "property"),
    ("  population = 1_207_800", "number"),
    ("", ""),
    ("  async explore(district: string) {", "function"),
    ("    const lights = await scan(district)", "variable"),
    ("    return lights.filter(l => l.on)", "keyword"),
    ("  }", "punct"),
    ("}", "punct"),
]

# 语义色 key -> 显示标签
SEMANTIC_LABELS = [
    ("keyword", "Keyword"), ("function", "Function"), ("type", "Type"),
    ("string", "String"), ("number", "Number"), ("comment", "Comment"),
    ("variable", "Variable"), ("param", "Param"), ("property", "Property"),
    ("constant", "Constant"), ("tag", "Tag"), ("attr", "Attribute"),
    ("operator", "Operator"), ("decorator", "Decorator"), ("link", "Link"),
    ("error", "Error"), ("added", "Added"), ("deleted", "Deleted"),
    ("modified", "Modified"), ("punct", "Punctuation"),
]

# 读取所有主题
themes = []
for f in sorted(os.listdir(THEMES_DIR)):
    if not f.endswith(".json"):
        continue
    with open(os.path.join(THEMES_DIR, f)) as fh:
        data = json.load(fh)
    # 提取语义色
    semantic = {}
    for tc in data.get("tokenColors", []):
        name = tc.get("name", "")
        fg = tc.get("settings", {}).get("foreground", "")
        if not fg:
            continue
        for key, label in SEMANTIC_LABELS:
            if label.lower() in name.lower() and key not in semantic:
                semantic[key] = fg
    # 从 colors 提取背景和前景
    colors = data.get("colors", {})
    themes.append({
        "file": f,
        "name": data.get("name", f),
        "type": data.get("type", "dark"),
        "bg": colors.get("editor.background", "#1e1e1e"),
        "fg": colors.get("editor.foreground", "#d4d4d4"),
        "accent": colors.get("tab.activeBorderTop", "#569cd6"),
        "semantic": semantic,
        "colors": colors,
    })

print(f"共 {len(themes)} 个主题")

# ============================================================
# 生成单主题预览图
# ============================================================
def render_theme(theme, cols=4):
    """生成单个主题的预览图"""
    bg = theme["bg"]
    fg = theme["fg"]
    accent = theme["accent"]
    sem = theme["semantic"]
    def sc(key, fallback="#888888"):
        v = sem.get(key, fallback)
        return v if v else fallback

    # 画布尺寸
    W = 800
    # 代码区高度
    code_h = len(CODE_LINES) * 22 + 30
    # 色块区
    n_colors = len(SEMANTIC_LABELS)
    rows = math.ceil(n_colors / cols)
    swatch_h = rows * 28 + 20
    # 标题区
    title_h = 50
    H = title_h + code_h + swatch_h + 20

    img = Image.new("RGB", (W, H), bg)
    draw = ImageDraw.Draw(img)

    # --- 标题区 ---
    draw.text((20, 15), theme["name"], fill=fg, font=FONT_TITLE)
    # 类型标签
    type_label = theme["type"].upper()
    tw = draw.textlength(type_label, font=FONT_SMALL)
    draw.rounded_rectangle([W - tw - 30, 18, W - 10, 34], radius=4, fill=accent)
    draw.text((W - tw - 20, 19), type_label, fill=bg, font=FONT_SMALL)

    # 分割线
    draw.line([(0, title_h), (W, title_h)], fill=sc("punct", "#333333"), width=1)

    # --- 代码区 ---
    y = title_h + 15
    for line_text, role in CODE_LINES:
        if not line_text:
            y += 22
            continue
        # 行号
        line_num = CODE_LINES.index((line_text, role)) + 1
        draw.text((10, y), f"{line_num:>2}", fill=sc("comment", "#666666"), font=FONT_CODE)
        # 代码文本（简单着色）
        color = sc(role, fg)
        draw.text((40, y), line_text, fill=color, font=FONT_CODE)
        y += 22

    # 分割线
    draw.line([(0, title_h + code_h), (W, title_h + code_h)], fill=sc("punct", "#333333"), width=1)

    # --- 色块区 ---
    y = title_h + code_h + 10
    swatch_w = (W - 40) // cols
    for i, (key, label) in enumerate(SEMANTIC_LABELS):
        col = i % cols
        row = i // cols
        x = 20 + col * swatch_w
        yy = y + row * 28
        color = sc(key, "#888888")
        # 色块
        draw.rounded_rectangle([x, yy, x + 16, yy + 16], radius=3, fill=color)
        # 标签
        draw.text((x + 22, yy + 1), label, fill=fg, font=FONT_LABEL)
        # 色值
        draw.text((x + 22, yy + 14), color, fill=theme["colors"].get("descriptionForeground", "#888888"), font=FONT_SMALL)

    return img

# ============================================================
# 生成合集大图（网格布局）
# ============================================================
def render_grid(themes, cols=2):
    """生成所有主题的网格预览大图"""
    # 先生成每个主题的小图
    thumbs = [render_theme(t) for t in themes]
    tw, th = thumbs[0].size
    # 缩小到 60%
    scale = 0.6
    tw_s, th_s = int(tw * scale), int(th * scale)
    thumbs_s = [t.resize((tw_s, th_s), Image.LANCZOS) for t in thumbs]

    rows = math.ceil(len(thumbs) / cols)
    padding = 16
    W = cols * tw_s + (cols + 1) * padding
    H = rows * th_s + (rows + 1) * padding + 60  # +60 for title

    grid = Image.new("RGB", (W, H), "#0A0A0A")
    draw = ImageDraw.Draw(grid)
    draw.text((padding, 20), f"TPalette - {len(themes)} Themes", fill="#E0E0E0", font=FONT_TITLE)

    for i, thumb in enumerate(thumbs_s):
        col = i % cols
        row = i // cols
        x = padding + col * (tw_s + padding)
        y = 60 + padding + row * (th_s + padding)
        grid.paste(thumb, (x, y))

    return grid

# ============================================================
# 生成所有预览图
# ============================================================
for t in themes:
    img = render_theme(t)
    name = t["file"].replace(".json", "")
    path = os.path.join(PREVIEWS_DIR, f"{name}.png")
    img.save(path)
    print(f"  + {name}.png  ({t['name']})")

# 合集大图
grid = render_grid(themes, cols=2)
grid_path = os.path.join(PREVIEWS_DIR, "all-themes.png")
grid.save(grid_path)
print(f"\n  + all-themes.png  (合集预览)")

print(f"\n共生成 {len(themes) + 1} 张预览图 -> previews/")
