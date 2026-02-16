f1_y = int(input())
f1_m = int(input())
f1_d = int(input())

f2_y = int(input())
f2_m = int(input())
f2_d = int(input())

if f1_y < f2_y:
    print("1")
elif f1_y == f2_y:
    if f1_m < f2_m:
        print("1")
    elif f1_m == f2_m:
        if f1_d < f2_d:
            print("1")
        elif f1_d == f2_d:
            print("0")
        else:
            print("2")
    else:
        print("2")
else:
    print("2")