from .node import Node


class GNode(Node):

    def __init__(self, data=None):
        super().__init__(data)


class Graph:

    def __init__(self):
        self.graph_dict = {}

    def add_vertex(self, val):
        a_node = GNode(val)
        if a_node not in self.graph_dict:
            self.graph_dict[a_node] = []

    def add_edge(self, val1, val2):
        a_node = GNode(val1)
        b_node = GNode(val2)
        if a_node in self.graph_dict and b_node in self.graph_dict:
            self.graph_dict[a_node].append(b_node)
            self.graph_dict[b_node].append(a_node)
        else:
            raise ValueError("Both vertices must be in the graph.")

    def __str__(self):
        result = ""
        for vertex in self.graph_dict:
            result += f"{vertex.data}: "
            adjacent_nodes = [node.data for node in self.graph_dict[vertex]]
            result += ", ".join(adjacent_nodes)
            result += "\n"
        return result
