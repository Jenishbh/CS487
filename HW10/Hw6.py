
import enum


class Student:
    def __init__(self, studentName):
        self.__studentName=studentName
        self.hw_score=[]
        self.exam_score=[]
        self.avg=()
        
        self.score=[] 

    
    @property
    def studentName(self):
        return self.__studentName
    
    
    
    

    def addHWScore(self):
        #c=input("enter a Student name: ")
        #if c in self.studentName:
        print("Please Enter -1 For exit")
        while True:
            self.score=int(input("Enter a Homework Score: "))
            if self.score == -1:
                break
            else:
                self.hw_score.append(self.score)

        return self.hw_score

        

    def addExamScore(self):
        #c=input("enter a Student name: ")
        #if c in self.studentName:
        print("Please enter -1 for exit")
        while True:
            self.score=int(input("Enter a Exam Score: "))
            if self.score == -1:
                break
            else:
                self.exam_score.append(self.score)

            
        return self.exam_score

    

    



    def calculate(self):
        totalh=0
        totalhavg=0
        totale=0
        totaleavg=0
        self.addHWScore()
        self.addExamScore()
        if len(self.hw_score)>5:
            self.hw_score.remove(min(self.hw_score))
            
        totalh=sum(self.hw_score)
        totalhavg=totalh/len(self.hw_score)
        print("The Homework Avrage is "+round((totalhavg), 2))
    
        totale=sum(self.exam_score)
        totaleavg=totale/len(self.exam_score)
        print("The Exam Avrage is "+round((totaleavg), 2))

        self.avg=(0.4*totalhavg)+(0.6*totaleavg)
        print("The final Avarage is ",round((self.avg),2))

        self.hw_score.clear()
        self.exam_score.clear()

        

        return self.avg

   


    
        




class Course(Student):
    def __init__(self, courceTitle, courceNo):
        Student.hw_score=[]
        Student.exam_score=[]
        self.__courceTitle=courceTitle
        self.__courceNo=courceNo
        self.Enroll=[]
        self.Studentlist=[]
        self.stu={}
        
        
       
    
    @property
    def courceTitle(self):
        return self.__courceTitle
    @property
    def courceNo(self):
        return self.__courceNo
    
    def studentName(self):
        return self.__studentName

    
    def addstudent(self, studentName):
        
        self.Studentlist.append(studentName)
        
        return self.Studentlist

    
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

    
    def studentgetAvarage(self):
        
        for i in self.Studentlist:
            self.stu[i]=(self.calculate())
        print(self.stu)
        return self.stu
         
        
        


class RecordOffice(Course):
    def __init__(self):
        self.stu=Course.stu

    
    
    def grade(self):
        for i in self.stu.values():
            if  i >= 90: return "A"
            if  90 > i >= 80: return "B"
            if  80 > i >= 70: return "C"
            if  70 > i >= 60: return "D"
            if  60 > i: return "F"



    



def main():
    s1=Student("Jenish")
    
    
    s=Course("Math",101)
    #
   #
    #s.studentgetAvarage(s1.studentList)
    #print("")
    #s.addHWScore(86)
    #s.addHWScore(64)
    #s.addHWScore(87)
    #s.addHWScore(65)
    #s.addHWScore(78)
    #s.addHWScore(93)
#
    #s.addExamScore(74)
    #s.addExamScore(95)
    #s.addExamScore(75)
    #s.addExamScore(76)
    #s.addExamScore(83)
    #s.calculate()
#
    s.addstudent("Jenish")
    s.studentgetAvarage()
    #
#
    s2=RecordOffice()
    s2.grade()
    
    
    
    









main()


    

    


        



