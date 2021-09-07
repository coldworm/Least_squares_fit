import matplotlib.pyplot as plot
import math
import random
import numpy as np
from scipy.optimize import fsolve
import sympy

N = 40
noise = 0.05
x0_t = 1
y0_t = 1


# F(A,B,C,D,E) = sum(x^2 + Axy +By^2 + Cx +Dy + E)^2
# | sum(x^2 * y^2), sum(x * y^3), sum(x^2 * y), sum(x * y^2), sum(x * y) |   |A|    |sum(x^3 * y)  |
# | sum(x * y^3),   sum(y^4),     sum(x * y^2), sum(y^3),     sum(y^2)   |   |B|    |sum(x^2 * y^2)|
# | sum(x^2 * y),   sum(x * y^2), sum(x^2),     sum(x * y),   sum(x)     | * |C| = -|sum(x^3)      |
# | sum(x * y^2),   sum(y^3),     sum(x * y),   sum(y^2),     sum(y)     |   |D|    |sum(x^2 * y)  |
# | sum(x * y),     sum(y^2),     sum(x),       sum(y),       N          |   |E|    |sum(x^2)      |
def raw_data_to_normal_equation(x, y):
    x_sum = 0
    y_sum = 0
    xx_sum = 0
    xy_sum = 0
    yy_sum = 0
    xxx_sum = 0
    xxy_sum = 0
    xyy_sum = 0
    yyy_sum = 0
    xxxx_sum = 0
    xxxy_sum = 0
    xxyy_sum = 0
    xyyy_sum = 0
    yyyy_sum = 0

    for n in range(0, len(x)):
        x_sum += x[n]
        y_sum += y[n]
        xx_sum += x[n] ** 2
        xy_sum += x[n] * y[n]
        yy_sum += y[n] ** 2
        xxx_sum += x[n] ** 3
        xxy_sum += x[n] ** 2 * y[n]
        xyy_sum += y[n] ** 2 * x[n]
        yyy_sum += y[n] ** 3
        xxxx_sum += x[n] ** 4
        xxxy_sum += x[n] ** 3 * y[n]
        xxyy_sum += x[n] ** 2 * y[n] ** 2
        xyyy_sum += y[n] ** 3 * x[n]
        yyyy_sum += y[n] ** 4

    # x^2 + Axy + By^2 + Cx + Dy + E = 0
    x_n = np.mat([[xxyy_sum, xyyy_sum, xxy_sum, xyy_sum, xy_sum],
                  [xyyy_sum, yyyy_sum, xyy_sum, yyy_sum, yy_sum],
                  [xxy_sum, xyy_sum, xx_sum, xy_sum, x_sum],
                  [xyy_sum, yyy_sum, xy_sum, yy_sum, y_sum],
                  [xy_sum, yy_sum, x_sum, y_sum, len(x)]])
    y_n = [-xxxy_sum, -xxyy_sum, -xxx_sum, -xxy_sum, -xx_sum]

    res = np.linalg.solve(x_n, y_n)
    return res


# Circle:(x - d)^2 + (y - e)^2 + r = 0     with (r=-1)
#        x^2 - 2dx + d^2 + y^2 - 2ey + e^2 - 1 = 0
#
# Ellipse:X^2 + A*XY + B*Y^2 + C*X + D*Y + E = 0
# Ellipse*matrix->Circle: [X, Y] * [[a c], [c b]] = [x, y]
#   x = aX + cY, y = cX + bY
#
# (a^2*X^2 + 2ac*XY + c^2*Y^2 - 2ad*X - 2cd*Y + d^2) + (c^2*X^2 + 2bc*XY + b^2*Y^2 - 2ce*X - 2be*Y + e^2) + r = 0
# (2ac + 2bc)/(a^2 + c^2) = A
# (b^2 + c^2)/(a^2 + c^2) = B
# -2(ad+ce)/(a^2 + c^2) = C
# -2(cd+be)/(a^2 + c^2) = D
# (d^2 + e^2 + r)/(a^2 + c^2) = E
def fsolve_func(i, coef):
    a, b, c, d, e = i[0], i[1], i[2], i[3], i[4]
    A, B, C, D, E = coef[0], coef[1], coef[2], coef[3], coef[4]
    return [(2 * a * c + 2 * b * c) / (a ** 2 + c ** 2) - A,
            (b ** 2 + c ** 2) / (a ** 2 + c ** 2) - B,
            2 * (a * d + c * e) / (a ** 2 + c ** 2) + C,
            2 * (c * d + b * e) / (a ** 2 + c ** 2) + D,
            (d ** 2 + e ** 2 - 1) / (a ** 2 + c ** 2) - E]


if __name__ == '__main__':
    mat_c2e = [[0.6, 0.4], [0.4, 0.8]]  # matrix for circle to ellipse
    # mat_e2c = [[2.5, -1.25], [-1.25, 1.875]]

    # generate original points
    rad = -math.pi
    x_o = [math.cos(rad) + x0_t]
    y_o = [math.sin(rad) + y0_t + random.uniform(-noise, noise)]
    x_1 = [x_o[0] * mat_c2e[0][0] + y_o[0] * mat_c2e[0][1]]
    y_1 = [x_o[0] * mat_c2e[1][0] + y_o[0] * mat_c2e[1][1]]
    # x_2 = [x_1[0] * mat_e2c[0][0] + y_1[0] * mat_e2c[0][1]]
    # y_2 = [x_1[0] * mat_e2c[1][0] + y_1[0] * mat_e2c[1][1]]

    for i in range(1, N):
        rad = rad + 2 * math.pi / N
        x_o.append(math.cos(rad) + x0_t)
        y_o.append(math.sin(rad) + y0_t + random.uniform(-noise, noise))

        x_1.append(x_o[i] * mat_c2e[0][0] + y_o[i] * mat_c2e[0][1])
        y_1.append(x_o[i] * mat_c2e[1][0] + y_o[i] * mat_c2e[1][1])
        # x_2.append(x_1[i] * mat_e2c[0][0] + y_1[i] * mat_e2c[0][1])
        # y_2.append(x_1[i] * mat_e2c[1][0] + y_1[i] * mat_e2c[1][1])

    plot.scatter(x_o, y_o, s=10, facecolors='none', edgecolors='r', alpha=0.9)
    plot.scatter(x_1, y_1, s=10, facecolors='none', edgecolors='b', alpha=0.9)
    # plot.scatter(x_2, y_2, s=10, facecolors='none', edgecolors='g', alpha=0.9)

    [A, B, C, D, E] = raw_data_to_normal_equation(x_1, y_1)
    print('A B C D E: %f %f %f %f %f' % (A, B, C, D, E))

    mat = np.mat([[1, A / 2], [A / 2, B]])
    print('Center of ellipse:')
    print(-0.5 * np.dot(np.mat([C, D]), np.linalg.inv(mat)))

    # a = sympy.Symbol('a')
    # b = sympy.Symbol('b')
    # c = sympy.Symbol('c')
    # d = sympy.Symbol('d')
    # e = sympy.Symbol('e')
    # res = sympy.solve([(2 * a * c + 2 * b * c) / (a**2 + c**2) - A,
    #                    (b ** 2 + c ** 2) / (a ** 2 + c ** 2) - B,
    #                    2 * (a * d + c * e) / (a ** 2 + c ** 2) + C,
    #                    2 * (c * d + b * e) / (a ** 2 + c ** 2) + D,
    #                    (d ** 2 + e ** 2 - 1) / (a ** 2 + c ** 2)],
    #                   [a, b, c, d, e])

    [a, b, c, d, e] = fsolve(fsolve_func, np.array([0.1, 0.1, 0.1, 0.1, 0.1]), np.array([A, B, C, D, E]))
    print('a b c d e:  %f %f %f %f %f' % (a, b, c, d, e))

    print('\nEquation of ellipse:\nx^2 + (%f))*xy + (%f)*y^2 + (%f)*x + (%f)*y + (%f) = 0' % (A, B, C, D, E))
    print('\nMatrix from ellipse to circle:')
    print(np.array([[a, c], [c, b]]))

    print('\nEquation of circle:\n(x - (%f))^2 + (y - (%f))^2 = 1' % (d, e))
    print('\nMatrix from circle to ellipse:')
    print(np.linalg.inv([[a, c], [c, b]]))

    # generate final points
    rad = -math.pi
    x_f = [math.cos(rad) + d]
    y_f = [math.sin(rad) + e]

    for i in range(1, 2*N):
        rad = rad + 2 * math.pi / (2*N)
        x_f.append(math.cos(rad) + d)
        y_f.append(math.sin(rad) + e)
    plot.plot(x_f, y_f, alpha=0.9)

    plot.axis('equal')
    plot.show()
