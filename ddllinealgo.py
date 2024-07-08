import matplotlib.pyplot as plt

# Given points
x1, y1 = 2, 3
x2, y2 = 10, 8

# Calculate dx and dy
dx = x2 - x1
dy = y2 - y1

# Calculate the number of steps
steps = max(abs(dx), abs(dy))

# Calculate the increment values for each step
x_inc = dx / steps
y_inc = dy / steps

# Initialize the starting point
x, y = x1, y1

# Lists to store the points
points = [(round(x), round(y))]

# Calculate all points
for _ in range(steps):
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
plt.xlim(0, 12)
plt.ylim(0, 10)
plt.xticks(range(0, 13))
plt.yticks(range(0, 11))
plt.gca().set_aspect('equal', adjustable='box')

# Annotating the points
for (x, y) in points:
    plt.text(x, y, f'({x},{y})', fontsize=12, verticalalignment='bottom')

plt.show()
