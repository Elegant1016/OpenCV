from abc import ABCMeta, abstractmethod

class Base(metaclass=ABCMeta):
    @abstractmethod
    def foo(self):
        pass

    @abstractmethod
    def bar(self):
        pass

class Concrete(Base):
    def foo(self):
        print("Foo Implemented")

    def bar(self):
        print("Bar Implemented")

assert issubclass(Concrete, Base)
c = Concrete()
c.bar()
c.foo()