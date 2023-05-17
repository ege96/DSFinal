import pygame
from dataclasses import dataclass

from .node import VisualNode
from .visualizer import BaseVisualizer

from .COLORS import *

from .shapes import Rectangle, Circle


@dataclass(order=True)
class GraphNode(VisualNode):
    def __init__(self, value, x: int, y: int, shape: Rectangle | Circle):
        super().__init__(value, shape)
        self.x: int = x
        self.y: int = y

    def __hash__(self):
        return hash((self.x, self.y))


class Graph(BaseVisualizer):
    def __init__(self, surface, font):
        super().__init__(surface, font)
        self.nodes: dict[GraphNode, list[list[GraphNode, int]]] = {}
        self.idx = 0
        self.prev_node = None

    def add_node(self, node: GraphNode):
        if node in self.nodes:
            raise ValueError("Node already exists")

        self.nodes[node] = []
        self.idx += 1

    def add_edge(self, node1: GraphNode, node2: GraphNode, weight: int = 0):
        if node1 not in self.nodes or node2 not in self.nodes:
            return

        if node1 in self.nodes[node2]:
            return

        if node2 in self.nodes[node1]:
            return

        self.nodes[node1].append([node2, weight])
        self.nodes[node2].append([node1, weight])

    def remove_edge(self, node1: GraphNode, node2: GraphNode):
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
        if node not in self.nodes:
            raise ValueError("Node does not exist")

        for n in self.nodes:
            print("removing edges")
            self.remove_edge(n, node)

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
                self.remove_node(node)

            elif button_clicked == "right":
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







