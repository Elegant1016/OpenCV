from abc import ABCMeta, abstractmethod

class Animal:
    __metaclass__ = ABCMeta

    @abstractmethod
    def saySomething(self):
        pass


class Cat(Animal):
    def saySomething(self):
        print("I say Meauuuu")

# a = Animal()
c = Cat()
c.saySomething()