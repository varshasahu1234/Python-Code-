#============================================ PYTHON DICTIONERY =========================================
#=== Dictionery in python ================

# mydict = {"Name" : "Varsha",
#          "Age" : 20,
#          "City" : "Haridwar",
#          "Bangalore" : "City of Oceans"}
# print(mydict)

# # Access the value using the key =======================

# print(mydict["Name"])
# print(mydict["Age"])
# print(mydict["City"])
# print(mydict["Bangalore"])


# Duplicate keys are not allowed in the dictionery ========================

# mydict = {"Name" : "Varsha",
#          "Age" : 20,
#          "Age" : 25,
#          "Bangalore" : "City of Oceans"}
# print(mydict)

# Find the lenght of the dictionery ==============================

# mydict = {"Name" : "Varsha",
#          "Age" : 20,
#          "City" : "Haridwar",
#          "Bangalore" : "City of Oceans"}
# print(len(mydict))

# Dictionery with different data ============================================ 

# mydict = {"Name" : "Varsha",
#          "Age" : 20,
#          "City" : "Haridwar",
#          "Bangalore" : "City of Oceans",
#          "is_married" : False }
# print(mydict)

# The dictionery constructor can be used to create a dictionery =============

# mydict1 = dict(Name = "Varsha", Age = 20, City = "Haridwar", Bangalore = "City of Oceans", is_married = False)
# print(mydict1)

# ================ Access the dictionery items using the get() method ====================================

# mydict = {"Name" : "Varsha",
#          "Age" : 20,
#          "City" : "Haridwar",
#          "Bangalore" : "City of Oceans",
#          "is_married" : False }

# print(mydict.get("Name"))
# print(mydict.get("Age"))
# print(mydict.get("City"))
# print(mydict.get("Bangalore"))
# print(mydict.get("is_married"))

# =============== Access the dictionery items using the key() / value() method ============================================================

# mydict = {"Name" : "Varsha",
#          "Age" : 20,
#          "City" : "Haridwar",
#          "Bangalore" : "City of Oceans",
#          "is_married" : False }

# x = mydict.keys()
# print(x)

# y = mydict.values()
# print(y)

# ============================================================

# car = { "brand" : "Ford",
#         "Model" : "Mustang",
#         "year" : 1964 }

# x = car.values()
# car ["year"] = 2020
# print(x)

# ============== remove an item from dictionery using the pop() method ===========================================

# car = { "brand" : "Ford",
#         "Model" : "Mustang",
#         "year" : 1964 }

# car.pop("Model")
# print(car)

# car = { "brand" : "Ford",
#         "Model" : "Mustang",
#         "year" : 1964 }

# car.popitem()
# print(car)

# using the del keyword to remove the items from the dictionery =====================================

# car = { "brand" : "Ford",
#         "Model" : "Mustang",
#         "year" : 1964 }

# del car ["Model"]
# print(car)

# =========================== using the clear() method =============================================

# car = { "brand" : "Ford",
#         "Model" : "Mustang",
#         "year" : 1964 }

# car.clear()
# print(car)

# ======================== looping through a dictionery using the for loop ====================================

# car = { "brand" : "Ford",
#         "Model" : "Mustang",
#         "year" : 1964 }

# for x in car:
#     print(x)
#     print(car[x])

#===============================================

# for x in car.values():
#     print(x)

# for x in car.keys():
#     print(x)

#=================================================

# for x in car.items():
#     print(x)

# ======================== copy a dictionery using the copy() method ===========================

# car = { "brand" : "Ford",
#         "Model" : "Mustang",
#         "year" : 1964 }

# car1 = car.copy()
# print(car1)

# ======================== copy a dictionery using the dict() method ===========================

# car = { "brand" : "Ford",
#         "Model" : "Mustang",
#         "year" : 1964 }

# car1 = dict(car)
# print(car1)

# ====================== nested dictionery ==================================

# 1 =======================================

# myfamily = {
#             "child1":{
#                 "name" : "varsha",
#                 "year" : 2004
#             },
#             "child2":{
#                 "name" : "meenu",
#                 "year" : 2003
#             },
#             "child3":{
#                 "name" : "vanshi",
#                 "year" : 2005
#             },
# }

# print(myfamily)
# print(myfamily["child3"]["year"])


# 2 =================================================

# child4 = {
#         "name" : "nagesh",
#         "year" : 1998
#     }
# child5 = {
#         "name" : "ramesh",
#         "year" : 1996
#     }

# x = {
#     "child4" : child4,
#     "child5" : child5,
# }
# print(x)

# ============================= 