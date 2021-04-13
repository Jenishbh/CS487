class Time():
    def __init__(self,hour,minute,second):
        self.__hour=hour
        self.__minute=minute
        self.__second=second

    def hour(self):
        return self.__hour

    def minute(self):
        return self.__minute
    def second(self):
        return self.__second

    def __str__(self):
        return str(self.__hour)+":"+str(self.__minute)+":"+str(self.__second)

class SavingsAccount(Time):
    
    def __init__(self,annualinterestRate,savingsBalance,updetedTime):
        self.__annualinterestRate=annualinterestRate
        self.__savingsBalance=savingsBalance
        self.__updetedTime=updetedTime
        
        

    def annualinterestRate(self):
        return self.__annualinterestRate
    def savingsBalance(self):
        return self.__savingsBalance
    #def updatedTime(self):
        #return self.__updatedTime


    
    def __calculateMonthlyIntrest(self):
        return (self.__annualinterestRate*self.__savingsBalance)/12/100
    def __addbalance(self):
        return self.__calculateMonthlyIntrest()+self.__savingsBalance



    def InitBalance(self):
        print("$",self.__savingsBalance,"Updated:",self.__updetedTime)
        return""

    def Show(self,updetedTime):
        print("Balance After 1 month's intrest applide at",self.__annualinterestRate/100,"\n",self.__addbalance(),"Updated:",updetedTime)
        return""
        






