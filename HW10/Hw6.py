
import enum


class Student:
    def __init__(self, studentName):
        self.__studentName=studentName
        self.hw_score=[]
        self.exam_score=[]
        self.avg=()
        self.studentList=[]
        self.score=[]

    
    @property
    def studentName(self):
        return self.__studentName
    
    
    
    

    def addHWScore(self, score):
        #c=input("enter a Student name: ")
        #if c in self.studentName:
            self.hw_score.append(score)
            return self.hw_score

        

    def addExamScore(self, score):
        #c=input("enter a Student name: ")
        #if c in self.studentName:
            self.exam_score.append(score)
            
            return self.exam_score

    def addstudent(self, studentnName):
        self.studentList.append(studentnName)
        return self.studentList

    



    def calculate(self):
        totalh=0
        totalhavg=0
        totale=0
        totaleavg=0
        if len(self.hw_score)>5:
            self.hw_score.remove(min(self.hw_score))
            
        totalh=sum(self.hw_score)
        totalhavg=totalh/len(self.hw_score)
        print("The Homework Avrage is "+str(totalhavg))
    
        totale=sum(self.exam_score)
        totaleavg=totale/len(self.exam_score)
        print("The Exam Avrage is "+str(totaleavg))

        self.avg=(0.4*totalhavg)+(0.6*totaleavg)
        print("The final Avarage is ",round((self.avg),2))

        self.hw_score.clear()
        self.exam_score.clear()

        return self.avg


    
        



            

        




class Course(Student):
    def __init__(self, courceTitle, courceNo, studentname=Student.studentName):
        self.__studentName=studentname
        self.hw_score=[]
        self.exam_score=[]
        self.avg=[]
        self.__courceTitle=courceTitle
        self.__courceNo=courceNo
        self.Enroll=[]
        
        
       
    
    @property
    def courceTitle(self):
        return self.__courceTitle
    @property
    def courceNo(self):
        return self.__courceNo
    
    def studentName(self):
        return self.__studentName

    

    
    def addStudent(self, studentName):
        
        if studentName in self.Enroll:
            print("You Already Enroled in the class")
        else:
            self.Enroll.append(studentName)
            print("Student: "+str(studentName)+" added to class", end=" ")
            print( self.courceTitle)

    def display_Enroll(self):
        self.Enroll.sort()
        print("Number of Student Enrolled are: "+str(len(self.Enroll)))
        print("The Student enroled for the cource "+self.courceTitle)
        for i in self.Enroll:
            print(i)

    
    def studentgetAvarage(self, studentName):
        stu={}
        for stu.keys in studentName:
            return 

            stu[]=round(self.avg, 2)
            print(stu)
         
        
        




class RecordOffice(Student):

    
    Student.avg=[]
    def grade(self):
        for i in self.avg:
            if  i >= 90: return "A"
            if  90 > i >= 80: return "B"
            if  80 > i >= 70: return "C"
            if  70 > i >= 60: return "D"
            if  60 > i: return "F"



    







def main():
    s1=Student("Jenish")
    s1.addstudent("Kunj")
    s1.addstudent("Jenish")
    s=Course("Math",101)
    
    s.addHWScore(76)
    s.addHWScore(34)
    s.addHWScore(87)
    s.addHWScore(65)
    s.addHWScore(58)
    s.addHWScore(43)

    s.addExamScore(54)
    s.addExamScore(45)
    s.addExamScore(65)
    s.addExamScore(76)
    s.addExamScore(23)
    s.calculate()
    s.studentgetAvarage(s1.studentList)
    print("")
    s.addHWScore(86)
    s.addHWScore(64)
    s.addHWScore(87)
    s.addHWScore(65)
    s.addHWScore(78)
    s.addHWScore(93)

    s.addExamScore(74)
    s.addExamScore(95)
    s.addExamScore(75)
    s.addExamScore(76)
    s.addExamScore(83)
    s.calculate()

    s.studentgetAvarage(s1.studentList)
    s.addStudent(s1.addstudent("Loy"))

    s=RecordOffice(s1.studentName)
    
    
    
    









main()


    

    


        



