#======================= JSON = JAVASCRIPT OBECT NOTATION =============================

# import json 

###= this is a conversation of a JSON string to a python dictionery ===================== 
# x = '{"name" : "john", "age" : "21", "city" : "london"}'
# y = json.loads(x)

# print(y)
# print(type(y))

###= conversion from a python dictionery to a JSON string ======================

# a = {"name" : "john", 
#     "age" : "21",
#     "city" : "london"}

# b = json.dumps(a)
# print(b)
# print(type(b))

###= 

# y = [1, "jonny", True, False]
# x = json.dumps(y)
# print(x)
# print(type(x))

#=========== TYPE OF JSON STRING ======================

# print(json.dumps(["apple","banana"]))
# print(json.dumps(("apple","banana")))
# print(json.dumps(("Hello")))
# print(json.dumps(42))
# print(json.dumps(365.78))
# print(json.dumps((True)))
# print(json.dumps((False)))
# print(json.dumps((None)))



#==========================================================================

# import camelcase

# v = camelcase.CamelCase()
# text = "hello world"
# print(v.hump(text))

