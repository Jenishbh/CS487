
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
    def __init__(self, assignment_name,assignment_num, test, exam, weight):
      super().__init__(assignment_name,assignment_num)
      self.__test=test
      self.__exam=exam
      self.__weight=weight
    
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

    #add assignment
    def add_assignment(self, weight,assignment_num=list(range(6)),assignment_name=list(range(6))):
        self.assignment=weight,assignment_num, assignment_name
        f=open("Policy", "a")
        f.write("\n\nAssignmnet Num \t\t Assignment Name \t\t Assignment Wight\n"+str(self.assignment[2])+" \t\t\t\t\t\t  "+str(self.assignment[1])+" \t\t\t\t\t "+str(self.assignment[0]))
        f.close()
        return self.assignment
        
    #add test
    def add_test(self, weight, test_num=list(range(4)), test_name=list(range(4))):
        self.test=test_num, test_name,weight
        f=open("Policy", "a")
        f.write("\n\nTest Num \t\t Test Name \t\t Test Wight\n"+str(self.test[0])+" \t\t\t\t  "+str(self.test[1])+" \t\t\t "+str(self.test[2]))
        f.close()
        return self.test

    def add_exam(self, weight,exam_num=list(range(1)), exam_name=list(range(1))):
        self.exam=exam_num, exam_name, weight
        f=open("Policy", "a")
        f.write("\n\nExam Num \t\t Exam Name \t\t Exam Wight\n"+str(self.exam[0])+" \t\t\t\t\t\t  "+str(self.exam[1])+" \t\t\t\t\t "+str(self.exam[2]))
        f.close()
        return self.exam
    
    def calculate_weight(self):
        self.weight=self.assignment[2]+self.test[2]+self.exam[2]
        if self.weight<=100:
            True
        else:
            print("Your Weightage is unbalance please modify your Weight")
        return self.weight
    
        
    
    #Test
    def display(self):
        print( "Assignment Num: "+str(self.assignment[2])+"\nAssignment Name: "+str(self.assignment[1]))
        #test=print( "Test Num: "+str(self.test_num)+"\nTest Name: "+str(self.test_num))



class Student:
    def __init__(self, student_id, student_fname, student_lname):
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

    
    def display(self):
        print("Student ID: "+str(self.student_id)+"\nStudent First Name: "+str(self.student_fname)+"\nStudent Last Name: "+str(self.__student_lname))
        

class score(Semester, Student):
    def __init__(self, assignment_name=None, assignment_num=None,student_id=None,score=None):
        super().__init__(assignment_name, assignment_num, test=None, exam=None)
        Student().__init__(student_id,student_fname=None,student_lname=None)
        
        self.__score=score

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        self.__score=score



    def add_assignment_score(self, assignment_num,student_id, score):
        self.__score=(assignment_num,student_id, score<=100)
        return self.score

    def display(self):
        print( "Student ID: "+str(self.score[1])+"\n added Score\n Assignment Num: "+str(self.score[0])+"\nAssigment Score: "+str(self.score[2]))

class exam_score(Semester, Student):
    def __init__(self, student_id=None, test=None, exam=None, test_score=None, exam_score=None):
        super().__init__(test, exam,assignment_name=None, assignment_num=None)
        Student().__init__(student_id)
        self.__test_score=test_score
        self.__exam_score=exam_score

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


    def add_test_score(self, student_id, test, test_score):
        self.test_score=(student_id, test, test_score)
        return self.test_score

    def add_exam_score(self, student_id, exam, exam_score):
        self.exam_score=student_id,exam,exam_score
        return self.exam

    def test_display(self):
        print("Student ID: "+str(self.test_score[0])+"\nTest Name: "+str(self.add_test_score[1])+"\nTest Score: "+str(self.test_score[2]))

    def exam_display(self):
        print("Student Id: "+str(self.exam_score[0]+"\nExam Name: ")+str(self.exam_score[1])+"\nExam score: "+str(self.exam_score[2]))

    

        

def main():
    #Tester 
        #st=assigmnet(1,"Java")
        #st.add_assignment(2,"Java ad")
        #st2=Semester(1,"Java","test","exam",100)
        #st2=Student(19549,"Patel","Jenish")
        #st2.add_assignment(10,"Java ad",11)
        #st2.add_test(20,1,"Test1")
        #st2.display()
        
        
        #st1.display()
        #st2=score()
        #st2.add_assignment_score(st2.assignment_name,st2.student_id,23)
        #st2.display()
        #st2=exam_score()
        #st2.add_test_score(st2.student_id,st2.test,45)
        #st2.test_display()


        user_input=int(input("Please choice following Menu"))

        print("1:Add Semister\n2:Add Assignments\n3:Add Test\n4:Add Exam\n5:Add Student\n6:Add Score to Assigmnet\n7:Add score to Test\n8:Add score to exam\n9:Save the file ")

        while KeyboardInterrupt:
            
            if(user_input ==1 ):
                s=input(Semester())
            elif(user_input == 2):
                s=input(Semester.add_assignment())
            elif(user_input == 3):
                s=input(Semester.add_test())
            elif(user_input == 4):
                s=input(Semester.add_test())
            elif(user_input==5):
                s=input(Semester.add_exam())
            elif((user_input==6)):
                s=input(Student())
            elif(user_input==7):
                a=input("Student id: ")
                if a in s.find(Student.student_id):
                    print(Student.display())
                    print("\nEnter Student Score: ")
                    s=input(score.add_assignment_score()) 
            elif(user_input==8):
                a=input("Student id: ")
                if a in s.find(Student.student_id):
                    print(Student.display())
                    print("\nEnter Student Score: ")
                    s=input(exam_score.add_test_score())
            elif(user_input==9):
                a=input("Student id: ")
                if a in s.find(Student.student_id):
                    print(Student.display())
                    print("\nEnter Student Score: ")
                    s=input(exam_score.add_exam_score())

            elif(user_input==10):
        


main()
