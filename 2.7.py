import matplotlib.pyplot as plt
import numpy as np
import scipy.interpolate as interp
import scipy.optimize as opt
import math
import shapely.geometry

global CONSTANTS_RADIUS_OF_EARTH
CONSTANTS_RADIUS_OF_EARTH = 6371000

x = [25.310672, 25.310742, 25.310930, 25.311296, 25.311489, 25.311996, 25.312010, 25.312132, 25.312188, 25.312148,
     25.313108, 25.313110, 25.313646,
     25.313585, 25.313426, 25.313390, 25.313552, 25.313420, 25.312863, 25.312911, 25.312842, 25.312864, 25.312953,
     25.312418, 25.310994,
     25.310844, 25.310576]

y = [103.455760, 103.455722, 103.460080, 103.460284, 103.460352, 103.460518, 103.460560, 103.460622, 103.460586,
     103.460759,
     103.460782, 103.460869, 103.460920, 103.461655, 103.461614, 103.461814, 103.461850, 103.462329, 103.461891,
     103.461712,
     103.461558, 103.461358, 103.461299, 103.461108, 103.460608, 103.460462, 103.460162]


def GPStoXY(lat, lon, ref_lat, ref_lon):
    # input GPS and Reference GPS in degrees
    # output XY in meters (m) X:North Y:East
    lat_rad = math.radians(lat)
    lon_rad = math.radians(lon)
    ref_lat_rad = math.radians(ref_lat)
    ref_lon_rad = math.radians(ref_lon)
    sin_lat = math.sin(lat_rad)
    cos_lat = math.cos(lat_rad)
    ref_sin_lat = math.sin(ref_lat_rad)
    ref_cos_lat = math.cos(ref_lat_rad)
    cos_d_lon = math.cos(lon_rad - ref_lon_rad)
    arg = np.clip(ref_sin_lat * sin_lat + ref_cos_lat * cos_lat * cos_d_lon, -1.0, 1.0)
    c = math.acos(arg)
    k = 1.0
    if abs(c) > 0:
        k = (c / math.sin(c))
    x = float(k * (ref_cos_lat * sin_lat - ref_sin_lat * cos_lat * cos_d_lon) * CONSTANTS_RADIUS_OF_EARTH)
    y = float(k * cos_lat * math.sin(lon_rad - ref_lon_rad) * CONSTANTS_RADIUS_OF_EARTH)
    return x, y


ref_x = x[0]
ref_y = y[0]
for i in range(len(x)):
    x[i], y[i] = GPStoXY(x[i], y[i], ref_x, ref_y)

border = 0
for i in range(len(x) - 1):
    border = border + np.sqrt((x[i + 1] - x[i]) ** 2 + (y[i + 1] - y[i]) ** 2)
print(f'边界长度为{border}')

x_max = max(x)
y_max = max(y)
x_min = min(x)
y_min = min(y)

x = np.array(x).reshape(27, 1)
y = np.array(y).reshape(27, 1)
point = np.concatenate([x, y], axis=1)
# print(point)

poly = shapely.geometry.Polygon(point)
x, y = poly.exterior.xy
plt.plot(x, y)
ref = shapely.geometry.Polygon([[x_min, y_min], [x_min, y_max], [x_max, y_max], [x_max, y_min]])
x1, y1 = ref.exterior.xy
plt.plot(x1, y1)
plt.show()


def generate_point(n, x_max, y_max, x_min, y_min):
    p = np.zeros([n, 2])
    p[:, 0] = np.random.uniform(x_min, x_max, [n, 1]).reshape([n, ])
    p[:, 1] = np.random.uniform(y_min, y_max, [n, 1]).reshape([n, ])
    return p


n = 100000
sum = 0
Points = generate_point(n, x_max, y_max, x_min, y_min)
for i in range(n):
    x = Points[i, 0]
    y = Points[i, 1]
    p = shapely.geometry.Point(x, y)
    if poly.contains(p):
        sum = sum + 1
S = (x_max-x_min) * (y_max-y_min)
print(f'矩形框面积为{S}')
print(f'共{sum}个点落在目标区域内')
print(f'面积为{sum/n*S}')