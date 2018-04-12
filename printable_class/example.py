"""Example PrintableClass usage. We create other classes that inherit from PrintableClass and overload
__printable_attributes__ method. The printed result stores then all the information needed by the programmer."""

from printable_class import PrintableClass


class BaseClass(PrintableClass):
    def __init__(self, param):
        self.param = param

    def __printable_attributes__(self) -> list:
        return ["param"]


class ChildClass(BaseClass):
    def __init__(self, param, argum, value):
        super().__init__(param)
        self._argum = 0
        self.argum = argum
        self.value = value

    @property
    def argum(self) -> int:
        return self._argum

    @argum.setter
    def argum(self, v: int):
        if not isinstance(v, int):
            raise TypeError("argum should be an integer")
        self._argum = v

    def __printable_attributes__(self) -> list:
        inherited = super().__printable_attributes__()
        mine = ["argum", "value"]
        return inherited + mine

if __name__ == "__main__":
    a = ChildClass(1, 2, 3)
    print(a)
