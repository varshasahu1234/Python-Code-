# Inharitence is a fundamental concept in object-oriented programming (oop) that allow a new class.

# class person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def introduction(self):
#         print(f"Hello!, My Name is {self.name} and I am {self.age} years old.")

# class Student(person):
#     pass

# x = Student("Alice", 30)
# x.introduction()

# class Student:
#     def __init__(self,name,roll_no,marks):
#         self.name=name
#         self.roll_no=roll_no
#         self.marks=marks
        
#     def per(self):
#         print(f"student name is : {self.name} roll no. : {self.roll_no}  percentage is {self.marks/500*100}")    

# p1=Student("wilson",1,400)
# p1.per()


#  Polymorphism.........................................


# class Car:
#     def __init__(self,name,max_speed):
#         self.name=name
#         self.max_speed=max_speed

#     def move(self):    
#        print("drive")


# class Boat:
#     def __init__(self,name,max_speed):
#         self.name=name
#         self.max_speed=max_speed

#     def move(self):   
#        print("sail")


# class Plane:
#     def __init__(self,name,max_speed):
#         self.name=name
#         self.max_speed=max_speed

#     def move(self):  
#        print("fly")

# car1=Car("ford","234")              
# boat1=Boat("boat mcboatface","50km/hr")
# plane1=Plane("boeing","744")

# for x in (car1,boat1,plane1):
#         x.move()


# class circle:
#     def __init__(self,radius):
#         self.radius=radius
# class area(circle):
#     def  area1(self):
#         print(f"area of circle is {3.14*self.radius*self.radius}")     
# class pera(area):
#     def pera1(self):
#         print(f"circumferance of circle is {2*3.14*self.radius}")

# radius=int(input("enter the radius"))
# a=pera(radius)
# a.area1()       
# a.pera1()


#==========================================================================================

