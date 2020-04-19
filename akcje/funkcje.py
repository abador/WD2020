def move(point, vector):
    for key in point:
        point[key] += vector[key]