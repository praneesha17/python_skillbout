class Student:
    def _init_(self,name,marks):
        self.__name= name
        self.__marks = marks
    #This function is used to set a name
    def set_name(self,name):
        self.__name = name
    #This function is used to get a name
    def get_name(self):
        return self.__name
    #This function is used to set marks
    def set_marks(self,marks):
        self.__marks = marks
    #this funtion is used to get marks
    def get_marks(self):
        if 0 <= marks<= 100:
            return self.__marks
        else:
            return "Error: Marks should be between 0 and 100."

name = input("Enter student name: ")
marks = int(input("Enter student marks: "))
student = Student()
student.set_name(name)
student.set_marks(marks)
print("Student name:",student.get_name())
print("Student marks:",student.get_marks())
