import matplotlib.pyplot as plt
import math

# Ask the user to input the points
x1 = float(input("Enter x-coordinate for point 1: "))
y1 = float(input("Enter y-coordinate for point 1: "))
x2 = float(input("Enter x-coordinate for point 2: "))
y2 = float(input("Enter y-coordinate for point 2: "))

# Calculate dx and dy
dx = x2 - x1
dy = y2 - y1

# Calculate the number of steps (rounded up to nearest integer)
steps = max(abs(dx), abs(dy))

# Calculate the increment values for each step
x_inc = dx / steps
y_inc = dy / steps

# Initialize the starting point
x, y = x1, y1

# Lists to store the points
points = [(round(x), round(y))]

# Calculate all points
for _ in range(math.ceil(steps)):
    x += x_inc
    y += y_inc
    points.append((round(x), round(y)))

# Separate the x and y coordinates for plotting
x_coords, y_coords = zip(*points)

# Plotting the points
plt.figure(figsize=(8, 6))
plt.plot(x_coords, y_coords, marker='o', color='b', linestyle='-')
plt.title('DDA Line Drawing Algorithm')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.xlim(min(x1, x2) - 1, max(x1, x2) + 1)
plt.ylim(min(y1, y2) - 1, max(y1, y2) + 1)
plt.xticks(range(math.floor(min(x1, x2)) - 1, math.ceil(max(x1, x2)) + 1))
plt.yticks(range(math.floor(min(y1, y2)) - 1, math.ceil(max(y1, y2)) + 1))
plt.gca().set_aspect('equal', adjustable='box')

# Annotating the points
for (x, y) in points:
    plt.text(x, y, f'({x},{y})', fontsize=12, verticalalignment='bottom')

plt.show()
