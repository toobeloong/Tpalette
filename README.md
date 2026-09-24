# Morandi Soft Theme

莫兰迪柔和配色 VSCode 主题插件。低饱和度高级感，护眼舒适。

## 安装

### 方式一：本地调试安装

```bash
cd ~/project/vscode-theme-morandi
# 在 VSCode 中按 F5 启动 Extension Development Host
# 或复制到 VSCode 扩展目录：
# macOS: ~/.vscode/extensions/
cp -r . ~/.vscode/extensions/morandi-theme-1.0.0
```

### 方式二：打包成 .vsix 安装

```bash
npm install -g @vscode/vsce
cd ~/project/vscode-theme-morandi
vsce package
# 生成的 .vsix 文件可在 VSCode 中安装
code --install-extension morandi-theme-1.0.0.vsix
code --install-extension morandi-theme-1.0.0.vsix
```

## 使用

1. `Cmd+K Cmd+T` 打开主题选择器
2. 选择 **Morandi Soft Dark** 或 **Morandi Soft Light**

## 配色预览

### 莫兰迪色板

| 色块 | 色值 | 用途 |
|------|------|------|
| 🟫 #2B2D31 | 深灰背景 | 编辑器背景 |
| 🟫 #1F2123 | 深灰黑 | 活动栏/状态栏 |
| 🟤 #A89B8E | 暖灰 | 关键字 |
| 🟢 #A8B89A | 灰绿 | 字符串 |
| 🔵 #8B9DA4 | 灰蓝 | 函数/链接 |
| 🟡 #B8A88E | 灰金 | 类/类型 |
| 🔴 #B08888 | 灰粉 | 错误/删除 |
| ⚪ #C4C7C5 | 浅灰 | 默认文字 |

### 深色主题 (Morandi Soft Dark)
- 背景: #2B2D31 (深灰)
- 文字: #C4C7C5 (浅灰)
- 强调: #8B9DA4 (灰蓝)

### 浅色主题 (Morandi Soft Light)
- 背景: #F5F3F0 (暖白)
- 文字: #4A4D4B (深灰)
- 强调: #8A9590 (灰绿)

## 如何添加新主题

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

## 主题 JSON 结构

```json
{
  "name": "主题名",
  "type": "dark|light",
  "colors": {
    "editor.background": "#hex",
    "editor.foreground": "#hex"
    // ... UI 颜色
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
vscode-theme-morandi/
├── package.json          # 插件清单
├── icon.png              # 插件图标
├── themes/
│   ├── morandi-dark.json # 深色主题
│   └── morandi-light.json# 浅色主题
└── README.md
```

## License

MIT
