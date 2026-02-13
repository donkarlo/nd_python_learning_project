from abc import ABC, abstractmethod

class Interface(ABC):
    @abstractmethod
    def __init__(self, inner:"Interface"):
        pass

    @abstractmethod
    def decorator_decoration_shared_method(self):
        pass
