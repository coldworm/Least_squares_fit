from tkinter import *
from tkinter import filedialog
import numpy as np

# example1 x_1 + 2*x_2 + 3*x_3 = y
# raw data in csv file:
# 1,2,3,14
# 1,1,2,9
# 2,1,4,16
# result: [1. 2. 3.]

# example2 c + x_1 + 2*x_2 + 3*x_3 = y
# raw data in csv file:
# 1,2,3,15
# 1,1,2,10
# 2,1,4,17
# 3,2,2,14
# result: [1. 1. 2. 3.]


def load_data(filename):
    data = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            line = line.split(',')
            current = [float(item) for item in line]
            data.append(current)
    return data


# x: x vector values
# y: y values
# c: const item flag
def raw_data_to_normal_equation(x, y, c):
    if not c:
        x_n = np.empty(shape=(0, x.shape[1]))
        y_n = []
        for i in range(x.shape[1]):
            tmp = []
            for j in range(x.shape[1]):
                tmp.append(np.sum(x[:, i] * x[:, j]))
            x_n = np.r_[x_n, [tmp]]
            y_n.append(np.sum(x[:, i] * y))
    else:
        x_n = np.empty(shape=(0, x.shape[1] + 1))
        y_n = []
        for i in range(x.shape[1]+1):
            tmp = []
            for j in range(x.shape[1]+1):
                if i == 0:
                    if j == 0:
                        tmp.append(x.shape[0])
                    else:
                        tmp.append(np.sum(x[:, j-1]))
                else:
                    if j == 0:
                        tmp.append(np.sum(x[:, i-1]))
                    else:
                        tmp.append(np.sum(x[:, i-1] * x[:, j-1]))
            x_n = np.r_[x_n, [tmp]]
            if i == 0:
                y_n.append(np.sum(y))
            else:
                y_n.append(np.sum(x[:, i-1] * y))
    return x_n, y_n


class MyWindow:

    def __init__(self):
        self.window = Tk()
        self.window.title('Multi-parameter fit')
        self.window.geometry('400x300')

        Button(self.window, text='Load', bg='#008B8B', command=self.select_file, width=8)\
            .place(relx=.05, rely=.15, anchor="w")
        self.file_path = Entry(self.window, width=36, state=DISABLED)
        self.file_path.place(relx=.25, rely=.15, anchor="w")

        self.const_item = BooleanVar()
        Checkbutton(self.window, text="Constant item", variable=self.const_item, command=self.start_calculation,
                    onvalue=True, offvalue=False).place(relx=.05, rely=.3, anchor="w")

        self.lab_info = StringVar()
        self.lab_info.set('Start')
        Message(self.window, textvariable=self.lab_info, bg="white", width=450).place(relx=.05, rely=.4, anchor="nw")

        self.window.mainloop()

    def select_file(self):
        self.file_path.config(state=NORMAL)
        self.file_path.delete(0, END)
        file_name = filedialog.askopenfilename(title='Select row data', filetypes=[("CSV", ".csv"), ('All Files', '*')])
        self.file_path.insert(0, file_name)
        self.file_path.config(state=DISABLED)

        self.start_calculation()

    def start_calculation(self):
        file_name = self.file_path.get()
        if len(file_name) == 0:
            return

        data = load_data(file_name)
        data = np.array(data, np.float)
        x = data[:, 0:-1]
        y = data[:, -1]

        x_n, y_n = raw_data_to_normal_equation(x, y, self.const_item.get())
        # print(x_n)
        # print(y_n)

        # Singular matrix check
        if np.linalg.cond(x_n) > 1/sys.float_info.epsilon:
            self.lab_info.set("Singular matrix, raw data may not sufficient!")
            return

        res = np.linalg.solve(x_n, y_n)
        self.lab_info.set(res)


if __name__ == "__main__":
    # a = np.array([[1, 2, 3], [1, 1, 2], [2, 1, 4]])
    # b = np.array([14, 9, 16])
    # x = np.linalg.solve(a, b)
    # print(x)

    # A = np.array([[6, 5, 13], [5, 6, 12], [13, 12, 29]])
    # B = np.array([55, 53, 124])
    # x = np.linalg.solve(A, B)
    # print(x)

    w = MyWindow()
