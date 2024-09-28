# -*- coding: ascii -*-
# by mrfriot

import json
import logging
from point import Point


class Map:
    def __init__(self, points: tuple[Point] = ()):
        self.points = points

    def setup(self, path_to_file: str):
        try:
            with open(path_to_file, "r") as file:
                data = json.loads(file.read())
            self.points = data["points"]
        except json.decoder.JSONDecodeError:
            logging.error("json.decoder.JSONDecodeError: map file is empty.")
        except FileNotFoundError:
            logging.error("FileNotFoundError: path to map file is wrong.")
        except KeyError:
            logging.error("KeyError: map has not \"points\" key.")
        except TypeError:
            logging.error("TypeError: wtf, why is it not dict?")

    def commit(self, path_to_file: str):
        pass
