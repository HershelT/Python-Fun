#!/usr/bin/python3
import math; import random; import time

class StudentManager():
    def __init__(self, name, age, year):
        self.name = name
        self.age = age
        self.year = year
        self.grade = 0
        self.classes = []
        
    def setGrade(self, grade):
        self.grade = grade
    def setName(self, name):
        self.name = name
    def setAge(self, age):
        self.age = age
    def setYear(self, year):
        self.year = year
    def addClasses(self, classes):
        self.classes.append(classes)
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def getYear(self):
        return self.year  
    def getGrade(self):
        return self.grade
    def getClasses(self):
        return self.classes
    def getTotalGrade(self):
        grade = 0
        for classes in self.classes:
            grade += classes.getStudentGrade(self)
        grade = grade / len(self.classes)
        return grade
class createClass():
    def __init__(self, name, credits, types):
        self.name = name
        self.credits = credits
        self.types = types
        self.students = []
        self.teacher = "Pending Hire"
        self.hashGrade = dict()
    def addStudents(self, student):
        self.students.append(student)
        student.addClasses(self)
        self.hashGrade[student.getName()] = 0
    def setPeriod(self, period):
        self.period = period
    def setTeacher(self, teacher):
        self.teacher = teacher
    def setStudentGrade(self, student, grade):
        self.hashGrade[student.getName()] = grade
    def getName(self):
        return self.name
    def getCredits(self):
        return self.credits
    def getTypes(self):
        return self.types
    def getPeriod(self):
        return self.period
    def getStudents(self):
        return self.students
    def getTeacher(self):
        return self.teacher
    def getStudentGrade(self,student):
        return self.hashGrade[student.getName()]
    
class school():
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.allStudents = []
        self.curriculum = []
    def addCurriculum(self, curriculum):
        self.curriculum.append(curriculum)
    def getName(self):
        return self.name
    def addStudent(self, student):
        self.allStudents.append(student)
    def getLevel(self):
        return self.level
    def getStudentCount(self):
        return len(self.allStudents)
    def getStudents(self):
        return self.allStudents
    def getCurriculum(self):
        return self.curriculum
 
studentHershel = StudentManager("Hershel", 18, "Senior")
studentYonatan = StudentManager("Yonatan", 17, "Senior")
studentJonah = StudentManager("Jonah", 18, "Senior")

classAPUSH = createClass("AP US History", 12, "History")
classAPUSH.setPeriod(7)
classAPUSH.addStudents(studentHershel)
classAPUSH.setPeriod(2)
classAPUSH.setStudentGrade(studentHershel, 93)

classCS = createClass("Intro to C++", 8, "Science")
classCS.setPeriod(7)
classCS.addStudents(studentHershel)
classCS.setPeriod(6)
classCS.setTeacher("Mr. Chavel")
classCS.setStudentGrade(studentHershel, 90)

classAPLit = createClass("The Advent of Modern Literature", 8, "English")
classAPLit.setPeriod(8)
classAPLit.addStudents(studentHershel)
classAPLit.setTeacher("Mr. Matanky")
classAPLit.addStudents(studentYonatan)
classAPLit.setStudentGrade(studentYonatan, 100)
classAPLit.setStudentGrade(studentHershel, 99)

classStupidHead = createClass("School is Stupid", 16, "Social Study")
classStupidHead.setPeriod(10)
classStupidHead.addStudents(studentYonatan)
classStupidHead.setStudentGrade(studentYonatan, 69)
classStupidHead.setTeacher("Dr. Chavez")

classStats = createClass("AP Statistics for Dummies", 12, "Math")
classStats.setPeriod(4)
classStats.setTeacher("Someone's Mom")
classStats.addStudents(studentJonah)
classStats.setStudentGrade(studentJonah, 91)

icja = school("Ida Crown Jewish Academy", "High School")
icja.addCurriculum(classCS)
icja.addCurriculum(classAPUSH)
icja.addCurriculum(classAPLit)
icja.addCurriculum(classStupidHead)
icja.addCurriculum(classStats)
#(To Do) change period offering maybe for student instead of in class
# because it can be different for students

allStudents = []
for classes in icja.getCurriculum():
    for student in classes.getStudents():
        allStudents.append(student)
allStudents = set(allStudents)
for student in allStudents:
    icja.addStudent(student)
#chaning classCS
#(To Do) students need seperate grade for each class
#add the list of classes student is taking
#move around or add new functions

def printU(text):
    for i in text:
     if i.isspace() == False:
         print(i+"\u0332",end='')
     else:
         print(i, end = '')
    print("")
def getStudentClass(name, what):
    for student in icja.getStudents():
        if name.lower() == student.getName().lower():
            if what == "class" or what == "classes":
                print(f"Classes for {student.getName()}:")
                for classes in student.getClasses():
                    print(f"{classes.getName()}, Grade: {classes.getStudentGrade(student)}")
            elif what == "year":
                print(f"Year: {student.getYear()}")
            elif "grade" in what or "total grade" in what:
                print(f"Total Grade: {student.getTotalGrade()}")
            elif "age" in what:
                print(f"Age: {student.getAge()}")
            else: 
                print("Wrong Input")
            print("")
            return True
    print("Person not in school\n")
    return False

leave =["exit", "leave", "break", "bye", "stop"]
print (f"\n\033[5mSchool: {icja.getName()}")
print(f"Student Count: {icja.getStudentCount()}\n")
for classes in sorted(icja.getCurriculum(), key= lambda s: s.getPeriod(), reverse = False) :
    print(f"\033[0;36m{classes.getName()}")
    print(f"\033[0;32mPeriod-{classes.getPeriod()}th")
    print(f"\033[0;34mTeacher: {classes.getTeacher()} ")
    printU("Students in class:")
    for students in classes.getStudents():
        print(f"\033[1m\033[0;30m{students.getName()}, Grade: {classes.getStudentGrade(students)}")
    print("\u001b[0m\n")
while True: 
    ask = input("what student do you want to check?")
    if ask.lower() in leave:
        print("leaving...")
        break
    askSecond = input("do you want to see classes, year, age, total grade?")
    print("")
    getStudentClass(ask, askSecond)
#(To Do) add a way to just type in classes, students and grades through text)
#(TO DO) ADD SEMESTER grades make an array that holds person object and semester

    
