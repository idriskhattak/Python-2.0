#WAP to ask the user to enter names of their 3 Favorite movides and store them in a list
# movies = []

# movies_1 = input('Enter the 1st movie name')
# movies_2 = input('Enter the 2nd movie name')
# movies_3 = input('Enter the 3rd movie name')

# list.append(movies_1,movies_2,movies_3)

# print(list)

list = []

for i in range(3):
    movies = input(f"Enter the number:{i+1} Favorite movies name :")
    list.append(movies)

print(list)

# The above are the rwo methods to solve the problem