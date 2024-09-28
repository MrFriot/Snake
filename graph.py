# -*- coding: ascii -*-
# by mrfriot


class Edge:
    def __init__(self, point_a_name: str, point_b_name: str):
        self.point_a = point_a_name
        self.point_b = point_b_name


class Point:
    def __init__(self, name: str, edges: list[Edge] = ()):
        self.name = name
        self.edges = edges

    def set_edges(self, edges: list[Edge]):
        self.edges = edges
