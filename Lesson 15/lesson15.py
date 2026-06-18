import matplotlib.pyplot as plt   
import numpy as np               

print("**1. Basic Plotting**")
x = np.linspace(-10, 10, 100)   
y = x**2 - 4*x + 4
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Plot of f(x) = x^2 - 4x + 4")
plt.show()

plt.savefig("/home/zhav3n/Desktop/homework/Lesson 15/task1.png")

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-np.pi, np.pi, 100)   # shared x values for both functions

y1 = np.tan(x)
y2 = x / 3

plt.plot(x, y1, color="blue", linestyle="-", label="tan(x)")
plt.plot(x, y2, color="red", linestyle="--", label="x/3")

plt.legend()
plt.savefig("/home/zhav3n/Desktop/homework/Lesson 15/practice2.png")