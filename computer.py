class Computer:
    def __init__(self,cpus,storages,memory,model,price):
        self.__memory=memory
        self.__model=model
        self.__price=price
        self.__cpus=cpus
        self.__storages=storages



    def __init__(self,memory,model,price):
        self.memory=float
        self.model=str
        self.price=float
    
    def __str__(self,setCPU):
        return""


class CPU:
    def __init__(self,type,cores,speed):
        self.__type=type
        self.__cores=cores
        self.__speed=speed    
    def type(self):
        return self.__type
    def cores(self):
        return self.__cores
    def speed(self):
        return self.__speed
    def __str__(self):
        print("CPU type is",self.__type,"CPU cores is",self.__cores,"CPU speed is",self.__speed,"GHz")
        return""

class Storage:

    def __init__(self,type,size):
        self.__type=type
        self.__size=size
    
    

    def Type(self):
        return self.__type

    def Size(self):
        return self.__size

    def __str__(self):
        print ("Your memory type is",self.__type,"Your memory size is ",self.__size) 
        return ""


def main():
    St=Storage("8GB",1800)
    print(St)
    sp=CPU("I7",8,3.8)
    print(sp)

main()
