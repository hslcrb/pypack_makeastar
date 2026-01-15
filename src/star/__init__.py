def _draw(lines):
    """Efficiently prints the generated pattern lines."""
    print('\n'.join(lines))

def triangle(n=5, char='*'):
    """Prints a left-aligned triangle."""
    _draw(f"{char*i}" for i in range(1, n+1))

def inverted(n=5, char='*'):
    """Prints an inverted triangle."""
    _draw(f"{char*i}" for i in range(n, 0, -1))

def pyramid(n=5, char='*'):
    """Prints a centered pyramid."""
    _draw(f"{char*(2*i-1):^{2*n-1}}".rstrip() for i in range(1, n+1))

def diamond(n=5, char='*'):
    """Prints a diamond shape."""
    upper = [f"{char*(2*i-1):^{2*n-1}}".rstrip() for i in range(1, n+1)]
    _draw(upper + upper[-2::-1])

def hourglass(n=5, char='*'):
    """Prints an hourglass shape."""
    upper = [f"{char*(2*i-1):^{2*n-1}}".rstrip() for i in range(n, 0, -1)]
    _draw(upper + upper[-2::-1])

def arrow(n=5, char='*'):
    """Prints a right-pointing arrow."""
    part = [f"{char*i}" for i in range(1, n+1)]
    _draw(part + part[-2::-1])
