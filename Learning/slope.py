import math

# Given points
x1, y1 = 2, 2
x2, y2 = 6, 10

# Calculate slope
slope = (y2 - y1) / (x2 - x1)

# Calculate Euclidean distance
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Output the results
print(f"Slope between points ({x1}, {y1}) and ({x2}, {y2}) is: {slope}")
print(f"Euclidean distance between points ({x1}, {y1}) and ({x2}, {y2}) is: {distance:.2f}")
