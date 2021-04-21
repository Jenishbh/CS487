
import enum


class Student:
    def __init__(self):
        
        Student.hw_score=[]
        Student.exam_score=[]
        Student.avg=()
        Student.Studentlist=[]
        self.score=[] 

    
    
    
    
    
    
    
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

   
    


    
        




class Course(Student):
    def __init__(self, courceTitle=None, courceNo=None):
        self.hw_score=Student.hw_score
        self.exam_score=Student.exam_score
        self.avg=Student.avg
        Course.courceTitle=[]
        Course.courceNo=[]
        self.Enroll={}
        self.Studentlist=Student.Studentlist
        Course.stu={}
        
        
       
    
    
    
    

    
    
    

    
    def addStudent(self):
        
        for i in self.Studentlist:
            
                while True:
                    e=input("Enter Cource Name: ")
                    if e=='exit':
                        break
                    else:
                        Course.courceTitle.append(e)
                    
                self.Enroll[i]=(Course.courceTitle)
                
                a=list(self.Enroll.values())
                for i in a:
                    self.Enroll=str(i)
                return self.Enroll


    def display_Enroll(self):
        self.Enroll.sort()
        print("Number of Student Enrolled are: "+str(len(self.Enroll)))
        print("The Student enroled for the cource "+self.courceTitle)
        for i in self.Enroll:
            print(i)

    #def result(self):
    #    return Student.avg
    
    def studentgetAvarage(self):
        ls=[]
        for i in self.Studentlist:
            for j in Course.courceTitle:
                print("Enter a Marks for %s in %s Subject"%(i,j))
                Course.stu[i]=[j, self.calculate()]
        print(Course.stu)
        return Course.stu

    def grade(self):
        
        return Student.avg

         
        
        


class RecordOffice(Course, Student):
    def __init__(self):
        self.Studentlist=Course.Studentlist
        self.avg=Student.avg
        self.stu=Course.stu
        
        

    
    

    
    def latter(self):
        
         for i in self.Studentlist:
            if self.avg >= 90: print("%s get Grade A in %s" %(i,Course.courceTitle)) 
            elif self.avg >= 80: print("%s get Grade B in %s" %(i,Course.courceTitle))
            elif self.avg >= 70: print("%s get Grade C in %s" %(i,Course.courceTitle))
            elif self.avg >= 60: print("%s get Grade D in %s" %(i,Course.courceTitle))
            else : print("%s get Grade E in %s" %(i,Course.courceTitle))


    



    
    

    
    

    



def main():
    s1=Student()
    s1.addstudent()
    
    s=Course()

    
    s.addStudent()
    s.studentgetAvarage()
    s.grade()
    

    s=RecordOffice()
    
    s.latter()

main()


    

    


        



