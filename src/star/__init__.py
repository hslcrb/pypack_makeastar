def _draw(lines):
    print('\n'.join(lines))

def _calc(w, h, i):
    return int(w * i / h)

def triangle(width, height=5, char='*'):
    """Left-aligned triangle."""
    if height is None: height = 5
    _draw(f"{char * _calc(width, height, i)}" for i in range(1, height + 1))

def right_triangle(width, height=5, char='*'):
    """Right-aligned triangle."""
    if height is None: height = 5
    _draw(f"{char * _calc(width, height, i):>{width}}" for i in range(1, height + 1))

def inverted(width, height=5, char='*'):
    """Inverted left-aligned triangle."""
    if height is None: height = 5
    _draw(f"{char * _calc(width, height, i)}" for i in range(height, 0, -1))

def inverted_right(width, height=5, char='*'):
    """Inverted right-aligned triangle."""
    if height is None: height = 5
    _draw(f"{char * _calc(width, height, i):>{width}}" for i in range(height, 0, -1))

def pyramid(n=5, char='*'):
    """Centered pyramid (width auto-scaled to 2n-1)."""
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
