#===================== NORMAL DISTRIBUTION ========================

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
#==============================================

# x = random.normal(size=(2,3))
# print(x)

#==========================================

# sns.displot(random.normal( size= 1000 ), kind='kde') 
# plt.show()

#======================= BINOMIAL DISTRIBUTION =====================

# data = {
#     "normal" : random.normal(loc=50, scale=5, size=1000),
#     "binomial" : random.binomial(n=100, p=0.5, size=1000)
# }
# sns.displot( data, kind = "kde" )
# plt.show()

#===================== POISION DISTRIBUTION =========================

# x = random.poisson( lam=2, size=10 )
# print(x)

# sns.displot(random.poisson(lam=2,size=1000))
# plt.show()

#======================================================================

# x = np.array([23,45,61,74,98,78,56,12,34,90])

# y = np.min(x)
# print(y)

# z = np.max(x)
# print(z)

# r = np.average(x)
# print(r)

#=======================================================


