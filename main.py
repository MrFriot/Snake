# -*- coding: ascii -*-
# by mrfriot

import logging
import map


def main() -> None:
    my_map = map.Map()
    my_map.setup("./maps/map1.json")
    print(my_map.points)
    print(my_map.edges)


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        # filename="snake.log",
        encoding="ascii",
        filemode="a",
        format="{asctime} | {levelname} | {message}",
        style="{",
        datefmt="%Y-%m-%d %H:%M"
    )
    logging.info("Start main.")
    main()
    logging.info("End main.")
