# coding: ascii


class Cell:
    _state: int

    def __init__(self, state: int = 0) -> None:
        if type(state) is not int:
            raise TypeError(f"Expected int, received {type(state).__name__}")
        self._state: int = state

    def get_state(self) -> int:
        return self._state

    def set_state(self, new_state: int) -> None:
        if type(new_state) is not int:
            raise TypeError(f"Expected int, received {type(new_state).__name__}")
        self._state = new_state
