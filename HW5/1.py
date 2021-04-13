class Robot():
    # Constructor
    def __init__(self, machineName, cpu, model, speed):
        #Machine().__init__(machineName)
        #JetFighter().__init__(model, speed)
        
        self.__cpu=cpu

    @property
    def cpu(self):
        return self.__cpu
    @cpu.setter
    def cpu(self, cpu):
        self.__cpu=cpu
        

    # Methods here
    def getExpensivePartsByType(cls):
        return list(Part.partNo())

    def getMovablePartsByType(cls):
        movablePart={MovablePart.type() : list(MovablePart.partNo())}

        return movablePart
    
    def fly(cls):
        pass

    def doWork(cls):
        return
    def display(cls):
        return "Machine:"+str(cls.__machineName)+"\nCPU:"+str(cls.__cpu)+"\nThis Machine has This parts\n"+"Part No:"+str(cls.__partNo)+"\nPrice"+str(cls.__price)
def main():
    robo = Robot('MTX', 'M1X', 'F-16', 1000)

main()