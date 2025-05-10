from typing import Protocol


class Quill(Protocol):
    def __init__(self):
        ...

    def switch(self):
        ...

    def refresh(self):
        ...
