class Person:
    # creating constructer or init method
    def __init__(self, name, age, gender, profession) -> None:
        self.name = name
        self.age = age
        self.gender = gender
        self.profession = profession

    def show(self):
        print(f"name = {self.name}, age = {self.age}, gender = {self.gender}, profession = {self.profession}")

#creating objects
person1 = Person("Saad", 18, "Male", "Student")
person2 = Person("Sahal", 16, "Male", "Student")
person3 = Person("Dawood", 20, "Male", "Student")
person4 = Person("Aisha", 99, "Female", "Grand mother")
person5 = Person("Maryam", 5, "Male", "Child")

person1.show()
print()
person2.show()
print()
person3.show()
print()
person4.show()
print()
person5.show()
print()
