import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as cm
from scipy.spatial import distance

#input parameters
max_map_size = 100 
max_iterations= 50000
max_vertex_dist = 1

vertex_explored = 0
vertex_discarded = 0
vertex_aprooved = 0

initial_location = (50,50)

#Generate Randon Points

def rand_pt():
    x = np.random.randint(low=0, high=max_map_size)
    y = np.random.randint(low=0, high=max_map_size)
    global vertex_explored
    vertex_explored += 1
    return (x,y)

#find nearest vertex

def nearest_vertex(explored_point):
    
    dist_list = distance.cdist(point_list,explored_point, 'euclidean')
    dist_list = dist_list.tolist() 
    shortest_distance = min(dist_list)
    index_of_mindist = dist_list.index(min(dist_list))
    shortest_point = point_list[index_of_mindist]
    if float(shortest_distance[0]) <= max_vertex_dist:
        return shortest_point
    else:
        return 1000


#list of points generated
point_list=[initial_location]

#plot initial

plt.scatter(initial_location[0],initial_location[1], c='#ff0e16', alpha=0.5)

#plot subsequent

for i in range(max_iterations):
    point = rand_pt()
    near_point = nearest_vertex([point])
    if near_point == 1000:
        vertex_discarded += 1
    else:
        vertex_aprooved += 1
        point_list.append(point)
        x_coordinates = [near_point[0], point[0]]
        y_coordinates = [near_point[1], point[1]]
        #print(near_point, point)
        plt.scatter(point[0],point[1], c='#ff7f0e', alpha=0.5)
        plt.plot(x_coordinates, y_coordinates)
        plt.draw()

print("initial location: " + str(initial_location))
print("vertex explored: " + str(vertex_explored))
print("vertex aprooved: " + str(vertex_aprooved))
print("vertex discarded: " + str(vertex_discarded))

#print(point_list)
plt.show()