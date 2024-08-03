sent = "hello, this code is just to count vowels in a sentence"
vowels = ['a', 'e', 'i', 'o', 'u']

count = 0

for char in sent:
    if char in vowels:
        print(char,end = ',')
        count += 1

print(f"\nThe total vowels are :{count}")

