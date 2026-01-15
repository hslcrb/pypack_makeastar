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
py = pyramid
dia = diamond
morae = hourglass
hwasal = arrow
