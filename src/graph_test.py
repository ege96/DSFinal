import pygame
from dataclasses import dataclass

from .node import VisualNode

from .COLORS import *

from .shapes import Rectangle, Circle


class GraphNode(VisualNode):
    def __init__(self, value, x: int, y: int, shape: Rectangle | Circle):
        super().__init__(value, shape)
        self.x: int = x
        self.y: int = y
        self.radius: int = 30


@dataclass(order=True)
class GraphEdge:
    node1: GraphNode
    node2: GraphNode
    weight: int = 0

    def __eq__(self, other):
        if isinstance(other, GraphEdge):
            return (self.node1 == other.node1 and self.node2 == other.node2) or (
                    self.node1 == other.node2 and self.node2 == other.node1)
        return False

    def __hash__(self):
        return hash((self.node1, self.node2))

    def draw(self, surface, color=BLACK, width=2):
        pygame.draw.line(surface, color, (self.node1.x, self.node1.y),
                         (self.node2.x, self.node2.y), width)


class Graph:
    def __init__(self, surface, font):
        self.nodes: dict[GraphNode, list[GraphEdge]] = {}
        self.surface: pygame.Surface = surface
        self.font: pygame.font.Font = font

    def add_node(self, node: GraphNode):
        if node in self.nodes:
            raise ValueError("Node already exists")

        self.nodes[node] = []

    def add_edge(self, node1: GraphNode, node2: GraphNode, weight: int = 0):
        if node1 not in self.nodes or node2 not in self.nodes:
            raise ValueError("Node does not exist")

        e1 = GraphEdge(node1, node2, weight)

        if e1 in self.nodes[node1]:
            return

        self.nodes[node1].append(e1)

    def remove_edge(self, node1: GraphNode, node2: GraphNode):
        if node1 not in self.nodes or node2 not in self.nodes:
            raise ValueError("Node does not exist")

        e1 = GraphEdge(node1, node2)

        if e1 not in self.nodes[node1]:
            return

        self.nodes[node1].remove(e1)

    def remove_node(self, node: GraphNode):
        if node not in self.nodes:
            raise ValueError("Node does not exist")

        for n in self.nodes:
            self.remove_edge(n, node)

        del self.nodes[node]

    def setup(self):
        self.djikstra_btn = Rectangle((10, 10), BLACK, 150, 40)
        self.djikstra_btn.draw_text(self.surface, "Dijkstra", self.font, BLACK)

        self.exit_btn = Rectangle((170, 10), BLACK, 70, 40)
        self.exit_btn.draw_text(self.surface, "Exit", self.font, BLACK)

        self.btns = {"dijkstra": self.djikstra_btn, "exit": self.exit_btn}

    def _buttonMenu(self, event):
        for btn in self.btns:
            btn_obj = self.btns[btn]
            btn_obj.draw(self.surface, width=2)
            btn_obj.draw_text(self.surface, btn.capitalize(), self.font, BLACK)

            if btn_obj.handle_event(event):
                match btn:
                    case "dijkstra":
                        self.dijkstra()
                    case "exit":
                        return "exit"

    def draw_nodes_edges(self):
        for node in self.nodes:
            node.shape.draw(self.surface)
            node.shape.draw_text(self.surface, node.value, self.font, BLACK)

            for edge in self.nodes[node]:
                edge.draw(self.surface)

    def open_input_menu(self):
        # when user clicks dijkstra button
        # ask from which node to start and end
        # then call dijkstra function
        pass

    def dijkstra(self):
        pass

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for node in self.nodes:
                    if node.shape.handle_event(event):
                        print("Node clicked")

        return

    def visualize(self):
        self.setup()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or self._visualize(event) == "exit":
                    return "exit"

    def _visualize(self, event):
        self.surface.fill(BLUE)

        if self._buttonMenu(event) == "exit":
            return "exit"

        self.draw_nodes_edges()







