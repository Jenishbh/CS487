import abc
from typing import Counter, Sized


class Displayble(abc.ABC):
    @abc.abstractmethod
    def Display():
        return None

class Employee(Displayble):
    def __init__(self, empid, salary):
        self.__empid=empid
        self.__salary=salary

    @property
    def empid(self):
        return self.__empid
    @empid.setter
    def empid(self, empid):
        self.__empid=empid

    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self, salary):
        self.__salary=salary

    
    def getSalary(self):
        return self.salary

    def Display(self):
        print("Employee ID: "+str(self.empid)+"\nSalary: "+str(self.salary))


    
class CompanyContract:
        MAX_EMPLOYEE_SIZE=10

        def maxEmployeeSize(cls):
            return  cls.MAX_EMPLOYEE_SIZE

        
class Company(Employee,Displayble, CompanyContract):
    def __init__(self, compName,numEmployees, employee=None):
        
        self.__compName=compName
        self.__employee=employee
        self.__numEmployees=numEmployees

    @property
    def compName(self):
        return self.__compName
    @compName.setter
    def compName(self, compName):
        self.__compName=compName

    @property
    def employee(self):
        return self.__employee
    @employee.setter
    def employee(self, employee):
        self.__employee=employee

    @property
    def numEmployees(self):
        return self.__numEmployees
    @numEmployees.setter
    def numEmployees(self, numEmployees):
        self.__numEmployees=numEmployees

    


    def addemployee(self,employee=list):
        self.employee=range(CompanyContract.MAX_EMPLOYEE_SIZE)
        self.employee=employee
        print("Employee List",(self.employee))
        
        
        

    def Display(self):
        print("Company Name: "+self.compName+"\nNumber of Employee: "+str(self.numEmployees))



class InternetCompany(Company):
    def __init__(self,url,salary=None):
       
        self.__url=url

    @property
    def url(self):
        return self.__url
    @url.setter
    def url(self, url):
        self.__url=url

    
    def getEmployeeHighSalary(self):
        print("High Salary",(Employee.getSalary))

    def Display(self):
        print("URL: "+str(self.url))

def main():
    s=Employee(1254,25000)
    s.Display()
    s2=Company("Intel",50)
    s2.addemployee(("Mayank","Jenish","Pritam"))
    s2.Display()
    s3=InternetCompany("Intel.com")
    s3.Display()
    s3.getEmployeeHighSalary()
    






    
main()      