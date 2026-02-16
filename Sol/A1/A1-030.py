n = int(input())
nums = list(map(int, input().split()))

i = 0
total = 0
result = ""
count = 0

while count < n:
    bigger = max(nums[i], nums[i+1])
    total += bigger
    
    if count == 0:
        result = str(bigger)
    else:
        result += " + " + str(bigger)
    
    i += 2
    count += 1

print(result + " = " + str(total))
