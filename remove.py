# =============== REMOVE FILE =============

import os

# os.remove("formating.txt")

#===================================

if os.path.exists("filehandling.txt"):
    os.remove("filehandling.txt")

else:
    print("The File does not exists.") 