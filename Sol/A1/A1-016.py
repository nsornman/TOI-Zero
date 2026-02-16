number = int(input())

if len(str(number)) == 8:
    if str(number)[2] == "1" and str(number)[3] == "6":
        print("yes")
    else:
        print("no")
else:
    print("no")