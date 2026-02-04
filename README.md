<div align="center">

# 📁 Tree Generator

**Transform your project structure into beautiful markdown documentation**

[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![No Dependencies](https://img.shields.io/badge/dependencies-0-brightgreen.svg)](https://github.com/Manalilou/tree-generator)

[Features](#-features) • [Quick Start](#-quick-start) • [Examples](#-examples) • [Configuration](#-configuration)

</div>

---

## ✨ Features

- 🌳 **Beautiful visual tree** with 40+ file type icons
- 📦 **Zero dependencies** - pure Python 3.7+
- 🚫 **Smart filtering** via `.treeignore` file  
- ⚡ **Lightning fast** - scans thousands of files instantly
- 🔄 **Cross-platform** - Windows, macOS, Linux

## 🚀 Quick Start

```bash
# Download the script
curl -O https://raw.githubusercontent.com/Manalilou/tree-generator/main/generate_tree.py

# Run it
python generate_tree.py
```

Your `README.md` is now updated with your project structure! 🎉

## 📸 Example

The script generates a README.md with your project structure using emoji icons:

<table>
<tr>
<td width="50%" valign="top">

**Before**
```
my-project/
├── src/
├── tests/
└── ...
```

</td>
<td width="50%" valign="top">

**After**  
*Visual tree with emoji icons*

```
📁 my-project/
│   🐳 Dockerfile
│   📦 package.json
│   📁 src/
│   │   ⚛️ App.tsx
│   │   🎨 styles.css
│   📁 tests/
│   │   🐍 test_main.py
```

</td>
</tr>
</table>

> **Note:** Emoji icons display correctly on GitHub. If you see squares in your terminal, that's normal - the generated README will render properly on GitHub.

## 🎨 Supported Icons

| 🐍 Python | 📜 JavaScript | 📘 TypeScript | ⚛️ React | 🐳 Docker |
|-----------|--------------|---------------|----------|-----------|
| ☕ Java | 🦀 Rust | 🐹 Go | 💎 Ruby | 🌐 HTML |
| 🎨 CSS | 📋 JSON | ⚙️ YAML | 🗄️ SQL | 📝 Markdown |

**40+ file types supported!** See [USAGE.md](USAGE.md) for complete list.

## ⚙️ Configuration

Create a `.treeignore` to exclude files:

```bash
# .treeignore
node_modules/
dist/
.env
```

<details>
<summary><b>Default exclusions</b></summary>

- `.git/`, `__pycache__/`, `venv/`, `.venv/`
- `node_modules/`, `.idea/`, `.vscode/`
- `.next/`, `dist/`, `build/`
- `.DS_Store`, `Thumbs.db`

</details>

## 💡 Why Tree Generator?

| Problem | Solution |
|---------|----------|
| 📖 Outdated documentation | Auto-generate on every commit |
| 🤔 Complex project structure | Visual overview in seconds |
| 👥 Onboarding new developers | Instant project map |

## 🛠️ Advanced

<details>
<summary><b>Custom output file</b></summary>

```python
# Line 199 in generate_tree.py
output_path = os.path.join(root, "STRUCTURE.md")
```

</details>

<details>
<summary><b>Add custom icons</b></summary>

```python
# Line 88 in generate_tree.py
icons = {
    ".myext": "🎯",
    # ... add yours
}
```

</details>

## 🤝 Contributing

Contributions welcome! See [CONTRIBUTING.md](CONTRIBUTING.md)

- 🐛 Found a bug? [Open an issue](https://github.com/Manalilou/tree-generator/issues)
- 💡 Have an idea? [Start a discussion](https://github.com/Manalilou/tree-generator/discussions)
- 🎨 Want to add icons? Fork and PR!

## 📄 License

MIT © [Manalilou](LICENSE)

---

<div align="center">

**Made with ❤️ for developers**

Give it a ⭐ if this project helped you!

</div>