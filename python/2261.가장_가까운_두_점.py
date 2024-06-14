# closet pair 문제를 분할정복 알고리즘으로 풀이
import sys;rl=sys.stdin.readline
import math

n = int(rl())

coords = []
for _ in range(n):
    x, y = map(int,rl().split())
    coords.append((x, y))
coords_sort_x = sorted(coords,key=lambda x: x[0])
coords_sort_y = sorted(coords,key=lambda x: x[1])

def get_dist_square(a, b):
    x_a, y_a = a
    x_b, y_b = b
    
    return (x_a - x_b)**2 + (y_a - y_b)**2

def get_min_dist(coords):
    cnt = len(coords)
    min_dist = math.inf
    for i in range(cnt):
        for j in range(i+1,cnt):
            if i == j:
                continue
            dist = get_dist_square(coords[i], coords[j])
            min_dist = min(dist, min_dist)
    return min_dist

def divide_and_conquer(local_coords):
    cnt = len(local_coords)
    if cnt < 4:
        return get_min_dist(local_coords)
    mid = cnt // 2
    left_coords = local_coords[:mid]
    right_coords = local_coords[mid:]
    
    left_min_dist = divide_and_conquer(left_coords)
    right_min_dist = divide_and_conquer(right_coords)
    local_min_dist = min(left_min_dist, right_min_dist)
    
    coords_in_band_square = []
    x_mid, y_mid = local_coords[mid]
    for i in range(cnt):
        x_i, y_i = local_coords[i]
        if abs(x_mid - x_i) ** 2 < local_min_dist or abs(y_mid - y_i) ** 2 < local_min_dist:
            coords_in_band_square.append((x_i, y_i))
    coords_in_band_square.sort(key=lambda x: x[1])
    
    min_dist_in_band = local_min_dist
    
    for i in range(len(coords_in_band_square)):
        j = i + 1
        while j < len(coords_in_band_square) and coords_in_band_square[j][1] - coords_in_band_square[i][1] < local_min_dist:
            min_dist_in_band = min(min_dist_in_band, get_dist_square(coords_in_band_square[i], coords_in_band_square[j]))
            j += 1
    
    return min_dist_in_band

print(divide_and_conquer(coords_sort_x))