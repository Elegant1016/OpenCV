from abc import ABCMeta, abstractmethod
class Book(metaclass=ABCMeta):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self, title, author):
        pass



class Solution:
    pass

class MyBook(Book):
    def __init__(self, title, author, price):
        # Book.__init__(self, title, author)
        # super(MyBook, self).__init__( title, author)

        super().__init__(title, author)
        self.price = price

    def display(self):
        print("Title: " + self.title)
        print("Author: " + self.author)
        print("Price: " + str(self.price))
        # print("Price:", end=" ")
        # print(self.price)

title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()