def EXY_YIQ(p) -> bool:
    """Excess yellow from YIQ color space"""
    Y = int(0.299 * p[0] + 0.587 * p[1] + 0.114 * p[2])
    I = int(0.596 * p[0] - 0.275 * p[1] - 0.321 * p[2])
    Q = int(0.212 * p[0] - 0.523 * p[1] + 0.311 * p[2])

    if (Y > I) & (Y > Q):
        return True
    return False


def elongation_feature(image) -> double:
    try:
        length = len(image)
        width = len(image[0])
    except:
        return -1

    return (length - width) / (length + width)


def R_n(p):
    return p[1] / (sum(p))


def ExG_RGB(p):
    return 2 * p[1] - p[0] - p[2]


def CIVE_RGB(p):
    return 0.441 * p[0] - 0.811 * p[1] + 0.385 * p[2] + 18.78
