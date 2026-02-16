inchar = input()
digit = input()
char = "H"
if inchar == char:
    if digit == "4567":
        print("safe unlocked")
    else:
        print("safe locked - change digit")
elif inchar != char and digit == "4567":
    print("safe locked - change char")
else:
    print("safe locked")