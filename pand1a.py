import pandas as pd 
import numpy as np
# s = pd.Series([])
# print(s)

# s = pd.Series([12,34,54,67])
# print(s)

# data = np.array(["a","b","c"])
# s =  pd.Series(data)

# data={"a":0,"b":1}
# s = pd.Series(data)
# print(s)

#=================================================================================

# L = [14,35,45,33,78,56]
# # print(L)
# ds = pd.Series()
# print(ds)


data = {'Name':['Tom','Jack','Steve','Ricky','Rohan','Sohan'],
        'Age':[20,35,25,21,22,33],
        'Salary':[52000,60000,55000,45000,65000,55000]}
df = pd.DataFrame(data)
# print(df)
print(df.head())
print(df.tail())
df.rename(columns={"Salary":"Monthly_Salary"}, inplace=True)
print(df.rename(columns={"Salary":"Monthly_Salary"}))
print(df.shape)                                        # Number of Rows and Columns
print(df.columns)                                      #  Column Name
print(df.describe)                      





import pandas as pd 
import numpy as np
# s = pd.Series([])
# print(s)

# s = pd.Series([12,34,54,67])
# print(s)

# data = np.array(["a","b","c"])
# s =  pd.Series(data)

# data={"a":0,"b":1}
# s = pd.Series(data)
# print(s)

#=================================================================================

# L = [14,35,45,33,78,56]
# # print(L)
# ds = pd.Series()
# print(ds)


# data = {'Name':['Tom','Jack','Steve','Ricky','Rohan','Sohan'],
#         'Age':[20,35,25,21,22,33],
#         'Salary':[52000,60000,55000,45000,65000,55000]}
# df = pd.DataFrame(data)
# # print(df)
# print(df.head())
# print(df.tail())
# df.rename(columns={"Salary":"Monthly_Salary"}, inplace=True)
# print(df.rename(columns={"Salary":"Monthly_Salary"}))
# print(df.shape)                                        # Number of Rows and Columns
# print(df.columns)                                      #  Column Name
# print(df.describe())                      
# print(df.info())        
# print(df.to_csv('Sample.csv',index=False))





