from math import sin as m_sin, pi as m_pi

print(m_sin(m_pi / 2))


def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None


pi = 3.14
print(sin(pi / 2))
