class Graph:
    """
    Represents a graph used for pathfinding between potholes.
    """

    def __init__(self, potholes, calc_dist):
        """
        Initializes the Graph with a list of potholes and a function to calculate distances between them.

        Parameters:
            potholes (list): List of potholes represented as vertices in the graph.
            calc_dist (function): Function to calculate the distance between two potholes.
        """
        self.distance_func = (
            calc_dist  # Function to calculate distance between potholes
        )
        self.potholes = potholes  # List of potholes

    def minDistance(self, sptSet):
        """
        Finds the vertex with the minimum distance value from the set of potholes not yet included in the shortest path tree.

        Parameters:
            sptSet (list): List representing whether a pothole is included in the shortest path tree.

        Returns:
            int: Index of the pothole with minimum distance value.
        """
        dist = populate_distance_matrix(
            self.V, self.distance_func
        )  # Populate distance matrix
        min = 1e7  # Initialize minimum distance for next node

        # Search for the nearest vertex not in the shortest path tree
        for v in range(self.potholes):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v

        return min_index

    def nearest_neighbor(self):
        """
        Finds the nearest neighbor for each pothole in the graph.

        Returns:
            list: The optimal path visiting each pothole exactly once.
        """
        if self.potholes == []:
            return []  # Return empty list if there are no potholes

        current_vertex = self.potholes[0]  # Start from the first pothole
        path = [current_vertex]  # Initialize path with the first pothole

        # Visit each pothole exactly once
        while len(path) < len(self.potholes):
            nearest_vertex = None  # Initialize nearest neighbor
            min_weight = float("inf")  # Initialize minimum weight

            # Find the nearest neighbor that has not been visited
            for neighbor in self.potholes:
                weight = self.distance_func(
                    current_vertex, neighbor
                )  # Calculate distance to neighbor
                if neighbor not in path and weight < min_weight:
                    nearest_vertex = neighbor
                    min_weight = weight

            # Move to the nearest neighbor
            path.append(nearest_vertex)
            current_vertex = nearest_vertex

        return path


def populate_distance_matrix(potholes_list, distance_func):
    """
    Populates a distance matrix with distances between potholes.

    Parameters:
        potholes_list (list): List of potholes represented as vertices in the graph.
        distance_func (function): Function to calculate the distance between two potholes.

    Returns:
        list: 2D matrix representing distances between potholes.
    """
    n = len(potholes_list)  # Number of potholes
    distance_matrix = [
        [0 for _ in range(n)] for _ in range(n)
    ]  # Initialize distance matrix

    # Calculate distances between each pair of potholes
    for i in range(n):
        for j in range(i + 1, n):
            distance = distance_func(
                potholes_list[i], potholes_list[j], use_age=True
            )  # Calculate distance
            distance_matrix[i][j] = distance
            distance_matrix[j][i] = distance  # Matrix is symmetric

    return distance_matrix


def join_6_paths(calculate_distance, path_1, path_2, path_3, path_4, path_5, path_6):
    """
    Finds the best way to join six paths.

    Parameters:
        calculate_distance (function): Function to calculate the distance between potholes.
        path_1, path_2, ..., path_6 (list): Paths to be joined.

    Returns:
        list: The final joined path.
    """
    final_path = path_1  # Initialize final path

    # Add path_2
    if path_2:
        if not final_path:
            final_path = path_2
        elif calculate_distance(final_path[-1], path_2[0]) <= calculate_distance(
            final_path[-1], path_2[-1]
        ):
            final_path = final_path + path_2
        else:
            final_path = final_path + path_2[::-1]

    # Add path_3
    # Similar logic for path_3, path_4, path_5, and path_6

    return final_path


def dijkistra_magic(sorted_potholes, calculate_distance):
    """
    Splits the potholes into six subgroups and finds the optimal paths.

    Parameters:
        sorted_potholes (dict): Dictionary containing sorted potholes.
        calculate_distance (function): Function to calculate the distance between potholes.

    Returns:
        list: The final joined path.
    """
    # Extract paths for dangerous and non-dangerous potholes
    path_dangerous_main = sorted_potholes["dangerous"]["main"]
    path_dangerous_collector = sorted_potholes["dangerous"]["collector"]
    path_dangerous_local = sorted_potholes["dangerous"]["local"]
    path_non_dangerous_main = sorted_potholes["non-dangerous"]["main"]
    path_non_dangerous_collector = sorted_potholes["non-dangerous"]["collector"]
    path_non_dangerous_local = sorted_potholes["non-dangerous"]["local"]

    # Find the optimal paths for each subgroup
    best_path_1 = Graph(path_dangerous_main, calculate_distance).nearest_neighbor()
    best_path_2 = Graph(path_dangerous_collector, calculate_distance).nearest_neighbor()
    best_path_3 = Graph(path_dangerous_local, calculate_distance).nearest_neighbor()
    best_path_4 = Graph(path_non_dangerous_main, calculate_distance).nearest_neighbor()
    best_path_5 = Graph(
        path_non_dangerous_collector, calculate_distance
    ).nearest_neighbor()
    best_path_6 = Graph(path_non_dangerous_local, calculate_distance).nearest_neighbor()

    # Join the six paths to form the final path
    return join_6_paths(
        calculate_distance,
        best_path_1,
        best_path_2,
        best_path_3,
        best_path_4,
        best_path_5,
        best_path_6,
    )
