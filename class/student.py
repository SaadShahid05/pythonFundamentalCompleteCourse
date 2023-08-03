class student:
    def __init__(self, name, grade) -> None:
        self.name = name
        self.grade = grade
    
    def getName(self):
        return self.name
    
    def printGrade(self):
        return self.grade

student1 = student("Saad", 6)
student2 = student("Ahmad", 5)
student3 = student("Shafat", 2)

print(student1.getName())
print(student2.getName())
print(student3.getName())

print(student1.printGrade())
print(student2.printGrade())
print(student3.printGrade())

print(student1.name)
print(student2.name)
print(student3.name)

