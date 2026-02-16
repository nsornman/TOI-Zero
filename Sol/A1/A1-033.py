vowels_found = 0
a = int(input())

vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

for i in range(a):
    char = input()
    if char in vowels:
        vowels_found = vowels_found + 1
print(vowels_found)