from nd_utility.oop.design_pattern.structural.composition.composite import Composite as BaseComposite
from ./component import Component
from ./leaf import Leaf
from typing import Optional

class Composite(Component, BaseComposite):
    """
    Composite node that can hold other Components.
    """

    def __init__(self):
        BaseComposite.__init__(self)
        Component.__init__(self)