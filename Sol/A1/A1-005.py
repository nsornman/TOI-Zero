#Sol1
# month = int(input(""))
# day = int(input(""))

# winter = (month == 1 or month == 2 or month == 3)
# spring = (month == 4 or month == 5 or month == 6)
# summer = (month == 7 or month == 8 or month == 9)
# autumn = (month == 10 or month == 11 or month == 12)

# if month == 3 and day >= 21:
#     print("spring")
# elif month == 6 and day >= 21:
#     print("summer")
# elif month == 9 and day >= 21:
#     print("autumn")
# elif month == 12 and day >= 21:
#     print("winter")
# elif winter:
#     print("winter")
# elif spring:
#     print("spring")
# elif summer:
#     print("summer")
# elif autumn:
#     print("autumn")

#Sol2
month = int(input())
day = int(input())

if (month == 3 and day >= 21) or (4 <= month <= 5):
    print("spring")
elif (month == 6 and day >= 21) or (7 <= month <= 8):
    print("summer")
elif (month == 9 and day >= 21) or (10 <= month <= 11):
    print("autumn")
else:
    print("winter")