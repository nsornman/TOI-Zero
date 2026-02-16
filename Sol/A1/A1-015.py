name = input()
surename = input()
age = int(input())

name_len = len(name)
surename_len = len(surename)

if name_len > 5 and surename_len > 5 :
    print(name[:2] + surename[-1] + str(age))
else:
    print(name[0] + str(age) + surename[-1])