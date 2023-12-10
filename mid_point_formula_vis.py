import matplotlib
import matplotlib.pyplot as plt


def midpoint(x1, y1, x2, y2, m, n):
    """
    This function calculates the coordinates of a point dividing the line segment joining the points (x1, y1) and (x2, y2) internally, in the ratio m: n.

    Args:
      x1: x-coordinate of the first point.
      y1: y-coordinate of the first point.
      x2: x-coordinate of the second point.
      y2: y-coordinate of the second point.
      m: ratio of the distance from the first point to the dividing point.
      n: ratio of the distance from the dividing point to the second point.

    Returns:
      A tuple containing the x and y coordinates of the dividing point.
    """
    x = (x1 * n + x2 * m) / (m + n)
    y = (y1 * n + y2 * m) / (m + n)
    return (x, y)


# Example usage
# x1, y1 = 1, 2
# x2, y2 = 5, 6
# m, n = 2, 3
x1 = int(input("Enter the X-coordinate of point P: "))
y1 = int(input("Enter the Y-coordinate of point P: "))

x2 = int(input("Enter the X-coordinate of point Q: "))
y2 = int(input("Enter the Y-coordinate of point Q: "))

m = int(input("Enter the ratio m : "))
n = int(input("Enter the ratio n : "))

midpoint_x, midpoint_y = midpoint(x1, y1, x2, y2, m, n)

# Plot the points and the line segment
plt.plot([x1, x2], [y1, y2], "b-o", label="Line segment")

# Plot the dividing point
plt.plot(midpoint_x, midpoint_y, "r*", markersize=10, label="Dividing point")

# Label the points
plt.annotate(
    f"({x1}, {y1})", (x1, y1), textcoords="offset points", xytext=(0, 10), ha="center"
)
plt.annotate(
    f"({x2}, {y2})", (x2, y2), textcoords="offset points", xytext=(0, -10), ha="center"
)
plt.annotate(
    f"({midpoint_x:.2f}, {midpoint_y:.2f})",
    (midpoint_x, midpoint_y),
    textcoords="offset points",
    xytext=(0, 10),
    ha="center",
    color="red",
)

# Set labels and title
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Visualization of dividing point")

# Add legend
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
