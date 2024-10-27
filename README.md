# 🌈 Python Potrace - The Ultimate Color Tracker! 🌈

**Welcome to the world of color tracing!** This is a **pure Python port** of Potrace, originally crafted by Peter Selinger. Are you ready to unleash your creativity with colors? Let’s get started!

<img width="200" height="200" src="https://gist.githubusercontent.com/tatarize/42884e5e99cda88aa5ddc2b0ab280973/raw/488cafa1811bd2227458390804910fbc4a90b9ea/head.svg"/>

![head-orig3](https://user-images.githubusercontent.com/3302478/115929160-2757f180-a43c-11eb-88dc-1320706c9a3f.png)

> **Note:** This image has been scaled up by a factor of 3.

![head-scaled](https://user-images.githubusercontent.com/3302478/154810339-6a444bfa-3f2e-4ad0-91cf-40570838a918.png)

---

## 🚀 Why Potrace?

This port is essential because many Python integrations of the original code, like `pypotrace`, encounter installation issues and compilation problems across different operating systems. Our version, written entirely in Python, promises compatibility with nearly everything!

## 🛠️ Installation

To install or to use as a requirement:

```bash
pip install potracer
```

### 🎨 Potrace-CLI
If you want to utilize the Command Line Interface available in the sister project `potrace-cli`, simply run:

```bash
pip install potracer[cli]
```

or:

```bash
pip install potrace-cli
```

The CLI project includes valid console script entrypoints for Potrace. Installing the command-line package will add `potracer` to your console scripts. Remember the `-r` suffix to avoid conflicts with existing installations.

## 📦 Requirements
- **NumPy**: Required for managing bitmap structures.

## ⚡ Speed
While written in Python, this code may perform around **500x slower** than the pure C version of Potrace. However, it remains efficient for general use and creative projects!

## 📜 How To Use

This is a simple script that converts a given file to an SVG using `potracer`. It utilizes **Pillow** for file loading and iterates over curves inside the plist to generate the SVG with corners and curves.

### Example Usage

```python
import sys
from PIL import Image
from potracer import Bitmap, POTRACE_TURNPOLICY_MINORITY  # `potracer` library

def file_to_svg(filename: str):
    try:
        image = Image.open(filename)
    except IOError:
        print(f"🚫 Image ({filename}) could not be loaded.")
        return

    bm = Bitmap(image)
    plist = bm.trace(
        turdsize=2,
        turnpolicy=POTRACE_TURNPOLICY_MINORITY,
        alphamax=1,
        opticurve=False,
        opttolerance=0.2,
    )

    with open(f"{filename}.svg", "w") as fp:
        fp.write(f'''<svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{image.width}" height="{image.height}" viewBox="0 0 {image.width} {image.height}">''')
        parts = []
        for curve in plist:
            fs = curve.start_point
            parts.append(f"M{fs.x},{fs.y}")
            for segment in curve.segments:
                if segment.is_corner:
                    a = segment.c
                    b = segment.end_point
                    parts.append(f"L{a.x},{a.y}L{b.x},{b.y}")
                else:
                    a = segment.c1
                    b = segment.c2
                    c = segment.end_point
                    parts.append(f"C{a.x},{a.y} {b.x},{b.y} {c.x},{c.y}")
            parts.append("z")
        fp.write(f'<path stroke="none" fill="black" fill-rule="evenodd" d="{"".join(parts)}"/>')
        fp.write("</svg>")

if __name__ == '__main__':
    file_to_svg(sys.argv[1])
```

## 🌐 Parallel Projects
This project intentionally mirrors a considerable amount of the API of `pypotrace`, allowing it to serve as a drop-in replacement.

For executing Potrace commands from the command line, this library offers CLI Potrace as an optional package.

## 📜 License
This program is free software; you can redistribute it and/or modify it under the terms of the **GNU General Public License** as published by the **Free Software Foundation**; either version 2, or (at your option) any later version.

Furthermore, this is permitted to be relicensed under any terms that Peter Selinger's original Potrace is licensed under. If he publishes the software under a more permissive license, this port should be considered licensed as such as well.

"Potrace" is a trademark of Peter Selinger. **Permission granted by Peter Selinger.**

---

🌟 **Let's create vibrant and colorful SVGs together with Potrace!** 🌟
