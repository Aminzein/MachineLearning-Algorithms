# coding: utf-8
import numpy as np
def calc_no_loop(new_points, points):
    new_shp = new_points.shape
    shp = points.shape
    return  np.sum((new_points.reshape((new_shp[0] , -1 , new_shp[1])) - points.reshape((-1,shp[0],shp[1])))**2 ,axis=2)
