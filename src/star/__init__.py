__version__ = "1.1"
__author__ = "Rheehose (Rhee Creative)"
__email__ = "rheehose@rheehose.com"

import sys
import re
from typing import Optional, Union, List

class Pattern:
    """ASCII Star Pattern object supporting composition."""
    def __init__(self, lines: List[str]):
        self.lines = [line.rstrip() for line in lines]

    def __str__(self) -> str:
        return '\n'.join(self.lines)

    def __add__(self, other: 'Pattern') -> 'Pattern':
        """Vertical composition: Pattern A + Pattern B."""
        return Pattern(self.lines + other.lines)

    def __mul__(self, count: int) -> 'Pattern':
        """Vertical repetition: Pattern * N."""
        if not isinstance(count, int):
            return NotImplemented
        return Pattern(self.lines * count)

    def draw(self) -> None:
        """Output the pattern to stdout."""
        if not self.lines:
            return
        sys.stdout.write('\n'.join(self.lines) + '\n')

def _draw(lines: Union[List[str], 'Pattern']) -> None:
    """Utility to draw lines or a Pattern object."""
    if isinstance(lines, Pattern):
        lines.draw()
    else:
        sys.stdout.write('\n'.join(lines) + '\n')

def _calc(w: int, h: int, i: int) -> int:
    return i if w == h else (w * i) // h

def _normalize_int(value: Union[int, float, str, None], default: Optional[int] = None) -> int:
    if value is None:
        return default or 0
    try:
        if isinstance(value, str):
            value = value.strip().replace(' ', '')
        return int(float(value))
    except (ValueError, TypeError):
        return default or 0

def triangle(width: Union[int, str], height: Union[int, str, None] = None, char: str = '*') -> Pattern:
    """Left-aligned triangle."""
    w = _normalize_int(width, 5)
    h = _normalize_int(height, w)
    lines = [f"{char * _calc(w, h, i)}" for i in range(1, h + 1)]
    return Pattern(lines)

def right_triangle(width: Union[int, str], height: Union[int, str, None] = None, char: str = '*') -> Pattern:
    """Right-aligned triangle."""
    w = _normalize_int(width, 5)
    h = _normalize_int(height, w)
    lines = [f"{char * _calc(w, h, i):>{w}}" for i in range(1, h + 1)]
    return Pattern(lines)

def inverted(width: Union[int, str], height: Union[int, str, None] = None, char: str = '*') -> Pattern:
    """Inverted left-aligned triangle."""
    w = _normalize_int(width, 5)
    h = _normalize_int(height, w)
    lines = [f"{char * _calc(w, h, i)}" for i in range(h, 0, -1)]
    return Pattern(lines)

def inverted_right(width: Union[int, str], height: Union[int, str, None] = None, char: str = '*') -> Pattern:
    """Inverted right-aligned triangle."""
    w = _normalize_int(width, 5)
    h = _normalize_int(height, w)
    lines = [f"{char * _calc(w, h, i):>{w}}" for i in range(h, 0, -1)]
    return Pattern(lines)

def pyramid(n: Union[int, str] = 5, char: str = '*') -> Pattern:
    """Centered pyramid."""
    size = _normalize_int(n, 5)
    width = 2 * size - 1
    lines = [f"{char * (2 * i - 1):^{width}}" for i in range(1, size + 1)]
    return Pattern(lines)

def rhombus(n: Union[int, str] = 5, char: str = '*') -> Pattern:
    """Rhombus shape (formerly diamond)."""
    size = _normalize_int(n, 5)
    width = 2 * size - 1
    top = [f"{char * (2 * i - 1):^{width}}" for i in range(1, size + 1)]
    return Pattern(top + top[-2::-1])

def diamond(n: Union[int, str] = 5, char: str = '*') -> Pattern:
    """Gem-style diamond shape."""
    size = _normalize_int(n, 5)
    width = 2 * size - 1
    # Crown part: expanding top
    crown = [f"{char * (size + 2 * i):^{width}}" for i in range(size // 2)]
    # Mid part: widest point
    mid = [char * width]
    # Pavillion part: tapering bottom
    pavillion = [f"{char * (2 * i - 1):^{width}}" for i in range(size - 1, 0, -1)]
    return Pattern(crown + mid + pavillion)

def hourglass(n: Union[int, str] = 5, char: str = '*') -> Pattern:
    """Hourglass shape."""
    size = _normalize_int(n, 5)
    width = 2 * size - 1
    top = [f"{char * (2 * i - 1):^{width}}" for i in range(size, 0, -1)]
    return Pattern(top + top[-2::-1])

def arrow(n: Union[int, str] = 5, char: str = '*') -> Pattern:
    """Right-pointing arrow."""
    size = _normalize_int(n, 5)
    part = [char * i for i in range(1, size + 1)]
    return Pattern(part + part[-2::-1])

def draw(command: Union[str, Pattern, int] = 5) -> None:
    """
    Universal draw function. 
    Accepts command strings, Pattern objects, or integers (default pyramid).
    """
    if isinstance(command, Pattern):
        command.draw()
        return
    
    if isinstance(command, int):
        pyramid(command).draw()
        return

    # Normalized parsing
    normalized = re.sub(r'[,.\s]+', ' ', command.strip())
    parts = normalized.split()
    if not parts: return
    
    func_name = parts[0].lower()
    args = [_normalize_int(p, 5) for p in parts[1:]]
    
    func_map = {
        'triangle': triangle, 'tri': triangle, 'samgak': triangle,
        'right': right_triangle, 'rtri': right_triangle, 'usamgak': right_triangle,
        'inverted': inverted, 'inv': inverted, 'yeoksamgak': inverted,
        'inverted_right': inverted_right, 'rinv': inverted_right, 'rtinv': inverted_right,
        'pyramid': pyramid, 'pyra': pyramid, 'pyramide': pyramid,
        'rhombus': rhombus, 'rhom': rhombus, 'marummo': rhombus,
        'diamond': diamond, 'dia': diamond, 'gem': diamond,
        'hourglass': hourglass, 'morae': hourglass,
        'arrow': arrow, 'hwasal': arrow,
    }
    
    func = func_map.get(func_name)
    if func:
        func(*args).draw()

# --- Aliases & Localization ---

# Top level shortcut
별 = 그려 = 모양 = draw

# Shape Functions
삼각형 = 삼 = ㅅㄱ = ㅅㄱㅎ = triangle
우측삼각형 = 오른쪽삼각형 = 우삼 = ㅇㅅㄱ = ㅇㅊㅅㄱ = right_triangle
역삼각형 = 역삼 = ㅇㅅ = ㅇㅅㄱㅎ = inverted
우측역삼각형 = 오른쪽역삼각형 = 우역 = ㅇㅇ = ㅇㅊㅇㅅ = inverted_right
피라미드 = 피라 = ㅍㄹ = ㅍㄹㅁㄷ = pyramid
다이아몬드 = 다이아 = ㄷㅇ = ㄷㅇㅇㅁㄷ = diamond
마름모 = 마 = ㅁㄹㅁ = ㅁㄹㅁㄴ = rhombus
모래시계 = 모 = ㅁㄹ = ㅁㄹㅅㄱ = hourglass
화살표 = 화 = ㅎㅅ = ㅎㅅㅍ = arrow

# Extra convenience
tri = triangle
rtri = right_triangle
inv = inverted
rinv = rtinv = inverted_right
pyra = pyramid
rhom = rhombus
dia = diamond
morae = hourglass
hwasal = arrow
