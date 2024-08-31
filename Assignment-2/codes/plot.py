import ctypes
import matplotlib.pyplot as plt

# Define a Point structure to match the C structure
class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_double), ("y", ctypes.c_double)]

# Load the shared library
lib = ctypes.CDLL('./midpoint.so')

# Define the argument and return types for the calculate_midpoint function
lib.calculate_midpoint.argtypes = [Point, Point]
lib.calculate_midpoint.restype = Point

# Function to calculate midpoint using the C function
def calculate_midpoint_py(p1, p2):
    return lib.calculate_midpoint(p1, p2)

# Coordinates of the parallelogram
points = [Point(3, 3), Point(6, 4), Point(8, 7), Point(5, 6)]

# Unpack coordinates for plotting
x_coords = [p.x for p in points]
y_coords = [p.y for p in points]

# Plot the points
plt.scatter(x_coords, y_coords, label="Vertices")

# Connect points to form the parallelogram
plt.plot([points[0].x, points[1].x], [points[0].y, points[1].y], label="Side AB")
plt.plot([points[1].x, points[2].x], [points[1].y, points[2].y], label="Side BC")
plt.plot([points[2].x, points[3].x], [points[2].y, points[3].y], label="Side CD")
plt.plot([points[3].x, points[0].x], [points[3].y, points[0].y], label="Side DA")

# Calculate midpoints for diagonals using the C function
midpoint_1 = calculate_midpoint_py(points[0], points[2])
midpoint_2 = calculate_midpoint_py(points[1], points[3])

# Plot the intersection point
plt.scatter(midpoint_1.x, midpoint_1.y, color='red', label="Intersection")

# Draw both diagonals as dotted lines
plt.plot([points[0].x, points[2].x], [points[0].y, points[2].y], linestyle='dotted', label="Diagonal AC")
plt.plot([points[1].x, points[3].x], [points[1].y, points[3].y], linestyle='dotted', label="Diagonal BD")

# Add labels to points
labels = ['A (3, 3)', 'B (6, 4)', 'C (8, 7)', 'D (5, 6)']
for i, point in enumerate(points):
    plt.text(point.x + 0.1, point.y + 0.1, labels[i])

# Add labels to midpoints
plt.text(midpoint_1.x + 0.1, midpoint_1.y + 0.1, f"M ({midpoint_1.x},{midpoint_1.y})")

# Set labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Parallelogram')

# Add legend
plt.legend()

# Show the plot
plt.grid(True)
plt.show()

