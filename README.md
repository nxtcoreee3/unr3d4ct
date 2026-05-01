# unr3d4ct 🔍

`unr3d4ct` is a lightweight digital forensics tool designed to recover text hidden under low-opacity digital redactions, such as "highlighter" marks or semi-transparent brush strokes often found in mobile photo editors.

---

## 🚀 Overview

Many mobile redaction tools don't actually delete pixel data; they simply overlay a semi-transparent color. `unr3d4ct` performs a multi-pass histogram expansion on your image. By cycling through aggressive contrast, brightness, and gamma adjustments, it isolates the slight color variances between a redaction stroke and the underlying text.


---


## 🛠 Installation

Due to recent changes in Python package management (PEP 668), it is highly recommended to install `unr3d4ct` within a virtual environment to avoid system conflicts.

### 1. Clone the Repository
```bash
git clone https://github.com/nxtcoreee3/unr3d4ct.git
cd unr3d4ct
```

### 2. Set Up Virtual Environment (Recommended)
```bash
# Create the environment
python3 -m venv venv

# Activate it
# On macOS/Linux:
source venv/bin/activate
# On Windows:
.\venv\Scripts\activate
```

### 3. Install Dependencies
Once the environment is active (you should see `(venv)` in your terminal), run:
```bash
pip install -r requirements.txt
```

---

## 💻 Usage

With your virtual environment active, run the tool on any image:

```bash
python3 unr3d4ct.py path/to/your/image.png
```

*Note: To exit the virtual environment when you are done, simply type `deactivate`.*
```


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
