def som_n(main, other):
    return main / sum(other)


def EXY_YIQ(p):
    """Excess yellow from YIQ color space"""
    Y = int(0.299 * p[0] + 0.587 * p[1] + 0.114 * p[2])
    I = int(0.596 * p[0] - 0.275 * p[1] - 0.321 * p[2])
    Q = int(0.212 * p[0] - 0.523 * p[1] + 0.311 * p[2])

    Y_n = som_n(Y, [Y, I, Q])
    I_n = som_n(I, [Y, I, Q])
    Q_n = som_n(Q, [Y, I, Q])

    return 2 * Y_n - I_n - Q_n


def elongation_feature(image):
    try:
        length = len(image)
        width = len(image[0])
    except:
        return -1

    return (length - width) / (length + width)


def R_n(p):
    return p[1] / (sum(p))


def ExG_RGB(p):
    return 2 * p[1] / sum(p) - p[0] / sum(p) - p[2] / sum(p)


def CIVE_RGB(p):
    return 0.441 * p[0] / sum(p) - 0.811 * p[1] / sum(p) \
           + 0.385 * p[2] / sum(p) + 18.78
