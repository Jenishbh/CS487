from abc import ABC , abstractmethod

class Bird:
    def fly(self):
        print("A Bird can Fly")


class Car:
    def run(self):
        print("A Person has a car")


class Person:
    def walk(self):
        print("A person can walk")



class Command(ABC):
    @abstractmethod
    def executed(self):
        pass

class invoke_fly(Command):
    def __init__(self, bird):
        self.bird=bird

    def executed(self):
       self.bird.fly()



class invoke_Car(Command):
    def __init__(self, car):
        self.car=car

    def executed(self):
       self.car.run()

class invoke_Person(Command):
    def __init__(self, person):
        self.person=person

    def executed(self):
       self.person.walk()
       

class Invoker:
    def __init__(self):
        self.commands=[]

    def addcommand(self, command):
        self.commands.append(command)

    def doWork(self):
        [c.executed() for c in self.commands]



def main():
    bird=Bird()
    car=Car()
    person=Person()

    invoker = Invoker()

    invoker.addcommand(invoke_fly(bird))
    invoker.addcommand(invoke_Car(car))
    invoker.addcommand(invoke_Person(person))


    invoker.doWork()


main()