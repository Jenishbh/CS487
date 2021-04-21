

#Class Student perform add Student Details such as a student name, student homework score, student exam score
#and calculate the avarage

class Student:
    def __init__(self):
        
        Student.hw_score=[] #initial contain Homework Store
        Student.exam_score=[] # initial contain Exam Socre
        Student.avg=()          #initial contain avarage
        Student.Studentlist=[]  #has a student list
        self.score=[]              # has a score 

    
    
    
    
    
    #the function ask user to enter the homework score and whenever they want exit just type -1 insated of score
    
    def addHWScore(self):
        
        print("Please Enter -1 For exit")
        while True:
            self.score=int(input("Enter a Homework Score: "))
            if self.score == -1:
                break
            else:
                self.hw_score.append(self.score)

        return self.hw_score

        
    #the function ask user to enter the exam score and whenever they want to exit just type -1 insated of score

    def addExamScore(self):
        
        print("Please enter -1 for exit")
        while True:
            self.score=int(input("Enter a Exam Score : "))
            if self.score == -1:
                break
            else:
                self.exam_score.append(self.score)

            
        return self.exam_score

    # the fuction ask user to input student name and type exit for Exit
    def addstudent(self):
        print("Please Enter 'exit' for Exit")
        while True:
            studentName=str(input("Enter A Student Name: "))
            if studentName == 'exit':
                break
            
            else:
                Student.Studentlist.append(studentName)
                
            
        return Student.Studentlist

      

    #the calculate function find the homework avarage and prompt after then 
    #find exam score avarage and prompt the user and after calculate final avarage with
    # 40% of hw avrage abd 60% of exam avarge 
    # also if user input more then 5 hw score then the fuction remove the minimum score from the list and calculate the avarage  

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

   
    


    
        


#class Course contain all details about course and the student

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
        
        
       
    
    
    
    

    
    
    
    #the function addstudent ask the user for cource name and assign the cource to the student 
    
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

    #desplay the total student count on a cource

    def display_Enroll(self):
        self.Enroll.sort()
        print("Number of Student Enrolled are: "+str(len(self.Enroll)))
        print("The Student enroled for the cource "+self.courceTitle)
        for i in self.Enroll:
            print(i)


    #the function get the student list and thir cource selection and ask user to enter the marks for perticuler subject and after added to one dict
    
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

         
        
        

# the Record office file contain all student final grade of cource
class RecordOffice(Course, Student):
    def __init__(self):
        self.Studentlist=Course.Studentlist
        self.avg=Student.avg
        self.stu=Course.stu
        
        

    
    
    #this function define the latter grade based on student's final avarage
    
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


    

    


        



