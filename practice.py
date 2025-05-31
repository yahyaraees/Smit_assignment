# Sawal: Kya function mein parameter dalna zaroori hai?
# Nahi, har function mein parameter dalna zaroori nahi hota.
# Lekin jab function ko kuch data ke sath kaam karna ho, tab parameter zaroori hota hai.
    #  ///////////////

#    Agar function same kaam har baar karega, to parameter optional hai.

# def greet():
#   print("hello world")s
# greet()     
# greet()     
# greet()     



   

#    Agar function har baar alag input ke sath kaam karega, to parameter zaroori hai.


# def fruit(flavor):
#   print(f'{flavor} is good flavor') 

# fruit('papaya')
# fruit('fajita')






# def fruit(flavor):
#     print(f'{flavor} i good has is good '  )


# fruit('papaya')
# fruit('fajita')



# class Person:
#     def __init__(self, name):
#         self.name = name

# p1 = Person("Ali")
# p2 = Person("Ahmed")
# print(p1.name)\\\



# class User:
#     def __init__(self, name):
#         self.name = name

# u1 = User("Yahya")
# u1.name = "Rais"
# print(u1.name)


# Fark (Difference):
# Attribute batata hai object “kya hai” (uski properties, jaise color, size).
# Method batata hai object “kya kar sakta hai” (uske actions, jaise chalna, rukna).
# Ek aur misaal (Real-life):
# Object: Ek insaan.
# Attributes: Uska naam (Rahul), umar (25), height (5.8 feet).
# Methods: Chalna, bolna, khaana.


# class student:
#   def __init__(self, name):
#     self.name = name

# s1 = student("yahya") 



# class student:
#     school_name = "muslim public school"

#     def __init__(self, name):
#        self.name = name

# s1 = student("ali")     
# s2 = student("zuhaib")  

# print(s1.school_name) 
# print(s2.school_name) 
# print(s1.name) 
# print(s2.name) 


# class Person:
#     def __init__(self, name):
#         self.__name = name  # private variable

#     def show(self):
#         print(f"Name is {self.__name}")       
# class Animal:
#     def sound(self):
#         print("Some sound")

# class Dog(Animal):
#     pass

# d = Dog()
# d.sound()       


class Student():
    def __init__ (self ,name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def show(self):
        print(f' My name is {self.name} : ----- My  age is {self.age} : -----  My grade is {self.grade}')
students = [
    Student('Yahya', 19, 'A'),
    Student('Hasnain', 29, 'B'),
    Student('Osama', 29, 'B'),
    Student('Huzaifa', 29, 'B'),
    Student('Anas', 29, 'B'),
    Student('Mohib', 29, 'B'),
    Student('Mohib', 29, 'B'),
    Student('Mohib', 29, 'B'),
    Student('Mohib', 29, 'B'),
    Student('Mohib', 29, 'B'),
    Student('Mohib', 29, 'B'),
    Student('Mohib', 29, 'B'),
    Student('Affan', 29, 'B'),
    Student('Abdullah', 29, 'C'),
    Student('Abdullah', 29, 'C'),
    Student('Abdullah', 29, 'C'),
    Student('Abdullah', 29, 'C'),
    Student('Abdullah', 29, 'C'),
    Student('Abdullah', 29, 'C'),
]

for s in students:
    s.show()




       
        