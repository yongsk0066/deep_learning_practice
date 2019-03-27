
import numpy as np
import matplotlib.pyplot as plt

# def step_function(x):
#     return np.array(x>0, dtype=np.int)

# x = np.arange(-5.0, 5.0, 0.1)
# y = step_function(x)
#
# plt.plot(x, y)
# plt.ylim(-0.1, 1.1)
# plt.show()

# def sigmoid(x):
#     return 1 / (1 + np.exp(-x))
#
# x = np.array([-1.0, 1.0, 2.0])
# print(sigmoid(x))
# A = np.array([[1, 2], [3, 4]])
# A.shape
#
# a = np.sin(np.pi)
# a = round(a, 15)
# print(a)
x = 1073741824
i = 0
while True:

    print(x)
    print(i)
    i += 1
    x = x / 2
    if x == 1:
        break
