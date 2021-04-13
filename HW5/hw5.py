import abc




class JetFighter():
    def __init__(self,model,speed):
        self.__model=model
        self.__speed=speed
    @property
    def speed(self):
        return self.__speed
    @speed.setter
    def partNo(self, speed):
        self.__speed=speed

    @property
    def model(self):
        return self.__model
    @model.setter
    def model(self, model):
        self.__model=model

    def __str__(self):
        return "Model:"+str(self.__model)+"speed:"+str(self.__speed)

class MovablePart:
    def __init__(self,partNo,price,type):
        self.__partNo=partNo
        self.__price=price
        self.__type-type

    @property
    def partNo(self):
        return self.__partNo
    @partNo.setter
    def partNo(self, partNo):
        self.__partNo=partNo

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price):
        self.__price=price

    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type):
        self.__type=type

    def Move():
        return None
    def __str__(self):
        return "Part No:"+str(self.__partNo)+"Price:"+str(self.__price)+"Type:"+str(self.__type)
    
class Part(MovablePart):
        def __init__(self,partNo,price):
            super().__init__(partNo,price)
            self.__partNo=partNo
            self.__price=price

        @property
        def partNo(self):
            return self.__partNo

        @partNo.setter
        def partNo(self, partNo):
            super().__partNo=partNo

        @property
        def price(self):
            return self.__price

        @price.setter
        def price(self, price):
            super().__price=price

       
class Displayable(Part, JetFighter):
    
    def display(self):
        return None

class Movable(MovablePart):
    @abc.abstractmethod
    def move():
        return None
    
    def fly():
        return None

class Flyable(JetFighter):
    
    def fly():
        return None

class Robot:
    def __init__(self, machineName, cpu, model, speed):
        self.__machineName=machineName
        self.__cpu=cpu
        self.__model=model
        self.__speed=speed

    @property
    def machineName(self):
        return self.__machineName
    @machineName.setter
    def machineName(self, machineName):
        self.__machineName=machineName

    @property
    def cpu(self):
        return self.__cpu
    @cpu.setter
    def cpu(self, cpu):
        self.__cpu=cpu

    @property
    def model(self):
        return self.__model
    @model.setter
    def model(self, model):
        self.__model=model

    @property
    def speed(self):
        return self.__speed
    @speed.setter
    def speed(self, speed):
        self.__speed=speed


    #def getExpensiveParts(double priceLimit):
        #return double.__priceLimit

    def getMovablePartsByType():{
        
    }

    def fly():
        pass
    def doWork(self):
        return "Machine Name:"+str(self.__machineName)+"CPU:"+str(self.__cpu)+"Model:"+str(self.__model)+"Speed:"+ste(self.__speed)


class Machine(Robot,Part):
    def __init__(self, machineName, cpu, model, speed):
        super().__init__(machineName, model, speed)
        Part().__init__(partNo,price)
        self.__machineName=machineName
        

    @property
    def machineName(self):
        return self.__machineName
    @machineName.setter
    def machineName(self, machineName):
        super().__machineName=machineName

    def partNO(self, partNO):
        return super().partNO(partNO)

    def price(self, price):
        return super().price(price)

    def doWork(self):
        return None

    def addPart(part):
        super().partNO.append(part)
        
        return None

    def removePart(partNO):
        super().partNO.append(partNO)

    def findDuplicatedPart():
        {
            super().partNo
        }













def main():
	robo = Robot('MTX', 'M1X', 'F-16', 10000)
	robo.addPart(Part(111, 100))
	robo.addPart(Part(222, 200))
	robo.addPart(Part(333, 300))
	robo.addPart(Part(222, 300))
	robo.addPart(MovablePart(555, 300, "TypeA"))
	robo.addPart(Part(111, 100))
	robo.addPart(Part(111, 100))
	robo.addPart(MovablePart(777, 300, "TypeB"))
	robo.addPart(MovablePart(655, 300, "TypeA"))
	robo.addPart(MovablePart(755, 300, "TypeA"))
	robo.addPart(MovablePart(977, 300, "TypeB"))
	
	robo.display()
	print()
	robo.doWork()
	print()
	robo.fly()
	print()
	
	partFreq = robo.findDuplicatedParts()
	for partNo in partFreq.keys():
		print(partNo,'=>', partFreq[partNo], 'times')
		
	print("\nExpensive part list----")
	expensiveParts = robo.getExpensiveParts(200)
	for part in expensiveParts:
		part.display()
	
	print("\nMovable part list----")
	movableParts = robo.getMovablePartsByType()
	for type, parts in movableParts.items():
		print("type =", type)
		for part in parts:
			part.display()
		print()
		
main()













































    

