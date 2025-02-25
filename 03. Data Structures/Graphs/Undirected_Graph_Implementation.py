"""
Implements an undirected graph using an adjacency list.

Key points:
1. Each node is stored as a key in a dictionary (`adjacency_list`).
2. The dictionary value is a list of neighboring nodes.
3. The graph tracks the total number of nodes (`number_of_nodes`).
"""


class Graph:
    def __init__(self):
        """
        Constructor initializes an empty adjacency list (a dictionary)
        and a node count of zero.
        """
        self.number_of_nodes = 0
        self.adjacency_list = {}

    def insert_node(self, data):
        """
        Adds a new node to the adjacency list as a key 
        with an empty list (no edges yet).
        Also increments the total number of nodes by 1.
        """
        if data not in self.adjacency_list:
            self.adjacency_list[data] = []
            self.number_of_nodes += 1

    def insert_edge(self, vertex1, vertex2):
        """
        Adds an undirected edge between vertex1 and vertex2.
        (Adds vertex2 to the list of vertex1's neighbors and vice versa.)

        If vertex2 is already in vertex1's adjacency list, 
        it indicates that the edge already exists.
        """
        if vertex2 not in self.adjacency_list[vertex1]:
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
        else:
            return "Edge already exists"

    def show_connections(self):
        """
        Prints each node in the graph along with the
        nodes it is directly connected to.
        """
        for node in self.adjacency_list:
            print(f"{node} -->> {' '.join(map(str, self.adjacency_list[node]))}")


# Example usage:
my_graph = Graph()
my_graph.insert_node(1)
my_graph.insert_node(2)
my_graph.insert_node(3)
my_graph.insert_edge(1, 2)
my_graph.insert_edge(1, 3)
my_graph.insert_edge(2, 3)
my_graph.show_connections()  # Displays each node's neighbors

"""
Expected output:
1 -->> 2 3
2 -->> 1 3
3 -->> 1 2
"""

print(my_graph.adjacency_list)  # {1: [2, 3], 2: [1, 3], 3: [1, 2]}
print(my_graph.number_of_nodes)  # 3
