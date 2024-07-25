# Include Key, Value pairs
# Mutable, Unordered
# Key msut be unique

Dict = {
    'name':'Idris',
    'age': 24,
    'height' : 5.8
}

print(Dict)

Dict['name'] = 'Khan' # ---> New value assin with the old key
print(Dict)

Dict['cast'] = 'Khattak' # ---> New key added in the same dict
print(Dict)

print(Dict['name']) # ---> Printing value using key