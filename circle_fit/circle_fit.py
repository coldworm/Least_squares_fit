# Simulation of least-squares circle fitting
# Copyright (C) <2020>  <coldworm>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

# please refer link https://wenku.baidu.com/view/ecda32525beef8c75fbfc77da26925c52dc59156.html

import matplotlib.pyplot as plot
import math
import random

N = 40
noise = 0.2
x0_t = 1
y0_t = 1.5

if __name__ == '__main__':
    # generate original points
    rad =-math.pi
    x_o = [math.cos(rad) + x0_t]
    y_o = [math.sin(rad) + random.uniform(-noise, noise) + y0_t]
    for i in range(1, N):
        rad = rad + 2*math.pi / N
        x_o.append(math.cos(rad) + x0_t)
        y_o.append(math.sin(rad) + random.uniform(-noise, noise) + y0_t)
    plot.scatter(x_o, y_o, s=10, facecolors='none', edgecolors='b', alpha=0.9)
    
    sum_x = 0
    sum_y = 0
    sum_x2 = 0
    sum_y2 = 0
    sum_x3 = 0
    sum_y3 = 0
    sum_xy = 0
    sum_x1y2 = 0
    sum_x2y1 = 0
    for i in range(0, N):
        x2 = x_o[i] * x_o[i]
        y2 = y_o[i] * y_o[i]
        sum_x = sum_x + x_o[i]
        sum_y = sum_y + y_o[i]
        sum_x2 = sum_x2 + x2
        sum_y2 = sum_y2 + y2
        sum_x3 = sum_x3 + x2 * x_o[i]
        sum_y3 = sum_y3 + y2 * y_o[i]
        sum_xy = sum_xy + x_o[i] * y_o[i]
        sum_x1y2 = sum_x1y2 + y2 * x_o[i]
        sum_x2y1 = sum_x2y1 + x2 * y_o[i]
    M11 = N * sum_x2 - sum_x * sum_x
    M12 = M21 = N * sum_xy - sum_x * sum_y
    M22 = N * sum_y2 - sum_y * sum_y
    H1 = N * sum_x3 + N * sum_x1y2 - (sum_x2 + sum_y2) * sum_x
    H2 = N * sum_y3 + N * sum_x2y1 - (sum_x2 + sum_y2) * sum_y
    A = (H2 * M12 - H1 * M22) / (M11 * M22 - M12 * M21)
    B = (H2 * M11 - H1 * M21) / (M12 * M22 - M11 * M22)
    C = -(sum_x2 + sum_y2 + A * sum_x + B * sum_y)/N

    # calculate results
    x0 = -A/2
    y0 = -B/2
    r = math.sqrt(A*A + B*B - 4*C)/2
    print("x0:", x0, " y0:", y0, " r:", r)

    # generate new points
    rad =-math.pi
    x_n = [math.cos(rad) + x0]
    y_n = [math.sin(rad) + y0]
    for i in range(1, 2*N+1):
        rad = rad + 2*math.pi / (2*N)
        x_n.append(math.cos(rad) + x0)
        y_n.append(math.sin(rad) + y0)
    plot.plot(x_n, y_n, 'r')

    plot.axis("equal")
    plot.show()
