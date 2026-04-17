#==============================================================

# var = [(input("Enter your list:"))]
# print(var)

#==================================================

# varlist = [(input("Enter your list:"))]
# varlist.append("pineapple")
# print(varlist)

#==================================================

# 31 ===========================================

# list2 = ["red", "green", "blue", "yellow", "pink"]
# list2.reverse()
# print(list2)

# 32 ========================================

# list2 = max([32, 34, 56, 67, 78, 98])
# print(list2)

# 33 ======================================

# list2 = min([32, 34, 56, 67, 78, 98])
# print(list2)

# 34 =========================================

# list2 = ["red", "green", "blue", "yellow", "pink", "blue", "black", "blue"]
# x = list2.count("blue")
# print(x)

# 35 ============================================

# list2 = ["red", "green", "blue", "yellow", "pink"]
# list1 = ["berry", "cherry", "mango", "apple"]
# x = list2 + list1
# print(x)

#  ==================================================================

# 36 =============================================

# mytuple = tuple((52,56,85,54,95))
# print(mytuple)

# 37 ===========================================

# mytuple = ("red", "green", "blue", "yellow", "pink")
# print(mytuple[0])


# mytuple = ("welcome", "to", "nielit", "this", "is", "python", "programming")
# print(mytuple[2])

# 38 =================================================

# mytuple = ("red", "green", "blue", "yellow", "pink")
# print(mytuple[-1])

# 39 ==================================================

# mytuple = ("red", "green", "blue", "yellow", "pink")
# print(len(mytuple))

# 40 ===========================================

# mytuple = ("red", "green", "blue", "yellow", "pink")
# y = list(mytuple)
# print(y)

# 41 =============================================

# var = {(input("Enter your list:"))}
# print(var)

# 42 =============================================

# varset = set((input("Enter your list:").split()))
# x = int(input())
# varset.add(x)
# print(varset)

# 43 ============================================

# varset = set((input("Enter your list:").split()))
# x = (input())
# varset.discard(x)
# print(varset)

# 44 ==========================================

# set1 = {"a", "b", "c", "d"}
# set2 = {"x", "y", "z"}
# set3 = set2.union(set1)
# print(set3)

# 45 ============================================

# set1 = {"a", "b", "c", "d"}
# set2 = {"x", "y", "z", "a", "b"}
# set3 = set1.intersection(set2)
# print(set3)

# 46 ====================================

# set1 = {"a", "b", "c", "d"}
# set2 = {"x", "y", "z", "a", "b"}
# set3 = set1.symmetric_difference(set2)
# print(set3)

# 47 ==========================================

# varset = set((input("Enter your list:").split()))
# var = input("Enter the string that you want to remove from the set:")
# varset.discard(var)
# print(varset)

# 48 =============================================

# varset = set((input("Enter your list:").split()))
# var = input("Enter the string that you want to remove from the set:")
# varset.remove(var)
# print(varset)

# 49 ========================================

# x = bool("")
# if x == False:
#     print("True, That is true statement")
# else :
#     print("False, That is incorrect statement")


#===========================================================

# x = int(input("Enter your number: "))

# if x%5 == 0 and x%8 ==0:
#     print("Yes it is divisible by 5,8")
# else:
#     print("No, it is not divisible by 5,8")

#========================================================

# x = int(input("Enter your number: "))

# if x>=18 :
#     print("eligible for vote")
# else:
#     print("not eligible for vote")

#==========================================================

# x = input("Enter your string: ")

# for i in x:
#     if i == "a":
#         print("a")
#     elif i == "e":
#         print("e")
#     elif i == "i":
#         print("i")
#     elif i == "o":
#         print("o")
#     elif i == "u":
#         print("u")
# else:
#     print("That is not vowel")

#==========================================================

# def greet(name):
#     print("Hello "+name+ " , Welcome to python programming")

# greet("varsha")
# greet("meenu")
# greet("vanshi")
# greet("priya")

#===========================================================

# x = str(input("Name: "))
# y = int(input("Class: "))
# z = int(input("Roll no.: "))
# a = str(input("Address: "))

# if y <= 12:
#     print(x)
#     print(y)
#     print(z)
#     print(a)
#     print("You have successfully enrolled")

# else:
#     print("You can not enrolled, your class should not be greater than 12 ")

#==================================================================================

# x = ["apple", "banana", "apple", "kiwi", "cherry","ram", "mango", "rasberry","apple","berry"]
# x = list(input("Enter your list: ").split())
# z = input("enter your element that you want to count: ")
# y = z.count(z)

# print(y)

#=======================================================

# x = ["apple", "apple", "banana","banana", "kiwi","kiwi", "mango", "mango"]




# x = int(input("Enter your first number: ")) 
# y = int(input("Enter your second number: ")) 

# z = input("Enter your operation: ") 

# if z == "+":
#     print(x+y)
# elif z == "-":
#     print(x-y)
# elif z == "*":
#     print(x*y)
# elif z == "/":
#     print(x/y)
# elif z == "%":
#     print(x%y)
# elif z == "//":
#     print(x//y)
# elif z == "**":
#     print(x**y)

# else:
#     print("Invalid operator")
    

#======================================================================

# x = ["apple","banana", "cherry", "kiwi", "orange", "mango"]
# x.pop(-1)
# print(x) 