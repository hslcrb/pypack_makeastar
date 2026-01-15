def _draw(lines):
    print('\n'.join(lines))

def _calc(w, h, i):
    # Safe division to calculate width at step i
    return int(w * i / h)

def triangle(width, height=None, char='*'):
    """Left-aligned triangle (samgak)."""
    if height is None: height = 5
    _draw(f"{char * _calc(width, height, i)}" for i in range(1, height + 1))

def right_triangle(width, height=None, char='*'):
    """Right-aligned triangle (usamgak)."""
    if height is None: height = 5
    _draw(f"{char * _calc(width, height, i):>{width}}" for i in range(1, height + 1))

def inverted(width, height=None, char='*'):
    """Inverted left-aligned triangle (yeoksamgak)."""
    if height is None: height = 5
    _draw(f"{char * _calc(width, height, i)}" for i in range(height, 0, -1))

def inverted_right(width, height=None, char='*'):
    """Inverted right-aligned triangle (yeokusamgak)."""
    if height is None: height = 5
    _draw(f"{char * _calc(width, height, i):>{width}}" for i in range(height, 0, -1))

def pyramid(n=5, char='*'):
    """Centered pyramid."""
    _draw(f"{char*(2*i-1):^{2*n-1}}".rstrip() for i in range(1, n+1))

def diamond(n=5, char='*'):
    """Diamond shape."""
    top = [f"{char*(2*i-1):^{2*n-1}}".rstrip() for i in range(1, n+1)]
    _draw(top + top[-2::-1])

def hourglass(n=5, char='*'):
    """Hourglass shape."""
    top = [f"{char*(2*i-1):^{2*n-1}}".rstrip() for i in range(n, 0, -1)]
    _draw(top + top[-2::-1])

def arrow(n=5, char='*'):
    """Right-pointing arrow."""
    part = [f"{char*i}" for i in range(1, n+1)]
    _draw(part + part[-2::-1])

# Aliases (Easy access & Korean phonetics)
samgak = tri = triangle
usamgak = rtri = right_triangle
yeoksamgak = inv = inverted
yeokusamgak = rinv = inverted_right
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
피 = pyramid
다 = diamond
모 = hourglass
화 = arrow

# Korean Choseong Aliases (초성)
ㅅㄱ = triangle
ㅇㅅㄱ = right_triangle
ㅇㅅ = inverted  # YeokSam (Note: WooSam is also ㅇㅅ, but YeokSam takes precedence)
ㅇㅇ = inverted_right # WooYeok
ㅍㄹ = pyramid
ㄷㅇ = diamond
ㅁㄹ = hourglass
ㅎㅅ = arrow
