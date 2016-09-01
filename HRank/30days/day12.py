class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:" + self.lastName + "," + self.firstName)
        print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        Person.__init__(self,firstName,lastName,idNumber)
        # Person(firstName, lastName, idNumber, scores)
        self.scores = scores

    def calculate(self):
        avgScore = sum(self.scores)//len(scores)
        if avgScore in range(90,101):
            return "O"
        elif avgScore in range(80,91):
            return "E"
        elif avgScore in range(70, 81):
            return "A"
        elif avgScore in range(55, 71):
            return "P"
        elif avgScore in range(40, 56):
            return "D"
        else:
            return "T"


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = input()# not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
