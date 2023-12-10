# code v0.0.1
# BUGS - it create error when float data and char data is entered

import math
import matplotlib.pyplot as plt


def distance(x1, y1, x2, y2):
    """
    Calculates the distance between two points.

    Args:
        x1: The x-coordinate of the first point.
        y1: The y-coordinate of the first point.
        x2: The x-coordinate of the second point.
        y2: The y-coordinate of the second point.

    Returns:
        The distance between the two points.
    """
    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return dist


# Get input from the user
x1 = int(input("Enter the X-coordinate of point P: "))
y1 = int(input("Enter the Y-coordinate of point P: "))

x2 = int(input("Enter the X-coordinate of point Q: "))
y2 = int(input("Enter the Y-coordinate of point Q: "))

dist = distance(x1, y1, x2, y2)

# Create plot
fig, ax = plt.subplots()

# Plot the line
ax.plot([x1, x2], [y1, y2], color="blue", linewidth=2)

# Label the points
ax.text(x1, y1, f"P({x1},{y1})", fontsize=11, color="red")
ax.text(x2, y2, f"Q({x2},{y2})", fontsize=11, color="red")

# Label the distance
midpoint_x = (x1 + x2) / 2
midpoint_y = (y1 + y2) / 2
ax.text(midpoint_x, midpoint_y, f"{dist:.2f}", fontsize=11, ha="center", va="center")

# Set limits slightly higher than point coordinates
ax.set_xlim(min(x1, x2) - 1, max(x1, x2) + 1)
ax.set_ylim(min(y1, y2) - 1, max(y1, y2) + 1)

# Set labels
ax.set_xlabel("X")
ax.set_ylabel("Y")

# Set title
ax.set_title("Line with Labeled Length")

# Show plot
plt.show()
