# Write a function to remove duplicates from a list.

def remove_dup(lst):
    return list(set(lst))

lst_1 = [1,1,1,2,3,4,4,5,6]

print(remove_dup(lst_1))