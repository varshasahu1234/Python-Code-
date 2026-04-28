import numpy as np

#========== without ufunc ===========

# x = [1,2,3,4,5]
# y = [6,7,8,9,10]
# z = []

# for i,j in zip(x,y):
#     z.append(i+j)

# print(z)

#============ with ufunc =============

# x = [1,2,3,4,5]
# y = [6,7,8,9,10]
# z = np.add(x,y)
# print(z)

#=========== Create our own ufunc ===================

# def myadd(x,y,z):
#     return x+y+z

# xyz = np.frompyfunc(myadd,3,1)#----------------- np.frompyfunc("function","input","output")
# print(xyz([1,2,3,4,5],[6,7,8,9,10],[1,2,3,4,6]))

# print(type(np.add))

#=================== Check if a function is a ufunc or not by using the if/else ==============

# if type(np.add) == np.ufunc:
#     print("Add is ufunc")
# else:
#     print("Add is not ufunc")

# #=======

# if type(np.subtract) == np.ufunc:
#     print("Subtract is ufunc")
# else:
#     print("Subtract is not ufunc")

#===============================================

#=== ADDITION ===

# arr1 = ([1,2,3,4,5,6])
# arr2 = ([13,27,43,46,58,62])
# newarr = np.add(arr1,arr2)
# print("Addition is :",newarr)
# print(type(np.add))

# #=== SUBTRACTION ===

# arr1 = ([1,2,3,4,5,6])
# arr2 = ([13,27,43,46,58,62])
# newarr = np.subtract(arr1,arr2)
# print("Subtraction is :",newarr)
# print(type(np.subtract))

# #=== DIVISION ===

# arr1 = ([1,2,3,4,5,6])
# arr2 = ([13,27,43,46,58,62])
# newarr = np.divide(arr1,arr2)
# print("Division is :",newarr)
# print(type(np.divide))

# #=== MULTIPLICATION ===

# arr1 = ([1,2,3,4,5,6])
# arr2 = ([13,27,43,46,58,62])
# newarr = np.multiply(arr1,arr2)
# print("Multiplication is :",newarr)
# print(type(np.multiply))

# #==== POWER ====

# arr1 = ([1,2,3,4,5,6])
# arr2 = ([13,2,4,6,8,2])
# newarr = np.power(arr1,arr2)
# print("Power is  :",newarr)
# print(type(np.power))

#===== REMAINDER ====

# arr1 = ([19,52,35,46,57,63])
# arr2 = ([3,2,4,6,8,2])
# newarr = np.mod(arr1,arr2)
# print("Remainder is  :",newarr)
# print(type(np.power))

