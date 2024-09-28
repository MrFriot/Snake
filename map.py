# -*- coding: ascii -*-
# by mrfriot

import json
import logging
from graph import Edge, Point


class Map:
    def __init__(self, points: list[Point] = (), edges: list[Edge] = ()):
        self.points = points
        self.edges = edges

    def setup(self, path_to_file: str):
        try:
            with open(path_to_file, "r") as file:
                data = json.loads(file.read())

            edges = [Edge(edge[0], edge[1]) for edge in data["edges"]]
            self.edges = edges

            points = []
            for point_name in data["points"]:
                point_edges = []
                for edge in edges:
                    if edge.point_a == point_name or edge.point_b == point_name:
                        point_edges.append(edge)
                points.append(Point(point_name, point_edges))
            self.points = points
        except json.decoder.JSONDecodeError:
            logging.error("json.decoder.JSONDecodeError: map file misfiled.")
        except FileNotFoundError:
            logging.error("FileNotFoundError: path to map file is wrong.")
        except KeyError:
            logging.error("KeyError: map has not necessary key.")
        except TypeError:
            logging.error("TypeError: wtf, why is it not dict?")
        except IndexError:
            logging.error("IndexError: some edge oes not have one of the points.")

    def commit(self, path_to_file: str):
        pass
