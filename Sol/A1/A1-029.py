vowels_found = 0
a = input()

vowels = ["a", "e", "i", "o", "u"]

for i in range(len(a)):
    if a[i] in vowels:
        vowels_found = vowels_found + 1
print(vowels_found)