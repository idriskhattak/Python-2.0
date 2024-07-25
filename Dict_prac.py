# Store followinf word meanings in a python dictionary
# table : "a piece of furniture", " list of facts & figures"
# cat : "a small animal"

# dic = {
#     'table': ["a piece of furniture","list of facts & figures"],
#     'cat': "a small animal"
# }

# print(dic)

"""
WAP to enter marks of 3 subjects from the user and store them in a dictionary.
Start with empty dictionary & add one by one. User subject name as key &
marks as value. 
"""
# dic.update method can be used for that

marks = {}

x1 = int(input('Enter phy : '))
marks.update({"phy" :x1})

x2 = int(input('Enter math : '))
marks.update({"math":x2})

x3 = int(input('Enter chem :'))
marks.update({"chem ":x3})

print(marks)