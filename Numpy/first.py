import numpy 

# array = num.array([1,2,3,4,5])         # CREATION OF ARRAY USING NUMPY ===================================

# print(array)
# print(type(array))

# print(num.__version__)

#===================== ARRAYS DIMENSIONS =================================

# #THIS IS 0-D ARRAY
# array_0D = numpy.array(52643)
# print(array_0D)           
# print(array_0D.ndim)

# # THIS IS 1-D ARRAY
# array_1D = numpy.array([1,2,3,4,5,6,7,8])
# print(array_1D)
# print(array_1D.ndim)

# # THIS IS 2-D ARRAY
# array_2D = numpy.array([[1,2,3],[4,5,6]])
# print(array_2D)
# print(array_2D.ndim)

# # THIS IS 3-D ARRAY
# array_3D = numpy.array([[[1,2,3],[4,5,6],[7,8,9]]])
# print(array_3D)
# print(array_3D.ndim)

# THIS IS MULTIPLE DIMENSIONS USES 
# array = numpy.array([1,2,3,4,5], ndmin=6)
# print(array)
# print("The number of dimension in array is :", array.ndim)

#===============================

# arr = numpy.array([1,3,5,7,9,])
# print(arr[3])
# print(arr[3]+arr[2])

# ar = numpy.array([[1,3,5,7,9],[2,4,6,8,10]])
# print(ar[1,3])
# print(ar[0,4])


#============================= Accessing the block and indexing the arrays =========================================

# Array indexing in 1-D

# array = numpy.array([1,2,3,4,5])
# print(array[0])

# Array indexing in 2-D

# array2 = numpy.array([[1,2,3],[4,5,6]])
# print(array2[0,1])

# Array indexing in 3-D

# array3 = numpy.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]]) 
# print(array3[1,1,2])

# ====================== SLICING THE ARRAYS ===========================

# # 1-D

# array = numpy.array([1,2,3,4,5])
# print(array[1:4])

# # 2-D

# array1 = numpy.array([[1,2,3],[5,6,7]])
# print(array1[0:2,1:3])

# # 3-D

# array2 = numpy.array([[1,2,3],[4,5,6],[7,8,9]])
# print(array2[1:3,0:3])




