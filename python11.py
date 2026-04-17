#============= DECLEAR A SET USING CURLY BRACES ===================
# vars = {"apple", "banana", "cherry", "mango"}
# print(vars)

# #=== set can not be declear duplicate item it will automatically remove the duplicate items=======

# var = {"red", "green", "yellow", "blue", "pink", "green"}
# print(var)

# # ture and 1 are considereed the same in python ====================

# myset = {True, 1, "banana", "cherry", "apple", "mango"}
# print(myset)

#=======================
# myset ={1, True, 2, 3, 4}
# print(myset)

#========================
# myset = {True, 1, True, False,0 ,True,1 , False, 0}
# print(myset)

#======== declear a set using the braces and get it's length using len() function

# var = {"red", "green", "yellow", "blue", "pink", "green"}
# print("The lenght of x set is:",len(var))

# var = {"red", "green", "yellow", "blue", "pink", "green"}
# print(type(var))

#========== declear a set using the set() constructure========

# vars = set(("apple", "banana", "cherry", "mango"))
# print(vars)

# ============= iterating through a set using the for loop================

# x = {"red", "green", "yellow", "blue", "pink", "green"}
# for y in x:
#     print(y)

#=================================

# vars = {"red", "green", "yellow", "blue", "pink", "green"}
# if "yellow" in vars:
#     print("yes, 'apple' is in this vars")
# else:
#     print("No, 'apple' is not in this vars")

#============================================

# vars = {"red", "green", "yellow", "blue", "pink", "green"}
# print("yellow" in vars)

#============= ADD METHOD================

# vars = {"red", "green", "yellow", "blue", "pink", "green"}
# vars.add("purple")
# print(vars)

#====================== UPDATE METHOD =====================
# myset = {"mango", "apple", "banana"}
# otherset = {"berry", "cherry", "kiwi"}
# otherset.update(myset)
# print(otherset)


#=============================================-======================

# myset = {"mango", "apple", "banana"}
# otherset = ["berry", "cherry", "kiwi"]
# myset.update(otherset)
# print(myset)

#=========================== REMOVE ITEM FROM THE SET ============================

# vars = {"red", "green", "yellow", "blue", "pink", "green"}
# vars.remove("pink")
# print(vars)