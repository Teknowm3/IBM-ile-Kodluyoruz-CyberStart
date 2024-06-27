def euclideanDistance(point1,point2):
    return ((point1[0] - point2[0]) **2 + (point1[1] - point2[1]) **2) **0.5

point1 = (1,2)
point2 = (3,4)
point3 = (5,8)

points = [point1,point2,point3] # list of points 

distances = [] # list of distances

for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distances.append(euclideanDistance(points[i], points[j]))

min_distance = distances[0]
for distance in distances: # find the minimum distance
    if distance < min_distance:
        min_distance = distance

print("Min mesafe: ", min_distance)

print("Öklid Mesafeleri:")
for distance in distances:
    print(distance)