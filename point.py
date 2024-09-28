# -*- coding: ascii -*-
# by mrfriot


class Point:
    def __init__(self, name: str, edges: tuple = ()):
        self.name = name
        self.edges = edges

    def set_edges(self, edges: tuple):
        self.edges = edges
