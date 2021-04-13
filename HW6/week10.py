from abc import ABC, abstractmethod
from os import name


class Person(ABC):
    def __init__(self,name):
        self.name=name
    
    @abstractmethod
    def sname(self):
        pass
    @abstractmethod
    def dowork(self):
        pass

    

class Enginner(Person):
    
        

    @property
    def sname(self):
        print(self.name)
    @property
    def dowork(self):
        print(self.name+" Do work")
    @property
    def eng(self):
        print(self.name,"is Engineer")
        
        

    
class Skill(Person):
    def __init__(self):
        self.__person=None
        self.name=name

        

    @property
    def person(self):
        return self.__person



    @person.setter
    def person(self, person):
        self.__person=person

    


class Softwer(Skill):
    def __init__(self,person):
        self.person=person
        
    @property
    def sname(self): 
        print(self.person.name+" has a Softwer engineer skill")

    @property
    def dowork(self):
        print(self.person.name+ " Do work")

class Hardwer(Skill):
    def __init__(self,person):
        self.person=person

    @property
    def sname(self):
        print( self.person.name," has a Hardwer engineer skill")

    @property
    def dowork(self):
        print(self.person.name+ " Do work")

class Construction(Skill):
    def __init__(self,person):
        self.person=person

    @property
    def sname(self):
         
        print( self.person.name+" has a Construction engineer skill")

    @property
    def dowork(self):
        print(self.person.name+ " Do work")

class Management(Skill):
    def __init__(self,person):
        self.person=person

    @property
    def sname(self): 
        print( self.person.name+" has a Management skill")
    @property
    def dowork(self):
        print(self.person.name + " Do work")


def main():

    
    
    obj1=Enginner("Kunj")
    obj1.dowork
    

    obj2=Enginner("Jenish")
    obj2=Softwer(obj2)
    obj2.sname
    obj2.dowork
    obj3=Enginner("Lam")
    obj4=Enginner("Manish")
    obj4=Hardwer(obj4)
    obj4.sname
    obj4.dowork
    obj3=Management(obj3)
    obj3.sname
    obj3.dowork
    
    
    

main()
