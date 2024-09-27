# -*- coding: ascii -*-
# by mrfriot

import logging


def main() -> None:
    pass


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        filename="snake.log",
        encoding="ascii",
        filemode="a",
        format="{asctime} | {levelname} | {message}",
        style="{",
        datefmt="%Y-%m-%d %H:%M"
    )
    logging.info("Start main.")
    main()
    logging.info("End main.")