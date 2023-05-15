import pygame
from dataclasses import dataclass

from .node import VisualNode

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

class GraphTest:
    def __init__(self, surface, font):
        self.nodes: dict[GraphNode, list[list[GraphNode, int]]] = {}
        self.surface: pygame.Surface = surface
        self.font: pygame.font.Font = font
        self.idx = 0
        self.prev_node = None

    def add_node(self, node: GraphNode):
        if node in self.nodes:
            raise ValueError("Node already exists")

        self.nodes[node] = []
        self.idx += 1

    def add_edge(self, node1: GraphNode, node2: GraphNode, weight: int = 0):
        if node1 not in self.nodes or node2 not in self.nodes:
            raise ValueError("Node does not exist")

        if node1 in self.nodes[node2]:
            return

        if node2 in self.nodes[node1]:
            return

        self.nodes[node1].append(node2)
        self.nodes[node2].append(node1)


    def remove_edge(self, node1: GraphNode, node2: GraphNode):
        if node1 not in self.nodes or node2 not in self.nodes:
            raise ValueError("Node does not exist")

        # only need to check one node, as the graph is undirected
        if node2 not in self.nodes[node1]:
            return

        self.nodes[node1].remove(node2)
        self.nodes[node2].remove(node1)


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
                        return "dijkstra"
                    case "exit":
                        return "exit"

    def draw_nodes_edges(self):
        node_list = []

        # draw edges first
        for node in self.nodes:
            node_list.append(node)
            for edge in self.nodes[node]:
                pygame.draw.line(self.surface, BLACK, (node.x, node.y), (edge.x, edge.y), 2)

        for node in node_list:
            node.shape.draw(self.surface)
            node.shape.draw_text(self.surface, node.value, self.font, BLACK)

    def open_input_menu(self):
        # when user clicks dijkstra button
        # ask from which node to start and end
        # then call dijkstra function
        rect1 = Rectangle((10, 10), BLACK, 150, 40)
        rect2 = Rectangle((170, 10), BLACK, 150, 40)
        rect3 = Rectangle((330, 10), BLACK, 70, 40)

        while True:
            for event in pygame.event.get():
                pass
            self.surface.fill(BLUE)
            rect1.draw(self.surface, width=2)
            rect2.draw(self.surface, width=2)
            rect3.draw(self.surface, width=2)
            rect1.draw_text(self.surface, "Start Node", self.font, BLACK)
            rect2.draw_text(self.surface, "End Node", self.font, BLACK)
            rect3.draw_text(self.surface, "Done", self.font, BLACK)

            pygame.display.update()



    def dijkstra_vis(self, start_node: GraphNode, end_node: GraphNode):
        pass


    def handle_window_input(self, current_value):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    current_value = current_value[:-1]
                elif event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                    return current_value
                elif event.unicode.isdigit():
                    current_value += event.unicode
        return current_value

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
        elif btn_res == "dijkstra":
            self.open_input_menu()
            return

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







