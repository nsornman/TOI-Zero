temp = int(input())
un = input()

if un == "C":
    if 0 < temp < 100:
        print("liquid")
    elif temp >= 100:
        print("gas")
    else:
        print("solid")
elif un == "F":
    if 32 < temp < 212:
        print("liquid")
    elif temp >= 212:
        print("gas")
    else:
        print("solid")