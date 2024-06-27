import math

# tuple of coordinates	
point1 = (3,4)
point2 = (6,8) 
point3 = (12,16)

points = [point1,point2,point3] # list of points	

def euclideanDistance(point1,point2): # function to calculate the distance between two points
    return math.sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)

distances = [] # list of distances	
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distances.append(euclideanDistance(points[i], points[j]))
    
min_distance = min(distances) # find the minimum distance

print(distances) # print the distances
print(min_distance) # print the minimum distance

# Output: [5.0, 15.0, 8.0]