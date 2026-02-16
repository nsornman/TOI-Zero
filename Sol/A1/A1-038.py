#ใช้ loop พิม * แล้วใช if เช็คตำแหน่งที่พิม X
num = int(input())
result = ""

for i in range(1, num+1):
    if i % 5 == 0:
        result += "X"
    else:
        result += "*"
print(result)