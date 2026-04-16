__version__ = "1.2"
__author__ = "Rheehose (Rhee Creative)"
__email__ = "rheehose@rheehose.com"

import sys
import re
import functools
from typing import Optional, Union, List

# Optimized string pool for common paddings
_SPACE_CACHE = {}

def _get_spaces(n: int) -> str:
    """Fast space retrieval from cache."""
    if n not in _SPACE_CACHE:
        _SPACE_CACHE[n] = ' ' * n
    return _SPACE_CACHE[n]

class Pattern:
    """Memory-efficient and cached ASCII Star Pattern."""
    __slots__ = ('lines', '_str')
    
    def __init__(self, lines: List[str]):
        self.lines = lines
        self._str = None  # Cache for __str__ output

    def __str__(self) -> str:
        if self._str is None:
            self._str = '\n'.join(self.lines)
        return self._str

    def __add__(self, other: 'Pattern') -> 'Pattern':
        return Pattern(self.lines + other.lines)

    def __mul__(self, count: int) -> 'Pattern':
        if not isinstance(count, int):
            return NotImplemented
        return Pattern(self.lines * count)

    def draw(self) -> None:
        """Optimized draw with pre-cached string."""
        if not self.lines:
            return
        sys.stdout.write(str(self) + '\n')

def _calc(w: int, h: int, i: int) -> int:
    return i if w == h else (w * i) // h

@functools.lru_cache(maxsize=32)
def _normalize_int(value: Union[int, float, str, None], default: int = 5) -> int:
    if value is None:
        return default
    try:
        if isinstance(value, str):
            value = value.strip().replace(' ', '')
        return int(float(value))
    except (ValueError, TypeError):
        return default

@functools.lru_cache(maxsize=128)
def triangle(width: Union[int, str], height: Union[int, str, None] = None, char: str = '*') -> Pattern:
    w = _normalize_int(width, 5)
    h = _normalize_int(height, w)
    return Pattern([char * _calc(w, h, i) for i in range(1, h + 1)])

@functools.lru_cache(maxsize=128)
def right_triangle(width: Union[int, str], height: Union[int, str, None] = None, char: str = '*') -> Pattern:
    w = _normalize_int(width, 5)
    h = _normalize_int(height, w)
    return Pattern([f"{char * _calc(w, h, i):>{w}}" for i in range(1, h + 1)])

@functools.lru_cache(maxsize=128)
def inverted(width: Union[int, str], height: Union[int, str, None] = None, char: str = '*') -> Pattern:
    w = _normalize_int(width, 5)
    h = _normalize_int(height, w)
    return Pattern([char * _calc(w, h, i) for i in range(h, 0, -1)])

@functools.lru_cache(maxsize=128)
def inverted_right(width: Union[int, str], height: Union[int, str, None] = None, char: str = '*') -> Pattern:
    w = _normalize_int(width, 5)
    h = _normalize_int(height, w)
    return Pattern([f"{char * _calc(w, h, i):>{w}}" for i in range(h, 0, -1)])

@functools.lru_cache(maxsize=128)
def pyramid(n: Union[int, str] = 5, char: str = '*') -> Pattern:
    size = _normalize_int(n, 5)
    width = 2 * size - 1
    return Pattern([f"{char * (2 * i - 1):^{width}}".rstrip() for i in range(1, size + 1)])

@functools.lru_cache(maxsize=128)
def rhombus(n: Union[int, str] = 5, char: str = '*') -> Pattern:
    size = _normalize_int(n, 5)
    width = 2 * size - 1
    top = [f"{char * (2 * i - 1):^{width}}".rstrip() for i in range(1, size + 1)]
    return Pattern(top + top[-2::-1])

@functools.lru_cache(maxsize=128)
def diamond(n: Union[int, str] = 5, char: str = '*') -> Pattern:
    size = _normalize_int(n, 5)
    width = 2 * size - 1
    crown = [f"{char * (size + 2 * i):^{width}}".rstrip() for i in range(size // 2)]
    mid = [char * width]
    pavillion = [f"{char * (2 * i - 1):^{width}}".rstrip() for i in range(size - 1, 0, -1)]
    return Pattern(crown + mid + pavillion)

@functools.lru_cache(maxsize=128)
def hourglass(n: Union[int, str] = 5, char: str = '*') -> Pattern:
    size = _normalize_int(n, 5)
    width = 2 * size - 1
    top = [f"{char * (2 * i - 1):^{width}}".rstrip() for i in range(size, 0, -1)]
    return Pattern(top + top[-2::-1])

@functools.lru_cache(maxsize=128)
def arrow(n: Union[int, str] = 5, char: str = '*') -> Pattern:
    size = _normalize_int(n, 5)
    part = [char * i for i in range(1, size + 1)]
    return Pattern(part + part[-2::-1])

def draw(command: Union[str, Pattern, int] = 5) -> None:
    if isinstance(command, Pattern):
        command.draw()
        return
    if isinstance(command, int):
        pyramid(command).draw()
        return
    
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
별 = 그려 = 모양 = draw
삼각형 = 삼 = ㅅㄱ = ㅅㄱㅎ = triangle
우측삼각형 = 오른쪽삼각형 = 우삼 = ㅇㅅㄱ = ㅇㅊㅅㄱ = right_triangle
역삼각형 = 역삼 = ㅇㅅ = ㅇㅅㄱㅎ = inverted
우측역삼각형 = 오른쪽역삼각형 = 우역 = ㅇㅇ = ㅇㅊㅇㅅ = inverted_right
피라미드 = 피라 = ㅍㄹ = ㅍㄹㅁㄷ = pyramid
다이아몬드 = 다이아 = ㄷㅇ = ㄷㅇㅇㅁㄷ = diamond
마름모 = 마 = ㅁㄹㅁ = ㅁㄹㅁㄴ = rhombus
모래시계 = 모 = ㅁㄹ = ㅁㄹㅅㄱ = hourglass
화살표 = 화 = ㅎㅅ = ㅎㅅㅍ = arrow

tri, rtri, inv, rinv, rtinv, pyra, rhom, dia, morae, hwasal = (
    triangle, right_triangle, inverted, inverted_right, inverted_right, 
    pyramid, rhombus, diamond, hourglass, arrow
)
