#============================== python tuple =============================
# create a tuple

# thistuple = ("apple", "banana", "mango", "orange", "cherry", "kiwi", "berry")
# print(thistuple)

#==================================================

# it will give the second index in tuple
# thistuple = ("apple", "banana", "mango", "orange", "cherry", "kiwi", "berry")
# print(thistuple[2])


#=========================================
# it will print the string "apple" not a tuple
# thistuple1 = ("apple")
# print(thistuple1)

# thistuple1 = ("apple",)
# print(thistuple1)

#====================================

# var = ("apple", 1, "banana", 2, "cherry")
# print(type(var))

#=========================================
# declearing the tuple with the help of the tuple() constructure

# var = tuple(("apple", "banana", "mango", "orange", "cherry", "kiwi", "berry"))
# print(var)


# var = tuple(("apple", "banana", "mango", "orange", "cherry", "kiwi", "berry"))
# print(var[-3])


# var = tuple(("apple", "banana", "mango", "orange", "cherry", "kiwi", "berry", 34, 45, 24, 56, 67, 89))
# print(var[-5:])

#======================================================================

# var = ("apple", "banana", "nielit", "mango", "cherry")

# if "nielit" in var:
#     print("Yes,nielit are present")
# else:
#     print("No,nielit are not present" )


#================================ UPDATE THE TUPLE ==============================
#  1 ============
# var = ("apple", "banana", "nielit", "mango", "cherry")
# y = list(var)
# y[2] = "kiwi"
# var = tuple(y)
# print(var)

#  2 ==================
# var = ("apple", "banana", "kiwi", "mango", "cherry")
# x = list(var)
# x.append("orange")
# var = tuple(x)
# print(var)

# 3 ====================

# var = ("apple", "banana", "cherry", "mango")
# y = list(var)
# x = ("orange", "berry", "pineapple", "papaya")
# y.extend(x)
# var = tuple(y)
# print(var)

# 4 =====================

# var = ("apple", "banana", "cherry", "mango")
# y = list(var)
# y.remove("banana")
# var = tuple(y)
# print(var)

# 5 ============================

# thistuple = ("apple", "banana", "cherry", "mango")
# del thistuple
# print(thistuple)

# =========================== ADD AN ITEM INTO THE TUPLE =======================

# var = ("apple", "banana", "cherry", "mango")
# y = ("orange",)
# var += y
# print(var)



#======================= UNPACKING THE TUPLE ===================================

#  1 ===========================================

# var = ("apple", "banana", "cherry", "mango")
# # unpacking a tuple / destructured method ================
# (a, b, c, d) = var
# print(a)
# print(b)
# print(c)
# print(d)

# 2 ============================

# thistuple = ("apple", "banana", "mango", "orange", "cherry", "kiwi", "berry")
# (x, y, z, *other) = thistuple
# print(x)
# print(y)
# print(z)
# print(other)


# ================================= FOR LOOP IN TUPLE ================================

# thistuple = ("apple", "banana", "mango", "orange", "cherry", "kiwi", "berry")
# for x in thistuple:
#     print(x)

# =================== LOOP THROUGH THE INDEX NUMBER OF THE TUPLE =============================

# thistuple = ("apple", "banana", "mango", "orange", "cherry", "kiwi", "berry")
# for y in range(len(thistuple)):
#     print(thistuple[y])


#=================== JOIN THE TUPLE ===============================

# tuple1 = ("a", "b", "c")
# tuple2 = (1 ,2, 3)
# tuple3 = tuple1 + tuple2
# print(tuple3)

# #============ MULTIPLE THE TUPLE ==================

# tuple1 = ("a", "b", "c")
# Y = tuple1 * 2
# print(Y)

#================== COUNT METHOD ======================

# thistuple = ("mango", "apple", "kiwi", "banana", "kiwi", "grapes", "kiwi")
# y = thistuple.count("kiwi")
# print(y)

# #=================== index method ====================

# thistuple = ("mango", "apple", "banana", "kiwi", "grapes")
# x = thistuple.index("kiwi")
# print(x)

 