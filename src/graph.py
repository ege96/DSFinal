import pygame
import random
import time
import math

from .node import Node

from .COLORS import BLUE, BROWN, BLACK

from .shapes import Shape, Rectangle, Circle


def get_clicked_node(nodes, x, y):
    for node in nodes:
        if math.sqrt((node.x - x)**2 + (node.y - y)**2) <= node.radius:
            return node
    return None


class Node:

    def __init__(self, x, y, index):
        self.x = x
        self.y = y
        self.index = index
        self.radius = 30

    def draw(self, surface, font):
        pygame.draw.circle(surface, BROWN, (self.x, self.y), self.radius)
        node_text = font.render(str(self.index), True, BLACK)
        text_rect = node_text.get_rect(center=(self.x, self.y))
        surface.blit(node_text, text_rect)


# Define the Edge class
class Edge:

    def __init__(self):
        self.node1 = None
        self.node2 = None

    def set_nodes(self, node1, node2):
        self.node1 = node1
        self.node2 = node2

    def draw(self, surface):
        pygame.draw.line(surface, BLACK, (self.node1.x, self.node1.y),
                         (self.node2.x, self.node2.y), 2)


# Define the Graph class
class Graph:

    def __init__(self, surface, font):
        self.nodes = []
        self.edges = []
        self.surface = surface
        self.font = font

    def add_node(self, node):
        self.nodes.append(node)
        # if len(self.nodes) > 1:
        #     # Add an edge between the new node and the previous node
        #     prev_node = self.nodes[-2]
        #     new_edge = Edge(prev_node, node)
        #     self.add_edge(new_edge)

    def add_edge(self, edge):
        self.edges.append(edge)

    def draw(self):
        for edge in self.edges:
            edge.draw(self.surface)
        for node in self.nodes:
            node.draw(self.surface, self.font)

    def visualize(self):
        self.surface.fill(BLUE)
        last_click_time = time.monotonic()

        running = True
        node_index = 1
        last_clicked_node = None

        while running:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    # Check the click timer
                    if time.monotonic() - last_click_time >= 0.1:
                        # Add a node at the clicked position
                        x, y = event.pos
                        node = Node(x, y, node_index)
                        self.add_node(node)
                        node_index += 1
                        # Reset the click timer
                        last_click_time = time.monotonic()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                    x, y = event.pos
                    clicked_node = get_clicked_node(self.nodes, x, y)
                    if clicked_node is not None:
                        if last_clicked_node is None:
                            last_clicked_node = clicked_node
                        else:
                            new_edge = Edge()
                            new_edge.set_nodes(last_clicked_node, clicked_node)
                            self.add_edge(new_edge)
                            last_clicked_node = None

            # Draw the graph
            self.surface.fill(BLUE)
            self.draw()

            # Update the display
            pygame.display.flip()

        # Quit pygame
        pygame.quit()
