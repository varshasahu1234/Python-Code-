# ============================ JOIN SETS USING MULTIPLE METHOD ==============================

# set1 = {"a", "b", "c"}
# set2 = { 1, 2, 3}
# set3 = set1.union(set2)
# print(set3)

#====== join multiple set using union() method ==========================

# set1 = {"a", "b", "c"}
# set2 = { 1, 2, 3}
# set3 = {"x", "y", "z"}
# x = set1.union(set2,set3)
# print(x)


# ======================== another method to join multiple set using | operator ==============

# set1 = {"a", "b", "c"}
# set2 = { 1, 2, 3}
# set3 = {"x", "y", "z"}
# x = set1 | set2 | set3
# print(x)


#=========== merge sets and tuple using union() method =====================

# set1 = {"appple", "banana", "orange"}
# tuple1 = (1, 2, 3)
# x = set1.union(tuple1)
# print(x)

#====== join multiple set using update() method ==========================

# 1 ==============
# set1 = {"apple", "mango", "banana", "orange"}
# set2 = {"red", "blue", "green", "yellow"}
# set1.update(set2)
# print(set1)

# 2 =============
# set1 = {"apple", "mango", "banana", "orange", "red", "blue"}
# set2 = {"red", "blue", "green", "yellow", "mango", "banana"}
# set1.update(set2)
# print(set1)


#============================== INTERSECTION OF SETS ===========================

# 1=======================
# set1 = {"apple", "mango", "banana", "orange"}
# set2 = {"green", "blue", "yellow", "Mango", "orange"}
# x = set1.intersection(set2)
# print(x)

# 2 =========================

# set1 = { 0 ,True, "banana", 1 , "c", "mango"}
# set2 = { 1 , True, False,  "microsoft", "Apple" ,"c"}
# set3 = set2.intersection(set1)
# print(set3)

#====================== Symmetric difference of sets==========================

# set1 = {"apple", "mango", "banana", "orange"}
# set2 = {"green", "blue", "yellow", "Mango", "orange"}
# set3 = set1.symmetric_difference(set2)
# print(set3)

#======== symmetric difference_update() method ======================

# set1 = {"apple", "mango", "banana", "orange", "green"}
# set2 = {"green", "blue", "yellow", "Mango", "orange"}
# set1.symmetric_difference_update(set2)
# print(set1)

# Creating a frozen set using the frozenset() constructor================

# myfrozenset = frozenset(["apple", "banana", "cherry"])
# print(myfrozenset)


#---------------------------------------------

# x = input("Enter your name:")
# print(x)


#--------------------------------------

# x = int(input("Enter your first number:"))
# y = int(input("Enter your second number:"))
# z = (x//y)
# print(z)


#----------------------------------------
# x = int(input("Enter your first number:"))
# y = int(input("Enter your second number:"))
# z = (x+y)
# print(z)