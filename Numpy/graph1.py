import matplotlib.pyplot as plt
import seaborn  as sns
import random
import numpy as np

#=================== LINE CHART ===================

# x = [1,2,3,4,5]
# y = [10,20,35,40,45]

# plt.plot(x,y)
# plt.show()

#======================= CUSTOMIZE CHART ========================

# x = [1,2,3,4,5,6,7]
# y = [10,20,35,40,45,55,60]

# plt.figure(figsize=(4,3)) # it will give the figure size of chart
# plt.plot(x,y, color="pink",marker="o",linestyle="dashed", linewidth="2", markersize="12")
# plt.title("This is Customize chart")
# plt.xlabel("This is label to x axis")
# plt.ylabel("This is label to y axis")
# plt.show()

#========================== Advanced line chart - multiple lines & legends =========================================

# x = [1,2,3,4,5]
# y1 = [10,20,25,35,45]
# y2 = [20,20,35,45,65]

# plt.plot(x,y1, label = "Sale 2024", color="green",marker="o",linestyle="dashed", linewidth="2", markersize="12")
# plt.plot(x,y2, label = "Sale 2025", marker ="o")
# plt.title("Dhurandhar Sale Comparision 2024 & 2025")

# plt.xlabel("Month")
# plt.ylabel("Sales")

# plt.legend()
# plt.show()


#============================================================================================================

# Subjects = ["Hindi", "English", "Maths", "Science", "Social Science"]
# Rohit = [55,63,75,85,50]
# Mohit = [85,65,56,85,74]

# plt.plot(Subjects,Rohit, label = "Rohit Marks", color="green",marker="o",linestyle="dashed", linewidth="2")
# plt.plot(Subjects,Mohit, label = "Mohit Marks", marker ="o", color="red")
# plt.title("STUDENT RESULT")

# plt.xlabel("SUBJECTS")
# plt.ylabel("STUDENTS")

# plt.legend()
# plt.show()

#=============================== Bar Chart ===================================

# x = [1,2,3,4,5]
# y = [10,20,35,45,50]
# plt.bar(x,y)
# plt.title("Bar Chart")
# plt.show()

# =================================================================

# x = ["JK","Ayush","Dev","Meenu","Varsha","Vanshika","Rohit","Deepak","Savitri","Bhavishya"]
# y = [10,20,35,55,50,55,35,75,50,90]
# color = ["red","orange","blue","blue","blue","blue","blue","blue","blue","green"]
# plt.bar(x,y, color=color , width=0.5)
# plt.title("Bar Chart")
# plt.show()

#==================== HISTOGRAM CHART ==============================

# data = [random.randint(1,100) for i in range(100)]

# plt.hist(data, bins = 5)
# plt.title("Histogram Example")
# plt.show()

#======================== PIE CHART ================================

# categories = ["A","B","C","D","E"]
# sales = [10,20,55,35,45]
# plt.pie(sales, labels=categories, autopct='%1.1f%%')
# plt.title("pie chart example")
# plt.show()

#================== SCATTER PLOT =============================

# y1 = [10,20,30,35,45]
# y2 = [20,30,35,40,45]

# plt.scatter(y1,y2)
# plt.title("Scatter Plot Example")
# plt.show()

#========= SUB PLOTS ------ USED TO SHOW MULTIPLE CHARTS IN ONE FIGURE ===========================

#========= DATA -- 1 ===============

# categories = ['monday','tuesday','wednesday','thursday','friday']
# sales = [10,20,55,35,45]

# #========= DATA -- 2 ===============

# y1 = [10,20,30,35,45]
# y2 = [20,30,35,40,45]

# plt.figure(figsize=(4,6))

# ##========= first plot -- bar chart =============

# plt.subplot(1,2,1)         # row , colums , position 

# plt.bar(categories,sales)
# plt.title("Daily sales")
# plt.xlabel("Week Day")
# plt.ylabel("Sales")

# ##========= second plot -- scatter chart =============

# plt.subplot(1,2,2)         # row , colums , position 

# plt.scatter(y1,y2)
# plt.title("Users Example")
# plt.xlabel("User1")
# plt.ylabel("User2")
# plt.show()

# ================== INTRODUCTION OF GRID =============================

x = np.array([1,2,3,4,5,6,7,8,9,10])
y = np.array([10,15,25,30,40,45,55,65,75,80])
plt.title("West Bengal VS Tamil Nadu Polls")
plt.xlabel("Months")
plt.ylabel("Polls")
plt.plot(x,y, marker='o', linestyle='dashed', color='purple', linewidth=2, markersize=5)
plt.grid(linestyle='--',color='blue',linewidth=0.5)
plt.show()

