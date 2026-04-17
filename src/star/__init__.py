__version__ = "2.0"
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
    """Next-Gen Star Pattern Engine with Bitmask Optimization."""
    __slots__ = ('bits', 'width', 'height', 'char', '_str', '_lines')
    
    def __init__(self, bits: List[int], width: int, char: str = '*'):
        self.bits = bits
        self.width = width
        self.height = len(bits)
        self.char = char
        self._str: Optional[str] = None
        self._lines: Optional[List[str]] = None

    @classmethod
    def from_lines(cls, lines: List[str], char: str = '*') -> 'Pattern':
        width = max(len(line) for line in lines) if lines else 0
        bits = []
        for line in lines:
            b = 0
            for i, c in enumerate(line):
                if c != ' ':
                    b |= (1 << (width - 1 - i))
            bits.append(b)
        return cls(bits, width, char)

    @property
    def lines(self) -> List[str]:
        if self._lines is None:
            res = []
            fmt = f"{{:0{self.width}b}}"
            for b in self.bits:
                line = fmt.format(b).replace('0', ' ').replace('1', self.char).rstrip()
                res.append(line)
            self._lines = res
        return self._lines

    def __str__(self) -> str:
        if self._str is None:
            self._str = '\n'.join(self.lines)
        return self._str

    def __add__(self, other: 'Pattern') -> 'Pattern':
        """Vertical Join (Top-Bottom)."""
        new_width = max(self.width, other.width)
        s_bits = [b << (new_width - self.width) for b in self.bits]
        o_bits = [b << (new_width - other.width) for b in other.bits]
        return Pattern(s_bits + o_bits, new_width, self.char)

    def __or__(self, other: 'Pattern') -> 'Pattern':
        """Horizontal Join (Left-Right)."""
        h = max(self.height, other.height)
        new_width = self.width + other.width
        new_bits = []
        for i in range(h):
            row_self = self.bits[i] if i < self.height else 0
            row_other = other.bits[i] if i < other.height else 0
            new_bits.append((row_self << other.width) | row_other)
        return Pattern(new_bits, new_width, self.char)

    def __and__(self, other: 'Pattern') -> 'Pattern':
        """Overlay (OR operation on bits)."""
        h = max(self.height, other.height)
        w = max(self.width, other.width)
        new_bits = []
        for i in range(h):
            b1 = (self.bits[i] << (w - self.width)) if i < self.height else 0
            b2 = (other.bits[i] << (w - other.width)) if i < other.height else 0
            new_bits.append(b1 | b2)
        return Pattern(new_bits, w, self.char)

    def __xor__(self, other: 'Pattern') -> 'Pattern':
        """Exclusive Overlay (XOR operation)."""
        h = max(self.height, other.height)
        w = max(self.width, other.width)
        new_bits = []
        for i in range(h):
            b1 = (self.bits[i] << (w - self.width)) if i < self.height else 0
            b2 = (other.bits[i] << (w - other.width)) if i < other.height else 0
            new_bits.append(b1 ^ b2)
        return Pattern(new_bits, w, self.char)

    def __sub__(self, other: 'Pattern') -> 'Pattern':
        """Masking (Subtract other from self)."""
        h = self.height
        w = self.width
        new_bits = []
        for i in range(h):
            b1 = self.bits[i]
            b2 = (other.bits[i] << (w - other.width)) if (i < other.height and w >= other.width) else (other.bits[i] >> (other.width - w)) if i < other.height else 0
            new_bits.append(b1 & ~b2)
        return Pattern(new_bits, w, self.char)

    def __invert__(self) -> 'Pattern':
        """Invert Bits (Negative pattern)."""
        mask = (1 << self.width) - 1
        return Pattern([(~b) & mask for b in self.bits], self.width, self.char)

    def __mul__(self, count: int) -> 'Pattern':
        """Vertical Repeat."""
        if not isinstance(count, int): return NotImplemented
        return Pattern(self.bits * count, self.width, self.char)

    def rotate(self, angle: int = 90) -> 'Pattern':
        """Rotate pattern (90, 180, 270)."""
        angle %= 360
        if angle == 0: return self
        new_bits = [0] * self.width
        for r in range(self.height):
            for c in range(self.width):
                if (self.bits[r] >> (self.width - 1 - c)) & 1:
                    new_bits[c] |= (1 << r)
        res = Pattern(new_bits, self.height, self.char)
        return res.rotate(angle - 90) if angle > 90 else res

    def flip_h(self) -> 'Pattern':
        """Horizontal Mirror."""
        new_bits = []
        for b in self.bits:
            rev = 0
            temp = b
            for _ in range(self.width):
                rev = (rev << 1) | (temp & 1)
                temp >>= 1
            new_bits.append(rev)
        return Pattern(new_bits, self.width, self.char)

    def flip_v(self) -> 'Pattern':
        """Vertical Mirror."""
        return Pattern(self.bits[::-1], self.width, self.char)

    def replace(self, char: str) -> 'Pattern':
        """Change drawing character."""
        return Pattern(self.bits, self.width, char)

    def draw(self) -> None:
        if not self.bits: return
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
    return Pattern.from_lines([char * _calc(w, h, i) for i in range(1, h + 1)], char)

@functools.lru_cache(maxsize=128)
def right_triangle(width: Union[int, str], height: Union[int, str, None] = None, char: str = '*') -> Pattern:
    w = _normalize_int(width, 5)
    h = _normalize_int(height, w)
    return Pattern.from_lines([f"{char * _calc(w, h, i):>{w}}" for i in range(1, h + 1)], char)

@functools.lru_cache(maxsize=128)
def inverted(width: Union[int, str], height: Union[int, str, None] = None, char: str = '*') -> Pattern:
    w = _normalize_int(width, 5)
    h = _normalize_int(height, w)
    return Pattern.from_lines([char * _calc(w, h, i) for i in range(h, 0, -1)], char)

@functools.lru_cache(maxsize=128)
def inverted_right(width: Union[int, str], height: Union[int, str, None] = None, char: str = '*') -> Pattern:
    w = _normalize_int(width, 5)
    h = _normalize_int(height, w)
    return Pattern.from_lines([f"{char * _calc(w, h, i):>{w}}" for i in range(h, 0, -1)], char)

@functools.lru_cache(maxsize=128)
def pyramid(n: Union[int, str] = 5, char: str = '*') -> Pattern:
    size = _normalize_int(n, 5)
    width = 2 * size - 1
    return Pattern.from_lines([f"{char * (2 * i - 1):^{width}}".rstrip() for i in range(1, size + 1)], char)

@functools.lru_cache(maxsize=128)
def rhombus(n: Union[int, str] = 5, char: str = '*') -> Pattern:
    size = _normalize_int(n, 5)
    width = 2 * size - 1
    top = [f"{char * (2 * i - 1):^{width}}".rstrip() for i in range(1, size + 1)]
    return Pattern.from_lines(top + top[-2::-1], char)

@functools.lru_cache(maxsize=128)
def diamond(n: Union[int, str] = 5, char: str = '*') -> Pattern:
    size = _normalize_int(n, 5)
    width = 2 * size - 1
    crown = [f"{char * (size + 2 * i):^{width}}".rstrip() for i in range(size // 2)]
    mid = [char * width]
    pavillion = [f"{char * (2 * i - 1):^{width}}".rstrip() for i in range(size - 1, 0, -1)]
    return Pattern.from_lines(crown + mid + pavillion, char)

@functools.lru_cache(maxsize=128)
def hourglass(n: Union[int, str] = 5, char: str = '*') -> Pattern:
    size = _normalize_int(n, 5)
    width = 2 * size - 1
    top = [f"{char * (2 * i - 1):^{width}}".rstrip() for i in range(size, 0, -1)]
    return Pattern.from_lines(top + top[-2::-1], char)

@functools.lru_cache(maxsize=128)
def arrow(n: Union[int, str] = 5, char: str = '*') -> Pattern:
    size = _normalize_int(n, 5)
    part = [char * i for i in range(1, size + 1)]
    return Pattern.from_lines(part + part[-2::-1], char)

@functools.lru_cache(maxsize=128)
def circle(r: Union[int, str] = 5, char: str = '*') -> Pattern:
    radius = _normalize_int(r, 5)
    width = 2 * radius + 1
    bits = []
    for y in range(-radius, radius + 1):
        row = 0
        for x in range(-radius, radius + 1):
            if x*x + y*y <= radius*radius:
                row |= (1 << (width - 1 - (x + radius)))
        bits.append(row)
    return Pattern(bits, width, char)

@functools.lru_cache(maxsize=128)
def heart(n: Union[int, str] = 10, char: str = '*') -> Pattern:
    size = _normalize_int(n, 10)
    width = 2 * size + 1
    bits = []
    for y in range(size, -size, -1):
        row = 0
        for x in range(-size, size + 1):
            # Heart formula: (x^2 + (1.2y - sqrt|x|)^2) <= size^2
            xx = x / (size * 0.6)
            yy = y / (size * 0.6)
            if xx**2 + (yy - abs(xx)**0.5)**2 <= 1:
                row |= (1 << (width - 1 - (x + size)))
        bits.append(row)
    return Pattern(bits, width, char)

def custom(func, w: int, h: int, char: str = '*') -> Pattern:
    """Custom formula: func(x, y) returns bool."""
    bits = []
    for y in range(h):
        row = 0
        for x in range(w):
            if func(x, y):
                row |= (1 << (w - 1 - x))
        bits.append(row)
    return Pattern(bits, w, char)

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
        'circle': circle, 'won': circle,
        'heart': heart, 'simjang': heart,
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
원 = ㅇ = ㅇㅎ = circle
심장 = 하트 = ㅎㅌ = ㅅㅈ = heart

tri, rtri, inv, rinv, rtinv, pyra, rhom, dia, morae, hwasal = (
    triangle, right_triangle, inverted, inverted_right, inverted_right, 
    pyramid, rhombus, diamond, hourglass, arrow
)
circ, won, hrt, simjang = circle, circle, heart, heart
