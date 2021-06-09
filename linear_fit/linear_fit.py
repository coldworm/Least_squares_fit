# Simulation of least-squares linear fitting
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

from tkinter import *
from tkinter import filedialog
import matplotlib.pyplot as plot
import random

# y=a+bx
a_theory = 2
b_theory = 0.2
num_s = 100
noise_s = 0.5


def load_data(filename):
    data = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            line = line.split(',')
            current = [float(item) for item in line]
            data.append(current)
    return data


def generate_simulate_data(num, a, b, noise):
    x = []
    y = []
    for i in range(1, num + 1):
        x.append(i)
        y.append(a + b * x[i - 1] + random.uniform(-noise, noise))
        # print(x[i-1], ',', '%.3f' % y[i-1])
    return x, y


def linear_fit(x, y):
    x_sqr = []
    xy = []
    x_sum = 0
    y_sum = 0
    x_sqr_sum = 0
    xy_sum = 0
    for i in range(1, len(x)):
        x_sqr.append(x[i - 1] * x[i - 1])
        xy.append(x[i - 1] * y[i - 1])
        x_sum = x_sum + x[i - 1]
        y_sum = y_sum + y[i - 1]
        x_sqr_sum = x_sqr_sum + x_sqr[i - 1]
        xy_sum = xy_sum + xy[i - 1]
    # Linear fitting calculation
    a_real = (x_sqr_sum * y_sum - x_sum * xy_sum) / (len(x) * x_sqr_sum - x_sum * x_sum)
    b_real = (len(x) * xy_sum - x_sum * y_sum) / (len(x) * x_sqr_sum - x_sum * x_sum)
    return a_real, b_real


class MyWindow:

    def __init__(self):
        self.window = Tk()
        self.window.title('Linear fit')
        self.window.geometry('400x300')

        Button(self.window, text='Load', bg='#008B8B', command=self.select_file, width=8) \
            .place(relx=.05, rely=.15, anchor="w")
        self.file_path = Entry(self.window, width=36, state=DISABLED)
        self.file_path.place(relx=.25, rely=.15, anchor="w")

        self.radio_v = IntVar()
        self.radio_v.set(2)
        Radiobutton(self.window, variable=self.radio_v, text="CSV data", value=1, command=self.change_task)\
            .place(relx=.05, rely=.25, anchor="nw")
        Radiobutton(self.window, variable=self.radio_v, text="Simulation", value=2, command=self.change_task)\
            .place(relx=.3, rely=.25, anchor="nw")

        self.res_info = StringVar()
        self.res_info.set('Start')
        Message(self.window, textvariable=self.res_info, bg="white", width=450).place(relx=.05, rely=.35, anchor="nw")
        self.change_task()
        self.window.mainloop()

    def select_file(self):
        self.file_path.config(state=NORMAL)
        self.file_path.delete(0, END)
        file_name = filedialog.askopenfilename(title='Select row data', filetypes=[("CSV", ".csv"), ('All Files', '*')])
        self.file_path.insert(0, file_name)
        self.file_path.config(state=DISABLED)

        if len(file_name) == 0:
            return

        if self.radio_v.get() == 1:
            self.change_task()

    def change_task(self):
        x_t = []
        y_t = []
        if self.radio_v.get() == 1:
            file_name = self.file_path.get()
            if len(file_name) == 0:
                return
            data = load_data(file_name)
            for i, j in data:
                x_t.append(i)
                y_t.append(j)
        elif self.radio_v.get() == 2:
            x_t, y_t = generate_simulate_data(num_s, a_theory, b_theory, noise_s)

        a_real, b_real = linear_fit(x_t, y_t)
        self.res_info.set('%f, %f' % (a_real, b_real))
        y_linear = []
        for i in range(1, len(x_t) + 1):
            y_linear.append(a_real + b_real * x_t[i - 1])
        plot.clf()
        plot.plot(x_t, y_t)
        plot.plot(x_t, y_linear)
        plot.show()


if __name__ == '__main__':
    MyWindow()
