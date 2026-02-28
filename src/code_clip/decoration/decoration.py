from typing import Any

from src.code_clip.decoration.decorator import Decorator
from src.code_clip.decoration.interface import Interface


class Decoration(Decorator):
    def __init__(self, inner: Interface, additional_property: Any):
        Decorator.__init__(self, inner)
        self._additional_property = additional_property

    def get_additional_property(self) -> Any:
        return self._additional_property
