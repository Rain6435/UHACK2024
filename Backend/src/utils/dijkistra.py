
# TODO: rajouter l'age en consideration

class Graph():
 
    def __init__(self, potholes, calc_dist):
        self.distance_func = calc_dist
        self.potholes = potholes

 
    # A utility function to find the vertex with
    # minimum distance value, from the set of potholes
    # not yet included in shortest path tree
    def minDistance(self, sptSet):
        dist = populate_distance_matrix(self.V, self.distance_func)
        # Initialize minimum distance for next node
        min = 1e7
 
        # Search not nearest vertex not in the
        # shortest path tree
        for v in range(self.potholes):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v
 
        return min_index

    def nearest_neighbor(self):
        # Start from the first vertex in the graph
        if self.potholes == []:
            return []
        current_vertex = self.potholes[0]
        path = [current_vertex]

        # Visit each vertex exactly once
        while len(path) < len(self.potholes):
            # Find the nearest neighbor that has not been visited
            nearest_vertex = None
            min_weight = float('inf')
            for neighbor in self.potholes:
                weight = self.distance_func(current_vertex, neighbor)
                if neighbor not in path and weight < min_weight:
                    nearest_vertex = neighbor
                    min_weight = weight
            
            # Move to the nearest neighbor
            path.append(nearest_vertex)
            current_vertex = nearest_vertex


        return path
 


def populate_distance_matrix(potholes_list, distance_func):
    n = len(potholes_list)
    distance_matrix = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(i+1, n):
            distance = distance_func(potholes_list[i], potholes_list[j], use_age=True)
            distance_matrix[i][j] = distance
            distance_matrix[j][i] = distance

    return distance_matrix


def join_6_paths(calculate_distance, path_1, path_2, path_3, path_4, path_5, path_6):
    '''
    Finds the best way to join these 6 paths, this means from the last point of
    path 1, is it better to connect to 1st or last point of path 2? The closest will
    be chosen
    '''

    final_path = path_1

    # Adding path_2
    if path_2:
        if not final_path:
            final_path = path_2
        elif calculate_distance(final_path[-1], path_2[0]) <= calculate_distance(final_path[-1], path_2[-1]):
            final_path = final_path + path_2
        else:
            final_path = final_path + path_2[::-1]
    
    # Adding path_3
    if path_3:
        if not final_path:
            final_path = path_3
        if calculate_distance(final_path[-1], path_3[0]) <= calculate_distance(final_path[-1], path_3[-1]):
            final_path = final_path + path_3
        else:
            final_path = final_path + path_3[::-1]
    
    # Adding path_4
    if path_4:
        if not final_path:
            final_path = path_4
        if calculate_distance(final_path[-1], path_4[0]) <= calculate_distance(final_path[-1], path_4[-1]):
            final_path = final_path + path_4
        else:
            final_path = final_path + path_4[::-1]
    
    # Adding path_5
    if path_5:
        if not final_path:
            final_path = path_5
        if calculate_distance(final_path[-1], path_5[0]) <= calculate_distance(final_path[-1], path_5[-1]):
            final_path = final_path + path_5
        else:
            final_path = final_path + path_5[::-1]
    
    # Adding path_6
    if path_6:
        if not final_path:
            final_path = path_6
        if calculate_distance(final_path[-1], path_6[0]) <= calculate_distance(final_path[-1], path_6[-1]):
            final_path = final_path + path_6
        else:
            final_path = final_path + path_6[::-1]


    return final_path


def dijkistra_magic(sorted_potholes, calculate_distance):
    '''
    Function that splits the potholes in the 6 subgroups:
        1 half for dangerous -> main, collector, local
        1 half for non-dangerous -> main, collector, local
    
        Then finds the 6 optimal paths
    '''
    path_dangerous_main             = sorted_potholes["dangerous"]["main"]          # path 1
    path_dangerous_collector        = sorted_potholes["dangerous"]["collector"]     # path 2
    path_dangerous_local            = sorted_potholes["dangerous"]["local"]         # path 3
    path_non_dangerous_main         = sorted_potholes["non-dangerous"]["main"]      # path 4
    path_non_dangerous_collector    = sorted_potholes["non-dangerous"]["collector"] # path 5
    path_non_dangerous_local        = sorted_potholes["non-dangerous"]["local"]     # path 6

    best_path_1 = Graph(path_dangerous_main, calculate_distance).nearest_neighbor()
    best_path_2 = Graph(path_dangerous_collector, calculate_distance).nearest_neighbor()
    best_path_3 = Graph(path_dangerous_local, calculate_distance).nearest_neighbor()
    best_path_4 = Graph(path_non_dangerous_main, calculate_distance).nearest_neighbor()
    best_path_5 = Graph(path_non_dangerous_collector, calculate_distance).nearest_neighbor()
    best_path_6 = Graph(path_non_dangerous_local, calculate_distance).nearest_neighbor()

    return join_6_paths(calculate_distance, best_path_1, best_path_2, best_path_3, best_path_4, best_path_5, best_path_6)

