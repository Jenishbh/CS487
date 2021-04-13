


class Student:
    def __init__(self, studentName):
        self.__studentName=studentName
        

    
    @property
    def studentName(self):
        return self.__studentName
    @studentName.setter()
    def studentName(self, studentName):
        self.__studentName=studentName


    

    def addHWScore(self, score):
        pass

    def addExamScore(self, score):
        pass




    class Course:
        def __init__(self, courceTitle, courceNo):
            self.__courceTitle=courceTitle
            self.__courceNo=courceNo

        @property
        def courceTitle(self):
            return self.__courceTitle

        @property
        def courceNo(self):
            return self.__courceNo


        
        def addStudent(self):
            pass

