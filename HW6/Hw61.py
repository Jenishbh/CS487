import shutil
total_weight=0
class assigmnet:
    def __init__(self, assignment_num, assignment_name):
        self.__assignment_name=assignment_name
        self.__assignment_num=assignment_num

    @property
    def assignment_name(self):
        return self.__assignment_name
    @property
    def assignment_num(self):
        return self.__assignment_num
    
    @assignment_name.setter
    def assignment_name(self, assignment_name):
        self.__assignment_name=assignment_name

    @assignment_num.setter
    def assignment_num(self, assignment_num):
        self.__assignment_num=assignment_num

    def display(self):
        print("Assignment Name:"+str(self.assignment_name)+"\nAssignment Num:"+str(self.assignment_num))
        return




class Semester(assigmnet):
    def __init__(self, assignment_name=None,assignment_num=None, test=None, exam=None, weight=None):
      super().__init__(assignment_name,assignment_num)
      self.__test=test
      self.__exam=exam
      self.__weight=weight
      self.total_weight=total_weight
    
    #@property
    #def assignment(self):
      #  return self.__assignment
    #@property
    #def assignment_num(self):
       # return self.__assignment_num
    #@assignment.setter
    #def assignment(self, assignment):
      #  self.__assignment=assignment

    @property
    def test(self):
        return self.__test
    @test.setter
    def test(self, test):
        self.__test=test

    @property
    def exam(self):
        return self.__exam
    @exam.setter
    def exam(self, exam):
        self.__exam=exam

    @property
    def weight(self):
        self.__weight
    @weight.setter
    def weight(self, weight):
        self.__weight=weight
    
    g=open("Policy",'w')
    g.write("Assignment Num \t\t\t Assignment Name \t\t\t Exam Score")
    g.close()
    #add assignment
    def add_assignment(self,weight, assignment_num:list(range(4)), assignment_name:list(range(4))):
        global total_weight
        total_weight=total_weight+weight
        print(total_weight)
        if total_weight>101:
           raise ValueError 
             
        self.assignment=weight,assignment_num,assignment_name
        g=open("Policy", 'a')
        g.write("\n\nAssignmnet Num \t\t Assignment Name \t\t Assignment Wight\n"+str(self.assignment[2])+" \t\t\t\t\t\t  "+str(self.assignment[1])+" \t\t\t\t\t "+str(self.assignment[0]))
        g.close()
        
             
        return self.assignment
        
    g=open("Policy",'w')
    g.write("Assignment Num \t\t\t Assignment Name \t\t\t Exam Score")
    g.close()   
    #add test
    def add_test(self, weight, test_num:list(range(4)), test_name:list(range(4))):
        global total_weight
        total_weight=total_weight+weight
        print(total_weight)
        if total_weight>101:
           raise ValueError 
        self.test=test_num, test_name,weight
        g=open("Policy", 'a')
        g.write("\n\nTest Num \t\t Test Name \t\t Test Wight\n"+str(self.test[0])+" \t\t\t\t  "+str(self.test[1])+" \t\t\t "+str(self.test[2]))
        g.close()
        return self.test
    g=open("Policy",'w')
    g.write("Assignment Num \t\t\t Assignment Name \t\t\t Exam Score")
    g.close()
    def add_exam(self, weight,exam_num:list(range(1)), exam_name:list(range(1))):
        global total_weight
        total_weight=total_weight+weight
        print(total_weight)
        if total_weight>101:
           raise ValueError 
        self.exam=exam_num, exam_name, weight
        g=open("Policy", 'a')
        g.write("\n\nExam Num \t\t Exam Name \t\t Exam Wight\n"+str(self.exam[0])+" \t\t\t\t\t\t  "+str(self.exam[1])+" \t\t\t\t\t "+str(self.exam[2]))
        g.close()
        return self.exam
    
    def calculate_weight(self):
        self.weight=self.assignment[2]+self.test[2]+self.exam[2]
        if self.weight<=100:
            print("Your Wieght is balance")
        else:
            print("Your Weightage is unbalance please modify your Weight")
            g=open("Policy", 'r')
            print(g)
        return self.weight
    
        
    
    #Test
    def display(self):
        print( "Assignment Num: "+str(self.assignment[0])+"\nAssignment Name: "+str(self.assignment[1]))
        #test=print( "Test Num: "+str(self.test_num)+"\nTest Name: "+str(self.test_num))



class Student:
    def __init__(self, student_id=None, student_fname=None, student_lname=None):
        self.__student_id=student_id
        self.__student_fname=student_fname
        self.__student_lname=student_lname

    @property
    def student_id(self):
        return self.__student_id
    @student_id.setter
    def student_id(self, student_id):
        self.__student_id=student_id

    @property
    def student_fname(self):
        return self.__student_fname
    @student_fname.setter
    def student_fname(self, student_fname):
        self.__student_fname=student_fname

    @property
    def student_fname(self):
        return self.__student_fname
    @student_fname.setter
    def student_fname(self, student_fname):
        self.__student_fname=student_fname

    def add_student(self, student_id, student_fname, student_lname):
        self.student=(student_id,student_fname,student_lname)

        return self.student

    def __student__(self):
      self.__student_id
      self.__student_fname
      self.__student_lname

      return self.__student__

    
    def display(self):
        print("Student ID: "+str(self.student_id)+"\nStudent First Name: "+str(self.student_fname)+"\nStudent Last Name: "+str(self.__student_lname))
        

class score(Semester, Student):
    
        
        
        

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        self.__score=score

    

    def add_assignment_score(self):
      
      validate=input("Enter Assignment number: ")
      if validate == super().assignment_num:
        for student_id in self.__student__:
          self.score=float(input("Enter Score for ")+str(student_id))
          score<=100
      return None

    def display(self):
        print( "Student ID: "+str(self.score[1])+"\n added Score\n Assignment Num: "+str(self.score[0])+"\nAssigment Score: "+str(self.score[2]))

class exam_score(Semester, Student):
    def __init__(self, student_id=None, test=None, exam=None, test_score=None, exam_score=None,student=None):
        super().__init__(test, exam,student_id)
        self.__test_score=test_score
        self.__exam_score=exam_score
        self.student_id=student_id
        self.student=Student.add_student

    @property
    def test_score(self):
        return self.__test_score
    @test_score.setter
    def test_score(self, test_score):
        self.__test_score=test_score

    @property
    def exam_score(self):
        return self.__exam_score
    @exam_score.setter
    def exam_score(self, exam_score):
        self.__exam_score=exam_score


    def S_id(self):
      return Student.student_id

    g=open("Grade",'w')
    g.write("Student ID \t\t Test Name \t\t Test Score")
    g.close()
    def add_test_score(self, student_id, test, test_score):
        
        self.test_score=(student_id, test, test_score)
        g=open("Grade",'a')
        g.write("\n"+str(self.test_score[0])+"\t\t\t\t\t\t"+str(self.test_score[1])+"\t\t\t\t\t\t"+str(self.test_score[2]))
        g.close()
        print("Student ID: "+str(self.test_score[0])+"\nTest Name: "+str(self.test_score[1])+"\nTest Score: "+str(self.test_score[2]))
        return self.test_score



    g=open("Grade",'w')
    g.write("Student ID \t\t\t Exam Name \t\t\t Exam Score")
    g.close()
    def add_exam_score(self, student_id, exam, exam_score):
        
            self.exam_score=student_id,exam,exam_score
            g=open("Grade",'a')
            g.write("\n"+str(self.exam_score[0])+"\t\t\t\t\t\t"+str(self.exam_score[1])+"\t\t\t\t\t\t"+str(self.exam_score[2]))
            g.close()
            
          
            return self.exam_score
        
    
    
    def test_display(self):
        print()
        
    
    def exam_save(self):
        print()
        
        

    
        

    

        

def main():
    #Tester 
        #st=assigmnet(1,"Java")
        #st.add_assignment(2,"Java ad")
        #st2=Semester(1,"Java","test","exam",100)
        #st2.add_assignment(2,"Java ad",11)
        #st2.display()
        #st2=Student(19549,"Patel","Jenish")
        #st2.display()
        
        #st2.add_test(20,1,"Test1")
        #st2.display()
        #s2=score()
        #s2.add_assignment_score()
        #st2=exam_score()
        #st2.add_test_score(18762, "Mid1", 54)
        #st2.add_test_score(19549, "Mid1", 66)
        #st2.add_exam_score(Student.student_id, "E1", 78)
        
        
        
        #st1.display()
        #st2=score()
        #st2.add_assignment_score(st2.assignment_name,st2.student_id,23)
        #st2.display()
        #st2=exam_score()
        #st2.add_test_score(st2.student_id,st2.test,45)
        #st2.test_display()
        
        

        
        while KeyboardInterrupt:
            print("1:Add Assignments\n2:Add Test\n3:Add Exam\n4:calculate the wightage\n5:Add Student\n6:Add Score to Assigmnet\n7:Add score to Test\n8:Add score to exam\n9:Save the file ")
            user_input=int(input("Please choice following Menu: "))
            
            if(user_input == 1):
                try:
                    s=Semester()
                    s.add_assignment(float(input("Enter Weight: ")),input("Add assingment name: "), input("Enter assignment num: "))
                except ValueError: 
                    g=open("Policy",'r')
                    print(g.read())
                    print("\nWARNING\nThe Weight is Unbalance Please ENTER AGAIN")
                    s.add_assignment(float(input("Enter Weight: ")),input("Add assingment name: "), input("Enter assignment num: "))
                    
                
                
            elif(user_input == 2):
                try:
                    s=Semester()
                    s.add_test(float(input("Enter Weight: ")), int(input("Enter Test num: ")), input("Enter Test name: "))
                except ValueError: 
                    g=open("Policy",'r')
                    print(g.read())
                    print("\nWARNING\nThe Weight is Unbalance Please ENTER AGAIN")
                    s.add_assignment(float(input("Enter Weight: ")),input("Add assingment name: "), input("Enter assignment num: "))
            elif(user_input == 3):
                try:
                    s=Semester()
                    s.add_exam(float(input("Enter Weight: ")), int(input("Enter exam num: ")), input("Enter Exam name: "))
                except ValueError: 
                    g=open("Policy",'r')
                    print(g.read())
                    print("\nWARNING\nThe Weight is Unbalance Please ENTER AGAIN")
                    s.add_assignment(float(input("Enter Weight: ")),input("Add assingment name: "), input("Enter assignment num: "))
            elif(user_input==4):
                Semester.calculate_weight()
            elif(user_input==5):
                w=Student()
                w.add_student(int(input("Enter a StudentId: ")), input("Enter Student First name: "), input("Enter Student Last name: "))
            elif((user_input==6)):
                s=score()
                s.add_assignment(int(input("Enter wight: ")), input("Enter Student First Name: "), input("Enter Last name: "))
            elif(user_input==7):
                s=exam_score()
                s.add_test_score(int((input("Enter Student id: "))),input("Test name: "), int(input("Exam score: ")))
                break
            elif(user_input==8):
                s=exam_score()
                s.add_exam_score(int((input("Enter Student id: "))),input("Exam name: "), int(input("Exam score: ")))

            elif(user_input==9):
                seen = set()
                with open('Grade') as f, open('Grade1','w') as o:
                    for line in f:
                        if not line.isspace() and not line in seen:
                            o.write(line)
                            seen.add(line)
                

            else:
                print("Error")
                
                    


                








main()
