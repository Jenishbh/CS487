import enum


class Student:
    def __init__(self, studentName):
        self.__studentName=studentName
        self.hw_score=[]
        self.exam_score=[]
        self.avg=()

    
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

    def student(self):
        return self.studentName

    def calculate(self):
        totalh=0
        totale=0
        if len(self.hw_score)>5:
            a=min(self.hw_score)
            self.hw_score.remove(a)
            for i in range(0, len(self.hw_score)):
                totalh=totalh+self.hw_score[i]
                
            for j in range(0, len(self.exam_score)):
                totale=totale+self.exam_score[j]
    
            self.avg=(((totalh*40)/100)/len(self.hw_score))+(((totale*60)/100)/len(self.exam_score))
            print("Student Total Avarage: "+str(round(self.avg)))
            
        else:
            for i in range(0, len(self.hw_score)):
                totalh=totalh+self.hw_score[i]
                
            for j in range(0, len(self.exam_score)):
                totale=totale+self.exam_score[j]
    
            self.avg=(((totalh*40)/100)/len(self.hw_score))+(((totale*60)/100)/len(self.exam_score))
            print("Student Total Avarage: "+str(round(self.avg)))
     
        return self.avg



class Course(Student):
    def __init__(self, courceTitle, courceNo):
        
        self.__courceTitle=courceTitle
        self.__courceNo=courceNo
        self.Enroll=[]
        
    @property
    def courceTitle(self):
        return self.__courceTitle
    @property
    def courceNo(self):
        return self.__courceNo

    def students(self):
        return self.studentName

    
    def addStudent(self, student):
        
        if self.studentName in self.Enroll:
            print("You Already Enroled in the class")
        else:
            self.Enroll.append(self.studentName)
            print("Student: "+str(self.studentName)+" added to", end="")
            print(self.courceTitle)

    def display_Enroll(self):
        self.Enroll.sort()
        print("Number of Student Enrolled are: "+str(len(self.Enroll)))
        print("The Student enroled for the cource "+self.courceTitle)
        for i in self.Enroll:
            print(i)

    def getStudentAvarages(self):
        for studentname in Student.studentName:
            group={studentname : avg}
        




class RecordOffice(Student):
    
    def calculate(self):
        return super().calculate()

    #def grade():
    #    if  avg >= 90: return "A"
    #    if  90 > avg >= 80: return "B"
    #    if  80 > avg >= 70: return "C"
    #    if  70 > avg >= 60: return "D"
    #    if  60 > avg: return "F"



    







def main():
    s=Student("Jenish")
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

    s=Course("Math",101)
    s.getStudentAvarages()









main()


    

    


        



