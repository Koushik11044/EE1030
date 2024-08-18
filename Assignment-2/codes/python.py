import matplotlib.pyplot as plt

# Coordinates of the parallelogram
points = [(3, 3), (6, 4), (8, 7), (5, 6)]

# Unpack coordinates for plotting
x_coords, y_coords = zip(*points)

# Plot the points
plt.scatter(x_coords, y_coords, label="Vertices")

# Connect points to form the parallelogram
plt.plot([points[0][0], points[1][0]], [points[0][1], points[1][1]], label="Side AB")
plt.plot([points[1][0], points[2][0]], [points[1][1], points[2][1]], label="Side BC")
plt.plot([points[2][0], points[3][0]], [points[2][1], points[3][1]], label="Side CD")
plt.plot([points[3][0], points[0][0]], [points[3][1], points[0][1]], label="Side DA")

# Calculate midpoints for diagonals
midpoint_1 = ((points[0][0] + points[2][0]) / 2, (points[0][1] + points[2][1]) / 2)
midpoint_2 = ((points[1][0] + points[3][0]) / 2, (points[1][1] + points[3][1]) / 2)

# Plot the intersection point
plt.scatter(midpoint_1[0], midpoint_1[1], color='red', label="Intersection")

# Draw both diagonals as dotted lines
plt.plot([points[0][0], points[2][0]], [points[0][1], points[2][1]], linestyle='dotted', label="Diagonal AC")
plt.plot([points[1][0], points[3][0]], [points[1][1], points[3][1]], linestyle='dotted', label="Diagonal BD")

# Add labels to points
labels = ['A (3, 3)', 'B (6, 4)', 'C (8, 7)', 'D (5, 6)']
for i, (x, y) in enumerate(points):
    plt.text(x + 0.1, y + 0.1, labels[i])

# Set labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Parallelogram')

# Add legend
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
