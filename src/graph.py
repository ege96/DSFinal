import pygame
from dataclasses import dataclass

from .node import VisualNode
from .visualizer import BaseVisualizer

from .COLORS import *

from .shapes import Rectangle, Circle


@dataclass(order=True)
class GraphNode(VisualNode):
    """GraphNode class, inherits from VisualNode

    Args:
        value (any): value of the node
        x (int): x coordinate of the node
        y (int): y coordinate of the node
        shape (Rectangle | Circle): shape of the node

    Attributes:
        x (int): x coordinate of the node
        y (int): y coordinate of the node
        shape (Rectangle | Circle): shape of the node
    """
    def __init__(self, value, x: int, y: int, shape: Rectangle | Circle):
        super().__init__(value, shape)
        self.x: int = x
        self.y: int = y

    def __hash__(self):
        """Hash function so that it can be used in dictionaries"""
        return hash((self.x, self.y))


class Graph(BaseVisualizer):
    """Graph class, inherits from BaseVisualizer

    Args:
        surface (pygame.Surface): surface to draw on
        font (pygame.font.Font): font to use for text

    Attributes:
        nodes (dict[GraphNode, list[list[GraphNode, int]]]): dictionary of nodes and their edges with weights

    """
    def __init__(self, surface, font):
        super().__init__(surface, font)
        self.nodes: dict[GraphNode, list[list[GraphNode, int]]] = {}
        self.idx = 0
        self.prev_node = None

    def add_node(self, node: GraphNode):
        """Add a node to the graph

        Args:
            node (GraphNode): node to add

        Raises:
            ValueError: if node already exists

        """
        if node in self.nodes:
            raise ValueError("Node already exists")

        self.nodes[node] = []
        self.idx += 1

    def add_edge(self, node1: GraphNode, node2: GraphNode, weight: int = 0):
        """Add an edge between two nodes

        If the edge already exists, it is not added

        Args:
            node1 (GraphNode): first node
            node2 (GraphNode): second node
            weight (int, optional): weight of the edge, defaults to 0

        """
        if node1 not in self.nodes or node2 not in self.nodes:
            return

        if [node1, weight] in self.nodes[node2]:
            return

        if [node2, weight] in self.nodes[node1]:
            return

        self.nodes[node1].append([node2, weight])
        self.nodes[node2].append([node1, weight])

    def remove_edge(self, node1: GraphNode, node2: GraphNode):
        """Remove an edge between two nodes

        Args:
            node1 (GraphNode): first node
            node2 (GraphNode): second node

        Raises:
            ValueError: if either node does not exist
        """

        if node1 not in self.nodes or node2 not in self.nodes:
            raise ValueError("Node does not exist")

        for nodes in self.nodes[node1]:
            if nodes[0] == node2:
                print("removing edge")
                self.nodes[node1].remove(nodes)
                break

        for nodes in self.nodes[node2]:
            if nodes[0] == node1:
                print("removing edge")
                self.nodes[node2].remove(nodes)
                break

    def remove_node(self, node: GraphNode):
        """Remove a node from the graph, along with all its incident edges

        Args:
            node (GraphNode): node to remove

        Raises:
            ValueError: if node does not exist

        """

        if node not in self.nodes:
            raise ValueError("Node does not exist")

        for n in self.nodes:
            # remove all edges incident to node
            print("removing edges")
            self.remove_edge(node, n)

        del self.nodes[node]

    def setup(self):
        btn_names = ["exit"]
        self.add_buttons(btn_names)

    def _buttonMenu(self, event):
        for btn in self.btns:
            btn_obj = self.btns[btn]
            btn_obj.draw(self.surface, width=2)
            btn_obj.draw_text(self.surface, btn.capitalize(), self.font, BLACK)

            if btn_obj.handle_event(event):
                match btn:
                    case "exit":
                        return "exit"

    def draw_nodes_edges(self):
        """Draw all nodes and edges on the surface"""
        node_list = []

        # draw edges first
        for node in self.nodes:
            node_list.append(node)
            for edge in self.nodes[node]:
                edge = edge[0]
                pygame.draw.line(self.surface, BLACK, (node.x, node.y), (edge.x, edge.y), 2)

        for node in node_list:
            node.shape.draw(self.surface)
            node.shape.draw_text(self.surface, node.value, self.font, BLACK)

    def handle_event(self, event):
        """Handle mouse events

        Args:
            event (pygame.event.Event): event to handle

        Returns:
            tuple[GraphNode, str]: node that was clicked and which mouse button was clicked

        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for node in self.nodes:
                    if node.shape.handle_event(event):
                        print("Node left clicked")
                        return node, "left"
                return None, "left"

            elif event.button == 3:
                for node in self.nodes:
                    if node.shape.handle_event(event):
                        print("Node right clicked")
                        return node, "right"
                return None, "right"

        return None, None

    def visualize(self):
        self.setup()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or self._visualize(event) == "exit":
                    return "exit"

    def _visualize(self, event):
        self.surface.fill(BLUE)

        btn_res = self._buttonMenu(event)
        if btn_res == "exit":
            return "exit"

        node, button_clicked = self.handle_event(event)

        if node is not None:
            if button_clicked == "left":
                # remove node if left-clicked
                self.remove_node(node)

            elif button_clicked == "right":
                # add edge if two nodes are successively right-clicked
                if self.prev_node is None:
                    self.prev_node = node
                else:
                    self.add_edge(self.prev_node, node)
                    self.prev_node = None

        else:
            if button_clicked == "left":
                # get mouse pos
                x, y = pygame.mouse.get_pos()
                node = GraphNode(str(self.idx), x, y, Circle((x, y), BROWN, 20))
                self.add_node(node)

        self.draw_nodes_edges()
        pygame.display.update()







