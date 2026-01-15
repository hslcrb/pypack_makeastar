__version__ = "1.0.0"
__author__ = "Rheehose (Rhee Creative)"
__email__ = "rheehose@rheehose.com"

import sys
from typing import Optional

def _draw(lines) -> None:
    # Use write for faster I/O than print
    sys.stdout.write('\n'.join(lines) + '\n')

def _calc(w: int, h: int, i: int) -> int:
    # Optimized: integer logic
    return i if w == h else (w * i) // h

def triangle(width: int, height: Optional[int] = None, char: str = '*') -> None:
    """Left-aligned triangle (samgak)."""
    # Optimized UX: default height to width for regular triangle
    h = height if height is not None else width
    if h == 0: return # Guard clause
    # Use generator expression for memory efficiency
    _draw(f"{char * _calc(width, h, i)}" for i in range(1, h + 1))

def right_triangle(width: int, height: Optional[int] = None, char: str = '*') -> None:
    """Right-aligned triangle (usamgak)."""
    h = height if height is not None else width
    if h == 0: return
    _draw(f"{char * _calc(width, h, i):>{width}}" for i in range(1, h + 1))

def inverted(width: int, height: Optional[int] = None, char: str = '*') -> None:
    """Inverted left-aligned triangle (yeoksamgak)."""
    h = height if height is not None else width
    if h == 0: return
    _draw(f"{char * _calc(width, h, i)}" for i in range(h, 0, -1))

def inverted_right(width: int, height: Optional[int] = None, char: str = '*') -> None:
    """Inverted right-aligned triangle (yeokusamgak)."""
    h = height if height is not None else width
    if h == 0: return
    _draw(f"{char * _calc(width, h, i):>{width}}" for i in range(h, 0, -1))

def pyramid(n: int = 5, char: str = '*') -> None:
    """Centered pyramid."""
    width = 2 * n - 1
    # Optimized: f-string formatting handles centering
    _draw(f"{char * (2 * i - 1):^{width}}".rstrip() for i in range(1, n + 1))

def diamond(n: int = 5, char: str = '*') -> None:
    """Diamond shape."""
    width = 2 * n - 1
    # Optimization: Generate top half once, reuse reversed for bottom
    top = [f"{char * (2 * i - 1):^{width}}".rstrip() for i in range(1, n + 1)]
    _draw(top + top[-2::-1])

def hourglass(n: int = 5, char: str = '*') -> None:
    """Hourglass shape."""
    width = 2 * n - 1
    top = [f"{char * (2 * i - 1):^{width}}".rstrip() for i in range(n, 0, -1)]
    _draw(top + top[-2::-1])

def arrow(n: int = 5, char: str = '*') -> None:
    """Right-pointing arrow."""
    part = [f"{char * i}" for i in range(1, n + 1)]
    _draw(part + part[-2::-1])

# Aliases (Easy access & Korean phonetics)
samgak = tri = triangle
usamgak = rtri = right_triangle
yeoksamgak = inv = inverted
yeokusamgak = rinv = rtinv = inverted_right
pyra = pyramid
dia = diamond
morae = hourglass
hwasal = arrow

# Korean Hangul Aliases (Full)
삼각형 = triangle
우측삼각형 = 오른쪽삼각형 = right_triangle
역삼각형 = inverted
우측역삼각형 = 오른쪽역삼각형 = inverted_right
피라미드 = pyramid
다이아몬드 = 다이아 = diamond
모래시계 = hourglass
화살표 = arrow

# Korean Short Aliases (줄임말)
삼 = triangle
우삼 = right_triangle
역삼 = inverted
우역 = inverted_right
피라 = pyramid
다 = diamond
모 = hourglass
화 = arrow

# Korean Choseong Aliases (초성)
ㅅㄱ = ㅅㄱㅎ = triangle
ㅇㅅㄱ = ㅇㅊㅅㄱㅎ = ㅇㄹㅉㅅㄱㅎ = right_triangle
ㅇㅅ = ㅇㅅㄱㅎ = inverted
ㅇㅇ = ㅇㅊㅇㅅㄱㅎ = ㅇㄹㅉㅇㅅㄱㅎ = inverted_right
ㅍㄹ = ㅍㄹㅁㄷ = pyramid
ㄷㅇ = ㄷㅇㅇㅁㄷ = diamond
ㅁㄹ = ㅁㄹㅅㄱ = hourglass
ㅎㅅ = ㅎㅅㅍ = arrow
