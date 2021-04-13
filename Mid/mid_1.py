from abc import abstractmethod


import enum
from typing import Dict, Iterable


class Rank(enum.Enum):

    Sergeant=1
    Corporal=1
    Specialist=3
    Private=4

class Parachute(enum.Enum):

    Sea=1
    Land=2




class Displayable():
    @abstractmethod
    def display():
        pass



class Flyable():
    def __init__(self) -> None:
        self.__fly

    @property
    def fly(self):
        return self.__fly
    @fly.setter
    def fly(self, fly):
        self.__fly=fly

    @abstractmethod
    def getTotalFuelExpense():
        pass
        


class Aircraft(Displayable, Flyable):
    def __init__(self,wing=float,weight=float):
        self.__wing=wing
        self.__weight=weight
        

    @abstractmethod
    @property
    def wing(self):
        return self.__wing
    @wing.setter
    def wing(self, wing):
        self.__wing=wing

    
    @abstractmethod
    def weight(self):
        return self.__weight

    @abstractmethod
    def parachute(self):
        return Parachute

    def getTotalFuelExpense():
        None

    def display(self):
        print("Aircraft Wing: "+str(self.__wing)+"\n Arcraft Weight: "+str(self.__weight)+"\nAircraft Paracute: "+str())


class Battleship(Aircraft, Displayable):
    def __init__(self, aircrafts=list, shipName=str):
        self.__aircrafts=[]
        self.__shipName=shipName

    @property
    def shipName(self):
        return self.__shipName
    @shipName.setter
    def shipName(self, shipName):
        self.__shipName=shipName

    
    def addAirCraft(self,name,shipname,weight,wing ):
        self.__aircrafts.append(name,shipname,weight,wing)
        return self.__aircrafts

    def display(self):
        return "Added aircraft: "+str(list(self.__aircrafts))

    
class Soldier(Displayable):
    def __init__(self,rank:Rank,salary:float,name:str):
        self.__rank=Rank
        self.__salary=salary
        self.__name=name

    def __soldier__(self):
        return self.__rank,self.salary,self.name
        

    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self, salary):
        self.__salary=salary

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name=name

    
    
    def display(self):
        print("Name: "+self.__name+"\nSalary: "+str(self.__salary+"Rank: "+str(self.__rank)))


class Jetfighter(Aircraft):
    def __init__(self, missiles:list,regulerfuel:float):
        self.__missiles=[]
        self.__regulerfuel=regulerfuel

    

    def missiles(self):
        return self.__missiles

    def regularFuel(self):
        return self.__regulerfuel

    def getTotalFuelExpense(self):
        return self.__regulerfuel*5.5
        

class SpaceShuttle(Jetfighter):
    def __init__(self, superfuel:float):
        self.__superfuel=superfuel

    
    def superFuel(self):
        return self.__superfuel

    def getTotalFuelExpense(self):
        return super().getTotalFuelExpense()+self.__superfuel




class Carrier(Soldier, Battleship):
    def __init__(self, rank: Rank, salary: float, name: str):None
        
        
        
    def __soldier__(self):
        return super().__soldier__()
    
    def addSoldier(self,name,rank,salary):
        return self.__soldier__.append(name,rank,salary)

    def findTopFiveSoldierNameWithHighSalaries(self):
        for Soldier.__soldier__.sort_values(by=[self.salary]).head(5) in Soldier.__soldier__ :
            print("Name: "+self.name)

    def findAllAircraftFuelExpenses():
        return super().getTotalFuelExpense

    def askAllJetFighterToFly():
        return Aircraft.fly("FLY")

    def getSoldier(self,index):
        try :
            index(self.name)
        except IndexError:
            print("An error occoured")

    def getSoldiersByRank(self):
       return {
            self.__rank : self.__name and self.__salary
            
        }

 

    
def main():
    s1=Aircraft(2,3.5)
    s1.parachute(Parachute.Land)
    #s1.display()
    s2=Soldier(Rank.Sergeant,50456.4,"Balbinder Sing")
    s2.display()
    s2=Jetfighter("Bramosh, agni",572)
    s2.getTotalFuelExpense()
    s2=SpaceShuttle(447)
    s2.getTotalFuelExpense
    s2=Battleship("F-16, J-7","Fighter")
    s2.addAirCraft("F-7","Fighter",45,2)
    s2.addAirCraft("Mig-27","Bomber",88,2)
    s2.addAirCraft("Sukhoi","Bomber",41,2)
    s2.display
    s2=Carrier()
    s2.addSoldier("Jigar",Rank.Corporal,2541)
    s2.addSoldier("Harsh",Rank.Sergeant,8855)
    s2.addSoldier("Jagan", Rank.Private,2210)
    s2.addSoldier("Limon",Rank.Corporal,4562)
    s2.findAllAircraftFuelExpenses()
    s2.askAllJetFighterToFly()
    s2.findTopFiveSoldierNameWithHighSalaries()

main()

    

