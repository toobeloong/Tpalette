# TPalette

> A curated collection of 12 VSCode themes — one pack, all the vibes.

TPalette 是一个 VSCode 主题合集插件，精选 12 款高质量配色主题，从莫兰迪柔和到赛博霓虹，从经典深色到清新浅色，一站式满足不同场景的视觉偏好。

## 主题预览

| # | 主题 | 类型 | 风格 | 背景 | 强调色 |
|---|------|------|------|------|--------|
| 1 | **Morandi Soft Dark** | 深色 | 莫兰迪柔和 | `#2B2D31` | `#8B9DA4` |
| 2 | **Morandi Soft Light** | 浅色 | 莫兰迪柔和 | `#F5F3F0` | `#8A9590` |
| 3 | **Dracula Official** | 深色 | 经典紫调 | `#282A36` | `#FF79C6` |
| 4 | **Tokyo Night** | 深色 | 蓝紫夜色 | `#1A1B26` | `#7AA2F7` |
| 5 | **Catppuccin Mocha** | 深色 | 柔和暖色 | `#1E1E2E` | `#89B4FA` |
| 6 | **Nord** | 深色 | 北极冷蓝 | `#2E3440` | `#88C0D0` |
| 7 | **Solarized Dark** | 深色 | 经典护眼 | `#002B36` | `#268BD2` |
| 8 | **Gruvbox Dark** | 深色 | 复古暖橙 | `#282828` | `#FABD2F` |
| 9 | **Synthwave 84** | 深色 | 霓虹复古 | `#262335` | `#FF7EDB` |
| 10 | **Everforest Dark** | 深色 | 森林绿调 | `#2D353B` | `#A7C080` |
| 11 | **GitHub Dark** | 深色 | 简洁官方 | `#0D1117` | `#58A6FF` |
| 12 | **One Dark Pro** | 深色 | 经典社区 | `#282C34` | `#528BFF` |

每个主题包含 **80+ UI 颜色** + **30+ 语法高亮规则**，覆盖编辑器、侧边栏、标签页、状态栏、终端、Git 装饰等全部区域。

## 安装

### 从 Marketplace 安装

在 VSCode 扩展搜索 `TPalette`，或命令行：

```bash
code --install-extension tpalette
```

### 从 .vsix 安装

```bash
code --install-extension tpalette-1.1.0.vsix
```

## 使用

1. `Cmd+K Cmd+T`（macOS）/ `Ctrl+K Ctrl+T`（Windows）打开主题选择器
2. 选择任意一款主题即可

## 如何添加自定义主题

1. 在 `themes/` 目录下新建 JSON 文件，如 `my-theme.json`
2. 在 `package.json` 的 `contributes.themes` 数组中添加：

```json
{
  "label": "My Custom Theme",
  "uiTheme": "vs-dark",
  "path": "./themes/my-theme.json"
}
```

3. 重新加载 VSCode

### uiTheme 可选值
- `vs-dark`: 深色主题
- `vs`: 浅色主题
- `hc-black`: 高对比度深色
- `hc-light`: 高对比度浅色

### 主题 JSON 结构

```json
{
  "name": "主题名",
  "type": "dark|light",
  "colors": {
    "editor.background": "#hex",
    "editor.foreground": "#hex"
  },
  "tokenColors": [
    {
      "name": "语法元素名",
      "scope": ["scope.name"],
      "settings": {
        "foreground": "#hex",
        "fontStyle": "bold italic underline"
      }
    }
  ]
}
```

### 常用 scope

| scope | 对应语法 |
|-------|---------|
| `comment` | 注释 |
| `string` | 字符串 |
| `keyword` | 关键字 |
| `entity.name.function` | 函数名 |
| `entity.name.type` | 类/类型名 |
| `variable` | 变量 |
| `constant.numeric` | 数字 |
| `entity.name.tag` | HTML 标签 |
| `entity.other.attribute-name` | 属性名 |

## 项目结构

```
tpalette/
├── package.json              # 插件清单（12 个主题注册）
├── icon.png                  # 插件图标
├── LICENSE
├── .vscodeignore
├── generate_themes.py        # 主题生成脚本
├── themes/
│   ├── morandi-dark.json     # 莫兰迪深色
│   ├── morandi-light.json    # 莫兰迪浅色
│   ├── dracula.json          # Dracula
│   ├── tokyo-night.json      # Tokyo Night
│   ├── catppuccin-mocha.json # Catppuccin Mocha
│   ├── nord.json             # Nord
│   ├── solarized-dark.json   # Solarized Dark
│   ├── gruvbox-dark.json     # Gruvbox Dark
│   ├── synthwave-84.json     # Synthwave 84
│   ├── everforest-dark.json  # Everforest Dark
│   ├── github-dark.json      # GitHub Dark
│   └── one-dark-pro.json     # One Dark Pro
└── README.md
```

## 打包发布

```bash
# 打包 .vsix
npx @vscode/vsce package

# 发布到 Marketplace
npx @vscode/vsce publish
```

## License

MIT
