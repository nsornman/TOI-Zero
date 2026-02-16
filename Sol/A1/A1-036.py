#1
num = int(input())
mod = num%10 #หารเอาเศษ
quo = num//10 #หารไม่เอาเศษ

if mod != 0:
        num = num - mod

for i in range(quo+1):
    print(num - 10*i, end=" ")

#2
# num = int(input())

# start = num - (num % 10)

# for i in range(start, -1, -10):
#     print(i, end=" ")
