def rgbString(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'


def intToColor(n):
    r = (n * 25) % 255
    g = (n**3 * 61) % 255
    b = (n * 34) % 255
    return rgbString(r, g, b)

