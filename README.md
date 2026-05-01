# unr3d4ct 🔍

`unr3d4ct` is a lightweight digital forensics tool designed to recover text hidden under low-opacity digital redactions, such as "highlighter" marks or semi-transparent brush strokes often found in mobile photo editors.

---

## 🚀 Overview

Many mobile redaction tools don't actually delete pixel data; they simply overlay a semi-transparent color. `unr3d4ct` performs a multi-pass histogram expansion on your image. By cycling through aggressive contrast, brightness, and gamma adjustments, it isolates the slight color variances between a redaction stroke and the underlying text.

---

## 🛠 Installation

### 1. Clone the Repository
Open your terminal and run:
```bash
git clone https://github.com/nxtcoreee3/unr3d4ct.git
cd unr3d4ct
```

### 2. Install Dependencies
Ensure you have Python 3 installed, then run:
```bash
pip install -r requirements.txt
```

*(Optional for macOS/Linux users)*: Make the installer executable:
```bash
chmod +x install.sh
./install.sh
```

---

## 💻 Usage

Run the script and provide the path to the redacted image:

```bash
python3 unr3d4ct.py evidence.png
```

### What happens next?
1. The tool generates a spectrum of exposure variants using different **Alpha** (Contrast), **Beta** (Brightness), and **Gamma** levels.
2. Results are saved to a new folder: `unr3d4ct_exports/`.
3. **macOS Users:** The folder will automatically pop open, and a system alert will sound when finished.

---

## ⚙️ How it Works

The script applies the following forensic transformations:
*   **Linear Scaling:** Stretches the pixel values to maximize the difference between the "black" of the ink and the "black" of the redaction.
*   **Gamma Correction:** Targets the shadows specifically to lift hidden details without blowing out the highlights.
*   **Batch Processing:** Since every redaction is different, the tool generates multiple variations so you can visually identify the "sweet spot."

---

## 🐧 OS Support

| OS | Command | Features |
| :--- | :--- | :--- |
| **macOS** | `python3 unr3d4ct.py` | Auto-open Finder, Audio Alerts |
| **Windows** | `python unr3d4ct.py` | Full processing |
| **Linux** | `python3 unr3d4ct.py` | Full processing |

---

## ⚠️ Disclaimer

This tool is for educational and forensic purposes only. It is effective against **translucent** marks (like the iOS/Android highlighter tool). It **cannot** recover data that has been overwritten by 100% opaque vector shapes or solid rectangles, as that pixel data has been physically destroyed.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
