import matplotlib.pyplot as plt   
import numpy as np               

print("**1. Basic Plotting**")
x = np.linspace(-10, 10, 100)   
y = x**2 - 4*x + 4
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Plot of f(x) = x^2 - 4x + 4")
plt.savefig("/home/zhav3n/Desktop/homework/Lesson 15/task1.png")


print("\n**2. Sine and Cosine Plot**")
plt.figure()
x = np.linspace(0, 2*np.pi, 100)  
y1 = np.sin(x)
y2 = np.cos(x)
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x, y1, color="blue", linestyle="-", label="sin(x)", marker="o", markevery=10)
plt.plot(x, y2, color="red", linestyle="--", label="cos(x)", marker="s", markevery=10 )
plt.title("Plot of y1 = sin(x) & y2 = cos(x)")
plt.legend()
plt.savefig("/home/zhav3n/Desktop/homework/Lesson 15/task2.png")

print("\n**3. Subplots**")

fig, axes = plt.subplots(2, 2)  

x1 = np.linspace(-5, 5, 100)   
x2 = np.linspace(0, 5, 100)    

# Top-left: $ f(x) = x^3 $
axes[0][0].plot(x1, x1**3, color="blue")
axes[0][0].set_title("y = x^3")
axes[0][0].set_xlabel("x")
axes[0][0].set_ylabel("y")

#   - Top-right: $ f(x) = \sin(x) $
axes[0][1].plot(x1, np.sin(x1), color="red")
axes[0][1].set_title("y = sin(x)")
axes[0][1].set_xlabel("x")
axes[0][1].set_ylabel("y")

#   - Bottom-left: $ f(x) = e^x $
axes[1][0].plot(x1, np.exp(x1), color="green")
axes[1][0].set_title("y = e^x")
axes[1][0].set_xlabel("x")
axes[1][0].set_ylabel("y")

#   - Bottom-right: $ f(x) = \log(x+1) $ (for $ x \geq 0 $)
axes[1][1].plot(x2, np.log(x2+1), color="purple")
axes[1][1].set_title("y = log(x+1)")
axes[1][1].set_xlabel("x")
axes[1][1].set_ylabel("y")

plt.tight_layout()
plt.savefig("/home/zhav3n/Desktop/homework/Lesson 15/task3.png")

print("\n**4. Scatter Plot**")
plt.figure()
x = np.random.uniform(0, 10, 100)
y = np.random.uniform(0, 10, 100)

plt.scatter(x, y, color="green", marker="^", alpha=0.7)
plt.title("100 Random Points")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.savefig("/home/zhav3n/Desktop/homework/Lesson 15/task4.png")

print("\n**5. Histogram**")
plt.figure()

data = np.random.normal(loc=0, scale=1, size=1000)

plt.hist(data, bins=30, alpha=0.6, color="blue")
plt.title("Distribution of 1000 Random Values")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.savefig("/home/zhav3n/Desktop/homework/Lesson 15/task5.png")

print("\n**6. 3D Plotting**")

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.cos(X**2 + Y**2)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

surface = ax.plot_surface(X, Y, Z, cmap='viridis')
fig.colorbar(surface)

ax.set_title("f(x,y) = cos(x^2 + y^2)")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
plt.savefig("/home/zhav3n/Desktop/homework/Lesson 15/task6.png")

print("\n**7. Bar Chart**")       
plt.figure()
products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
sales = [200, 150, 250, 175, 225]

plt.bar(products, sales, color=["red", "blue", "green", "orange", "purple"])
plt.title("Products sales")
plt.xlabel("products")
plt.ylabel("sales")
plt.savefig("/home/zhav3n/Desktop/homework/Lesson 15/task7.png")

print("\n**8. Stacked Bar Chart**")
plt.figure()

periods = ["T1", "T2", "T3", "T4"]
category_A = np.array([10, 20, 15, 25])
category_B = np.array([8, 12, 18, 24])
category_C = np.array([5, 15, 10, 20])

plt.bar(periods, category_A, color="blue", label="Category A")
plt.bar(periods, category_B, color="orange", label="Category B", bottom=category_A)
plt.bar(periods, category_C, color="green", label="Category C", bottom=category_A + category_B)

plt.title("categories over time")
plt.xlabel("Time")
plt.ylabel("Count")
plt.legend()
plt.savefig("/home/zhav3n/Desktop/homework/Lesson 15/task8.png")