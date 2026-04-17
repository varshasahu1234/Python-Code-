# ================== PYTHON FUNCTION ====================================

# def myfunction():
#     print("This is my function.")
# myfunction()

# # ======================= Multiple print ======================


# def myfunction():
#     print("This is my function.")
# myfunction()
# myfunction()
# myfunction()
# myfunction()
# myfunction()
# myfunction()
# myfunction()
# myfunction()
# myfunction()
# myfunction()
# myfunction()
# myfunction()
# myfunction()
# myfunction()
# myfunction()
# myfunction()
# myfunction()
# myfunction()
# myfunction()
# myfunction()
# myfunction()


# ==================== TEMPERATURE CONVERTER ==================

# def temperatureconverter(x):
#     celsicus = (x - 32) * 5/9
#     print(celsicus)
#     return celsicus

# print(temperatureconverter(50))

#==================== GREET USER ==================================

# def greetuser(name):
#     print("Hello " + name + ", welcome to python programming.")

# greetuser("varsha")

# ========================= PASS STATEMENT =============================

# def passfunction():
#     pass

# passfunction()

# ============================= ADD NUMBER ========================

# def add_show(a, b):
#     print(a+b)

# def add_two_num(a, b):
#     return a+b

# # calling the function ===================

# x = add_show(5, 10)
# print(x)

# y = add_two_num(5, 10)
# print(y)

# ============================= MULTIPLE ARGUMENTS =================================

# def newFunction(name):
#     print("Hello "+ name)

# newFunction("Varsha")
# newFunction("Meenu")
# newFunction("Rashmi")

# ========================= PARAMETERS AND ARGUMENTS ===========================

# def teachstudent(subject):  # PARAMETER
#     print("Today we are learning " + subject)

# teachstudent("python")  # ARGUMENT

# ====================== MULTIPLE PARAMETER AND ARGUMENTS -========================

# def joinname(fname, lname):
#     print(fname + " " + lname )

# joinname("John", "Doe")

# ========================= DEFAULT PARAMETER VALUES ================================

# def greet(name, greeting = "Hello"):
#     print(greeting + " " + name)

# greet("Alice")        # User default greeting
# greet("Bob", "Hi")    # Overrides default greeting

# =================== PUTTING THE ARGUMENT VALUE =============================

# def newFunction(name, animal):
#     print("I have a ," ,animal)
#     print("My " +animal + " name is " +name)

# newFunction( animal = "dog", name = "jackey")

# ================= PASSING DIFFERENT DATA TYPE OF A FUNCTION ===============================

# def myfunction(fruits):
#     for fruit in fruits:
#         print(fruit)

# myfruits = ["apple","banana","mango"]
# myfunction(myfruits)

# ============== FUNCTIONS CAN PASS VALUES USING THE RETURN STATEMENT ===================

# def add(a, b):
#     return a + b

# result = add(5, 10)
# print(result)


# ====================== NONE FORMATE =========================

# def add_two_num(a,b):
#     result = a + b
#     print(result)

# x = add_two_num(5,10)
# print(x)

# ============================== ARGS AND KWARGS =========================

# def myfunction( *alphabets ):
#     print("The first alphabet is " + alphabets[2])

# myfunction("A" , "B" , "C")

# ======================= GREETING NAME ===============================

# def greeting_user(*names):
#     for name in names:
#         print("Hello", name)

# greeting_user("Varsha", "Meenu", "Rashmi", "Vanshi")

#===========================================

# def myfunction(*numbers):
#     total = 0 
#     for number in numbers:
#         total += number
#     return total


# print(myfunction(1,2,3,4,5,6))
# print(myfunction(10,20,30,40))
# print(myfunction(5))

# ====================== FINDING THE MAXIMUM NUMBER ===============================

# def findmax(*numbers):
#     if len(numbers) == 0:
#         return None
#     maximum_Number = numbers[0]
#     for num in numbers:
#         if num > maximum_Number:
#             maximum_Number = num
#     return maximum_Number

# print(findmax(5,62,41,32,12,85,6))

#=================== MULTIPLE KWARGS =========================

# def multiple(**member):
    # print("His first name is " + member["fname"] + " and last name is " + member["lname"])

# multiple(fname = "Varsha", lname = "sahu")
# multiple(fname = "Meenu", lname = "jaiswal")

#======================= DIFFERENT TYPES OF PARAMETER ==========================

# def mydifferent(title, *agrs, **kwargs):
#     print("Title: " + title)
#     print("Agrs: " ,agrs)
#     print("kwargs: " ,kwargs)

# mydifferent("My Function", 1,2,3, name = "Alice", age = 30)

#================================================================================================

# birth_year= int(input("Enter your birth year: "))

# def agefunction(birth_year):
#     x= (2026-birth_year)
#     # print("You will get current year age:",x)
#     return x

# print(agefunction(birth_year))

#======================== LAMBDA FUNCTION =============================

# single line operation ===========================

# def myfunction(n):
#     return lambda a : a*n-50

# myfirstnum = myfunction(12)
# mysecondnum = myfunction(9)

# print(myfirstnum(11))
# print(mysecondnum(12))

# ================ iterables ============================

# mylist = [1,2,3,4,5,6]
# doubled = map(lambda x : x*2, mylist)
# print(list(doubled))

#====================================================

# mylist = [1,2,3,4,5,6,7,8,9,10]
# even_numbers = filter(lambda x : x%2 == 0, mylist)
# print(list(even_numbers))

#================ RANGE =================================

# mylist = [1,2,3,4,5,6,7,8,9,10]

# print(list(range(1,8,2)))   # range(start,stop,step)

# ============== MEMBERSHIP TESTING IN A RANGE ================================

# mylist = [1,2,3,4,5,6,7,8,9,10]

# print( 5 in mylist)
# print( 15 in mylist)

#=================================================================

# r = range(1,10,2)
# print(len(r))

