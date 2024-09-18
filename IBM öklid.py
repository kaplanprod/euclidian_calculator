import math

# List that includes points.
points = [(1, 2), (3, 5), (3, 4), (0, 6), (6, 8)]


# Euclidian Calculating Function.
def euclidianDistance(point1, point2):
    x1,y1 = point1
    x2,y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


# Distance List
distances = []

# Taking the points in the list and calling the function.
for i in range(len(points)):
    for j in range( i + 1, len(points)):
        distance = euclidianDistance(points[i],points[j])
        distances.append(distance)

# Taking the minimum distance between points.
min_distance = min(distances)

print(distances)
print(min_distance)