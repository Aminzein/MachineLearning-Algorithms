# coding: utf-8
import numpy as np
def calc_one_loop(new_points, points):
    m, n = len(new_points), len(points)    
    d = np.zeros((m, n))
    for i in range(m):
        d[i] = np.sum((new_points[i] - points) ** 2 , axis=1)
    return d
