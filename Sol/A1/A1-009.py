a = int(input())
b = int(input())

if a and b > 50:
    print("fail")
elif a >= 0 and b >= 0:
    if a+b >= 50:
        print("pass")
    else:
        print("fail")
else:
    print("fail")