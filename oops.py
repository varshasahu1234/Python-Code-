# ============================== DEFINE A CLASS =================================================

# class Myclass:
    # x = 5
# print(Myclass)  # it will print the class name and the memory location of the class
# print(Myclass.x)  # it will print the value of x which is 5 



# ==== this is object creation in a class ====================================

# class anotherclass:
#     x = 7             # this is an attribute of the class
# h1 = anotherclass()   # creating an object of the class
# print(h1.x)           # it will print the value of x which is 7

#====================================================================

# class person:

    # def __init__(self,name,age):  # this is a constructor which is used to initialize the attribute of the class 
        # self.name = name     
        # self.age = age     
    # defining a method in the class
    # def myfunc(self):
        # print("Hello! my name is "+ self.name + " and I am " + str(self.age) + " years old.")
# p1 = person("Alice",20)
# del p1
# p1.myfunc()

#=========================================================================

# ============== TEA STALL =======================

# x = input("Enter your size of Cup: ")
# y = int(input("Enter your no. of cup: "))
# if x == "Large":
#         print(y*45)
# elif x == "Medium":
#         print(y*25)
# elif x == "Small":
#         print(y*15)
# else:
#     print("Invalid size")


#========================================

# total = 0

# while True:
#     print("\n------Tea Menu-------")
#     print("1. Small Tea - ₹15")
#     print("2. Medium Tea - ₹30")
#     print("3. Large Tea - ₹45")

# #======== Enter the Choice of Cup ================
#     choice = input("Enter cup size (small/medium/large): ").lower()
#     Quantity = int(input("Enter quantity: "))       # Enter the qunatity of cup

# # if else statement ===============
#     if choice == "small":
#         price = 15
#     elif choice == "medium":
#         price = 30
#     elif choice == "large":
#         price = 45
#     else:
#         print("Invalid choice! Try again.")
#         continue

#     amount = price * Quantity
#     total += amount

#     print("Added ₹", amount, "to total bill.")

#     more = input("Do you want to order more? (yes/no): ").lower()
#     if more != "yes":
#         break

# print("\n--------- Final bill ----------")
# print("Total Amount to Pay: ₹",total)
# if total > 1000:
#     x = str(input("Enter your coupen code: ")).lower()
#     if x == "ayush":
#         print("You got 25% Discount",total/100*25)
#         print("Total Amount to Pay: ₹",total-total/100*25) 
# print("Thank you! Visit Again!")



#==================================================================================

# class Chai:
#     pass

# class Chaitime:
#     pass

# print(type(Chai))
# print(type(Chaitime))

# ginger_tea = Chai()
# masala_tea = Chaitime()

# # del (ginger_tea)
# print(type(ginger_tea))


# print(type(ginger_tea) is Chai)
# print(type(ginger_tea) is Chaitime)
# print(type(masala_tea) is Chaitime)

#==========================================================================

# class Car:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year

#     def display_info(self):
#         print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}")
# car1 = Car("Toyota","Camry", 2020)
# car1.display_info()

#===========================================================================================================

# ======= Accessing the properties/ attributes of the class using the object. ==============================

# class Car:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year

# car1 = Car("Toyota","Camry", 2020)

# print(car1.brand)
# print(car1.model)
# print(car1.year)

# #========= modify the propertites/attributes of the class using the object ===========================

# # car1.year = 2021
# # print(car1.year)

# #=========== delete the propertites/attributes of the class using the object ==========================

# # del car1.brand
# # print(car1.brand)

# #============== Add new propertites/attributes of the class using the object ===========================

# car1.color = "Red"
# print(car1.color)

#==============================================================================================

# class person:

#     def __init__(self, name, age, city, country):
#         self.name = name
#         self.age = age
#         self.city = city
#         self.country = country
    
#     def __str__(self):
#         return f"Name: {self.name}, Age: {self.age}, City: {self.city}, Country: {self.country}"

# p1 = person("Shinchan", 5, "Korea", "Japan")
# print(p1)


