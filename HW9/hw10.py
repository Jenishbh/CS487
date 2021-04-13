from abc import ABC, abstractmethod
class DataList(ABC):

    def __init__(self):

        self.items = []

        

    def addItem(self, item):

        self.items.append(item)

        

    # it is not completed yet, you need to add primitive method to it

    def search(self, target):

        for item in self.items:

            if target == self.getAttribute(item):

                return target

        return None  

 
   # it is not completed yet, you need to add primitive method to it

    def getTotal(self):

        sum = 0

        for item in self.items:

            sum += self.getAttribute(item)

        return sum

    
    def getAttribute(self, item):
        return item

class Student:

    def __init__(self, name, score, age):
        self.name=name
        self.score=score
        self.age=age

    def __str__(self):
        return self.name + ', ' + str(self.age)+', '+ "{:.2f}".format(self.score)


class StudentList(DataList):
    def setKey(self, getAttribute):
        self.__dict__.update(getAttribute)

    


def main():
    student = StudentList()
    student.addItem(Student("Jenish",77, 32))
    student.addItem(Student("Kunj",86, 44))
    student.setKey(dict(getAttribute=lambda x: x.score))
    sum=student.getTotal()
    print("Sum:", sum)

    student.setKey(dict(getAttribute=lambda x: x.age))
    age=student.getTotal()
    print("Age:", age)

    student.setKey(dict(getAttribute=lambda x: x.name))
    students = student.search("Jenish")
    print(students)

main()