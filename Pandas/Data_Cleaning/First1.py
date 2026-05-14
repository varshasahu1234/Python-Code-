# ============ DATA CLEANING ======================

# Data cleaning is the process of clearing the data and 

#============= What can be the bad Data ==================
# Missing values
# Duplicate values
# Empty Rows/Cells/Columns
# Wrong data type
# Inconsistant data

#"https://www.w3schools.com/python/pandas/data.js"

import pandas as pd

# data = pd.read_csv(r"C:\Users\NIELIT\Downloads\data (1).csv")
# # print(data.to_string())

# new_dt = data.dropna()
# print(new_dt.to_string())

#================= Removing the rows which contained nan value =========================

# data = pd.read_csv(r"C:\Users\NIELIT\Downloads\data (1).csv")
# data.dropna(inplace = True)
# print(data.to_string())

#=============== Adding the value in the Empty value =========================

# data1 = pd.read_csv(r"C:\Users\NIELIT\Downloads\data (1).csv")
# data1.fillna(258.5, inplace = True)
# print("After filling empty data :\n",data1.to_string())

#=============== Filling the missing values with the different values ============================

# data1 = pd.read_csv(r"C:\Users\NIELIT\Downloads\data (1).csv")
# data1.fillna({"Calories":540.5}, inplace=True)
# print("After Filling empty cells with different values: \n", data1.to_string())

# filling with location ===========

# data1 = pd.read_csv(r"C:\Users\NIELIT\Downloads\data (1).csv")
# data1.loc[17, "Calories"] = 240.6
# print("After filling empty cells with different values:", data1.to_string()) 

#================ Mean / Mode / Median ==============================

# # ---------------- mean -------------
# var = pd.read_csv(r"C:\Users\NIELIT\Downloads\data (1).csv")
# x = var["Calories"].mean()
# print("The mean value is:",x)

# var.fillna({"Calories": x}, inplace=True)
# print(var.to_string())

# # -------------- median ------------------------------
# var = pd.read_csv(r"C:\Users\NIELIT\Downloads\data (1).csv")
# x = var["Calories"].median()
# print("The median value is:",x)

# var.fillna({"Calories": x}, inplace=True)
# print(var.to_string())

# # ---------------- mode ----------------------

# var = pd.read_csv(r"C:\Users\NIELIT\Downloads\data (1).csv") 
# x = var["Calories"].mode()
# print("The mode value is:",x)

# var.fillna({"Calories": x}, inplace=True)
# print(var.to_string())


 