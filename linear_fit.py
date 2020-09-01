import matplotlib.pyplot as plot
import random

# y=a+bx
a_theory = 2
b_theory = 0.2
num = 100
noise = 0.5

if __name__ == '__main__':
    x = []  # original value of x
    y = []  # original value of y
    x_sqr = []
    xy = []
    x_sum = 0
    y_sum = 0
    x_sqr_sum = 0
    xy_sum = 0
    for i in range(1, num + 1):
        x.append(i)
        y.append(a_theory + b_theory * x[i - 1] + random.uniform(-noise, noise))

        x_sqr.append(x[i - 1] * x[i - 1])
        xy.append(x[i - 1] * y[i - 1])
        x_sum = x_sum + x[i - 1]
        y_sum = y_sum + y[i - 1]
        x_sqr_sum = x_sqr_sum + x_sqr[i - 1]
        xy_sum = xy_sum + xy[i - 1]
    # Linear fitting calculation
    a_real = (x_sqr_sum * y_sum - x_sum * xy_sum) / (num * x_sqr_sum - x_sum * x_sum)
    b_real = (num * xy_sum - x_sum * y_sum) / (num * x_sqr_sum - x_sum * x_sum)
    print(a_real)
    print(b_real)

    y_linear = []
    for i in range(1, num + 1):
        y_linear.append(a_real + b_real * x[i - 1])
    plot.plot(x, y)
    plot.plot(x, y_linear)
    plot.show()
    # input("input any key to continue.")
