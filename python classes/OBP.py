#Object Orientated Programming in Python
'''
# Exmaple 1:
class Dog:
	def __init__(self,name, age):
		self.name = name
		self.age = age


	def get_age(self):
		return self.age

	def get_name(self):
		return self.name

d = Dog("T
im", 5)
print(d.get_name())
print(d.get_age())
'''
'''
# Exmaple 2:
class Student:
	def __init__(self, name, age, grade):
		self.name = name
		self.age = age
		self.grade = grade

	def get_grade(self):
		return self.grade

class Course:
	def __init__ (self, name, max_students):
		self.name = name
		self.max_students = max_students
		self.students = []

	def add_student(self, Student):
		if len(self.students) < self.max_students:
			self.students.append(Student)
			return True
		return False
	def get_average_grade(self):
		value = 0
		for student in self.students:
			value += student.get_grade()

		return value / len(self.students)

s1 = Student("Tim", 19, 95)
s2 = Student("Bill", 19, 75)
s3 = Student("jill", 19, 80)

course = Course("Science", 2)
course.add_student(s1)
course.add_student(s2)

# print(course.add_student(s3))
print(course.get_average_grade())
'''


# Exmaple 3:

class Pet:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def show(self):
		print(f"I am {self.name} and I am {self.age} years old")
	def speak(self):
		print("")

class Cat(Pet):
	def __init__(self, name, age, color):
		super.__init__(name, age):
		self.color = color
	def speak(self):
		print("Meow")
	def show(self):
		print(f"I am {self.name} and I am {self.age} years old and c")
class Dog(Pet) :
	def speack(self):
		print("Bark")


p = Pet("Tim", 19)
p.show()
c = Cat("Bill", 15)
c.speak()


























