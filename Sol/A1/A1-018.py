num = int(input())

if 1 <= num <= 9:
    i = 0
    result = ""
    while i < num:
        result += "I"
        i += 1 
    print(result)
else:
    print("Error : Out of range")