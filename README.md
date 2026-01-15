<div align="center">
  <img src="logo.png" width="300" alt="makeastar logo" />
</div>

# makeastar

MINIMALIST Python package for printing star patterns.  
No complex loops needed - just import and call.

## Features

- **Optimized**: Uses generator expressions and f-strings for maximum efficiency.
- **Easy to Use**: Intuitive function names and **Aliases** (e.g., `star.samgak(5)` for triangle).
- **Flexible**: Supports custom width and height for triangles.
- **Lightweight**: Minimal code footprint.

## Installation

```bash
pip install makeastar
```

(Or install locally)

```bash
pip install .
```

## Usage

```python
import star

# 1. Triangle (Aliases: samgak, tri)
star.triangle(5)       # Fixed width=5, default height=5
star.samgak(5, 10)     # Width=5, Height=10
star.tri(5)

# 2. Right Triangle (Aliases: usamgak, rtri)
star.right_triangle(5)
star.usamgak(5)

# 3. Inverted Triangle (Aliases: yeoksamgak, inv)
star.inverted(5)
star.yeoksamgak(5)

# 4. Inverted Right Triangle (Aliases: yeokusamgak, rinv)
star.inverted_right(5)

# 5. Pyramid (Aliases: pyra)
star.pyramid(5)

# 6. Diamond (Aliases: dia)
star.diamond(5)

# 7. Hourglass (Aliases: morae)
star.hourglass(5)

# 8. Arrow (Aliases: hwasal)
star.arrow(5)
```

## Functions & Aliases

| Function | Alias | Description | Parameters |
|----------|-------|-------------|------------|
| `triangle` | `samgak`, `tri` | Left-aligned triangle | `(width, height=width, char='*')` |
| `right_triangle` | `usamgak`, `rtri` | Right-aligned triangle | `(width, height=width, char='*')` |
| `inverted` | `yeoksamgak`, `inv` | Inverted left-aligned triangle | `(width, height=width, char='*')` |
| `inverted_right` | `yeokusamgak`, `rtinv`, `rinv`| Inverted right-aligned triangle | `(width, height=width, char='*')` |
| `pyramid` | `pyra` | Centered pyramid | `(n=5, char='*')` |
| `diamond` | `dia` | Diamond shape | `(n=5, char='*')` |
| `hourglass` | `morae` | Hourglass shape | `(n=5, char='*')` |
| `arrow` | `hwasal` | Right arrow | `(n=5, char='*')` |

## Author

- **Rheehose (Rhee Creative)**
- Email: rheehose@rheehose.com
- GitHub: [hslcrb](https://github.com/hslcrb)
- Copyright © 2008-2026

## License

This project is licensed under the MIT License.
