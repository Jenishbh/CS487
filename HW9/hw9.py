from abc import ABC, abstractmethod
class DataList(ABC):

    def __init__(self):
        self.item=[]

    def addItem(self, item):
        self.item.append(item)

    def processList(self):
        self.preProcess()

        for data in self.item:
            print(data)

        self.postProcess()

    @abstractmethod   
    def preProcess(self):
        pass
    @abstractmethod
    def postProcess(self):
        pass

class Student:

    def __init__(self, name, score):
        self.name=name
        self.score=score

    def __str__(self):
        return self.name + ', ' + "{:.2f}".format(self.score)


class StudentList(DataList):
    def preProcess(self):
        for student in self.item:
            student.score *=1.1


    def postProcess(self):
        sum=0
        for student in self.item:
            sum+= student.score

        print("Avg =",sum/len(self.item))

    


def main():
    student = StudentList()
    student.addItem(Student("Jenish",77))
    student.addItem(Student("Kunj",86))


    student.processList()

main()