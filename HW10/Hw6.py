
import enum


class Student:
    def __init__(self, studentName):
        self.__studentName=studentName
        Student.hw_score=[]
        Student.exam_score=[]
        Student.avg=()
        Student.Studentlist=[]
        
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
            self.score=int(input("Enter a Exam Score : "))
            if self.score == -1:
                break
            else:
                self.exam_score.append(self.score)

            
        return self.exam_score

    
    def addstudent(self):
        print("Please Enter 'exit' for Exit")
        while True:
            studentName=str(input("Enter A Student Name: "))
            if studentName == 'exit':
                break
            
            else:
                Student.Studentlist.append(studentName)
            
            
        return Student.Studentlist

    



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
        print("The Homework Avrage is ",round((totalhavg), 2))
    
        totale=sum(self.exam_score)
        totaleavg=totale/len(self.exam_score)
        print("The Exam Avrage is ",round((totaleavg), 2))

        self.avg=(0.4*totalhavg)+(0.6*totaleavg)
        print("The final Avarage is ",round((self.avg),2))

        self.hw_score.clear()
        self.exam_score.clear()
        Student.avg=self.avg
        return self.avg

   
    def result(self):
        return Student.avg


    
        




class Course(Student):
    def __init__(self, courceTitle, courceNo):
        self.hw_score=Student.hw_score
        self.exam_score=Student.exam_score
        self.avg=Student.avg
        self.__courceTitle=courceTitle
        self.__courceNo=courceNo
        self.Enroll=[]
        self.Studentlist=Student.Studentlist
        Course.stu={}
        
        
       
    
    @property
    def courceTitle(self):
        return self.__courceTitle
    @property
    def courceNo(self):
        return self.__courceNo
    
    def studentName(self):
        return self.__studentName

    
    
    

    
    def addStudent(self):
        
        for i in self.Studentlist:
            if i in self.Enroll:
                print("You Already Enroled in the class")
            else:
                self.Enroll.append(i)
                print("Student: "+str(i)+" added to class", end=" ")
                print( self.courceTitle)

    def display_Enroll(self):
        self.Enroll.sort()
        print("Number of Student Enrolled are: "+str(len(self.Enroll)))
        print("The Student enroled for the cource "+self.courceTitle)
        for i in self.Enroll:
            print(i)

    #def result(self):
    #    return Student.avg
    def studentgetAvarage(self):
        
        for i in self.Studentlist:
            print("Enter a Score For",i)
            Course.stu[i]=(self.avg)
        print(Course.stu)
        return Course.stu

    def grade(self):
        
        return Course.stu.values()

         
        
        


class RecordOffice(Course, Student):
    def __init__(self):
        self.Studentlist=Course.Studentlist
        self.stu=Course.stu
        RecordOffice.sgrade=[]
        

    
    def grade(self):
        (RecordOffice.sgrade)=self.stu.values()
        
        a=list(RecordOffice.sgrade)
        for i in a:
            RecordOffice.sgrade=float(i)
        
        return RecordOffice.sgrade

    
    def latter(self):
        
        if RecordOffice.sgrade >= 90: print("A"); return"A"
        elif RecordOffice.sgrade >= 80: return "B"
        elif RecordOffice.sgrade >= 70: return "C"
        elif RecordOffice.sgrade >= 60: return "D"
        else : return "E"


    



    
    

    
    

    



def main():
    s1=Student("Jenish")
    s1.addstudent()
    s1.calculate()
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
    
    
    s.studentgetAvarage()
    #s.grade()
    
    #
#
    s=RecordOffice()
    s.grade()
    #s.latter()
    
    
    
    









main()


    

    


        



