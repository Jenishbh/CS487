class Person:
    def __init__(self,name=None):
        self.__name=name
        

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name=name

    def display(self):
        return "Name="+str(self.__name)

    def doWork(self):
        return str(self.__name)+"Is doing Nothing"

class Programmer(Person):
    def __init__(self, name, skills, salary):
        super().__init__(name=name)
        self.__skills=skills
        self.__salary=salary

    @property
    def skills(self):
        return self.__skills
    @skills.setter
    def skills(self,skills):
        self.__skills=skills
    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self, salary):
        self.__salary=salary

    def getAnnualincome(self):
        return self.__salary*12

    def display():
        return 

    def doWork():
        return 

class Manager(Programmer):
    def __init__(self, name, skills, salary,bouns):
        super().__init__(name, skills, salary)
        self.__bouns=bouns

    @property
    def bouns(self):
        return self.__bouns
    @bouns.setter
    def bouns(self, bouns):
        self.__bouns=bouns

    def getAnnualincome(self):
        return self.__salary*12+self.__bouns

    def display(self):
        return "name="+str(self.__name)+"\nSkills="+str(self.__skills)+"\nSalary"+str(self.__salary)
    def doWork(self):
        return str(self.__name)+"Is doing Nothing"  

class Project:
    def __init__(self, projName, budget=0.0, active=False):
        self.__projName=projName
        self.__budget=budget
        self.__active=active

    @property
    def projName(self):
        return self.__projName
    @projName.setter
    def projname(self, projName):
        self.__projName=projName
    
    @property
    def budget(self):
        return self.__budget
    @budget.setter
    def budget(self, budget):
        self.__budget=budget

    @property
    def active(self):
        return self.__active
    @active.setter
    def avtive(self, active):
        self.__active=active


    def display():
        return



class Group(Person):
    def __init__(self, name, member, groupName):
        Person.__init__(name)   
        self.__member=member
        self.__groupName=groupName

    @property
    def member(self):
        return self.__member
    @member.setter
    def member(self, member):
        self.__member=member

    @property
    def groupName(self):
        return self.__groupName

    @groupName.setter
    def groupName(self):
        self.__groupName=groupName

    

    def addMember(self, member):
       self.__member.append(member)
       return

    def AnyoneDoWork(self):
        return self.__name+"Do work!"

    def askManagerDoWork(self):
        return self.__name+"ASk to work"

    def getAllMEmberMoreThe(self, income):
        return

    def display(self):
        return "Name:"+self.__name+"Member of:"+self.__member+"Group Name:"+self.__groupName


class ITGroup(Project):
    def __init__(self, project):
        super().__init__(projName, budget=budget, active=active)
        self.__project = project


    @property
    def project(self):
        return self.__project

    @project.setter
    def project(self):
        self.__project=project

    def addProject(self, project):
        self.__project.append(project)
        return
    
    def findLargestProject(self):
        return "Project:"+self.__project+"Budget:"+self.__budget

    def display():
        return

    def getActiveProjects(self):
        return self.__active


        




















def main():
    p1 = Programmer("Lily", "C++, Java", 10000)
    p2 = Programmer("Judy", "Python, Java", 18000)
    m = Manager("Peter", "Management", 20000, 20000)
    proj1 = Project("MAX-5", 200000, True)
    proj2 = Project("FOX-4", 100000, False)
    proj3 = Project("FOX-XP", 500000, True)
    itgrp = ITGroup("ATX Group")
    itgrp.addMember(p1)
    itgrp.addMember(p2)
    itgrp.addMember(m)
    itgrp.addProject(proj1)
    itgrp.addProject(proj2)
    itgrp.addProject(proj3)
    itgrp.display()
    itgrp.askAnyoneDoWork()
    print()
    itgrp.askManagerDoWork()
    print("\nGet the largest project...")
    maxProj = itgrp.findLargestProject()
    maxProj.display()
    print("\nGet the acive projects...")
    projects = itgrp.getActiveProjects()
    for proj in projects:
    proj.display()
    print()
    print("\nGet the members with high income...")
    members = itgrp.getAllMembersMoreThan(200000)
    for member in members:
    member.display()
    print()