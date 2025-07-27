# 🧾 QR Code Generator

A simple Python utility to generate QR codes in **PNG** and **SVG** formats for any URL.

---

## ✨ Features

- Generate QR codes in:
  - 🖼️ PNG format
  - 🧩 SVG format
- Set:
  - Output file name
  - Colors for SVG QR codes

---

## 🛠️ Requirements

Install dependencies using:

```bash
pip install qrcode[pil] qrcode[svg]
```

---

## 🧪 Using a Virtual Environment (Recommended)

If you're using a Python virtual environment, follow these steps:

```bash
# Create a virtual environment
python3 -m venv venv

# Activate the environment
source venv/bin/activate
```

Once activated, your terminal will look like:

```bash
(venv) ➜  QR_generator git:(main)
```

After you're done running the code:

```bash
# Deactivate the virtual environment
deactivate
```

---

## 🚀 Usage

### Generate PNG QR Code

```python
from qr_code_generator import generate_qr_code

generate_qr_code(
    url='https://naming-ceremony-ac3e8.web.app/',
    file_name='naming_ceremony.png'
)
```

### Generate SVG QR Code

```python
from qr_code_generator import generate_svg_qr_code

generate_svg_qr_code(
    url='https://naming-ceremony-ac3e8.web.app/',
    file_name='naming_ceremony.svg',
    line_color='black',
    background_color='white'
)
```

---

## 📁 Project Structure

```
.
├── qr_code_generator.py
├── naming_ceremony.png       # Example PNG output
├── naming_ceremony.svg       # Example SVG output
├── venv/                     # Virtual environment (excluded from Git)
├── .gitignore
└── README.md
```

---

## 👤 Author

**Harsha Vardhan**  
🔗 [GitHub](https://github.com/harsha-snoogs)

---

⭐ _Star this repo if you found it useful!_
