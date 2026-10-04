import os
import numpy as np

inputFile = 'input.csv'
if not os.path.exists(inputFile):
    print('Cannot find ' + inputFile + '.')
    quit()

input = open(inputFile, 'r')

x = []
y = []
points = []

# Read each line of the input file.
# Storing the x-coordinates into x.
# Storing the y-coordinates into y.
line = input.readline()
index = 0
while line:
    coordinates = line.split(',')
    x.append(float(coordinates[0]))
    y.append(float(coordinates[1]))
    points.append((float(coordinates[0]), float(coordinates[1]), index))
    index += 1
    line = input.readline()

input.close()


def cross_product(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p2[1]) - (p2[1] - p1[1]) * (p3[0] - p2[0])


def convex_hull(points):
    if len(points) <= 1:
        return points

    points.sort()

    def build_half(points):
        hull = []
        for p in points:
            while len(hull) >= 2 and cross_product(hull[-2], hull[-1], p) <= 0:
                hull.pop()
            hull.append(p)
        return hull

    lower = build_half(points)
    upper = build_half(reversed(points))

    # put in counterclockwise order
    full_hull = lower[:-1] + upper[:-1]
    centroid = np.mean(np.array([(p[0], p[1]) for p in full_hull]), axis=0)
    full_hull.sort(key=lambda p: np.arctan2(p[1] - centroid[1], p[0] - centroid[0]))

    return full_hull


hull_points = convex_hull(points)
hull_indices = [p[2] for p in hull_points]

outputFile = 'output.txt'
out = open(outputFile, 'w')
for index in hull_indices:
    out.write("{}\n".format(index))
out.close()
