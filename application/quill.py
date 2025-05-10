from typing import Protocol


class State(Protocol):

    def __init__(self):
        ...

    def switch_state(self, state):
        ...

    def refresh_data(self, state):
        ...
