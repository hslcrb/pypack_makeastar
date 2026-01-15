# makeastar

MINIMALIST Python package for printing star patterns.  
No complex loops needed—just import and call.

## Features

- **Optimized**: Uses generator expressions and f-strings for maximum efficiency.
- **Easy to Use**: Intuitive function names (e.g., `star.pyramid(5)`).
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

# 1. Triangle
star.triangle(5)

# 2. Inverted Triangle
star.inverted(5)

# 3. Pyramid
star.pyramid(5)

# 4. Diamond
star.diamond(5)

# 5. Hourglass
star.hourglass(5)

# 6. Arrow (Right)
star.arrow(5)
```

## Supported Patterns

| Function | Description |
|----------|-------------|
| `triangle(n)` | Prints a left-aligned right triangle. |
| `inverted(n)` | Prints an inverted left-aligned right triangle. |
| `pyramid(n)` | Prints a centered pyramid. |
| `diamond(n)` | Prints a diamond shape. |
| `hourglass(n)` | Prints an hourglass shape. |
| `arrow(n)` | Prints a right-pointing arrow. |

## License

This project is licensed under the MIT License.
