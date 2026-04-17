#======================= FILE HANDLING ===============================

# ========== OPEN A NEW FILE =========

# file = open("file.txt","r")

# print(file.read())

# ============= CLOSE FILE ==============

# file.close()

# print(file.read())

#============ SHORT FORM FOR READ FILE ===============

# with open("file.txt") as f:
#     print(f.read())

#=========== READLINE NOT COMPLETE PARAGRAPH ================

# with open("file.txt") as f:
#     print(f.readline())
#     print(f.readline())
#     print(f.readline())

# ============= WRITE A FILE WITH THE APPEND METHOD ===========

# with open("file.txt","a") as f:
#     f.write("This is a new line added to the file.\n")
# with open("file.txt","r") as f:
#     print(f.read())

#============= OVERWRITEING THE FILE WITH THE "w" METHOD =============

# with open("file.txt","w") as f:
#     f.write("OOPs! I Have Overwriting the whole file.\n")
# with open("file.txt") as f:
#     print(f.read())

#=============== CREATE A NEW FILE ======================

# f = open("filehandling.txt","x")
# x = open("formating.txt","x")

