# coding: utf-8
import numpy as np
def calc_two_loops(new_points, points):
    m, n = len(new_points), len(points)
    d = np.zeros((m, n))
    for i in range(m):
        for j in range(n):
            d[i, j] = np.sum((new_points[i] - points[j]) ** 2)
    return d
