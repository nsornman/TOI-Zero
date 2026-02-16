num = int(input())
# min_num = 0

#1
# for i in range(num):
#     nums = int(input())
#     if i == 0:
#         min_num = nums
#     else:
#         if nums < min_num:
#             min_num = nums
# print(min_num)

#2
min_num = 10**9
for i in range(num):
    nums = int(input())
    if nums < min_num:
        min_num = nums
print(min_num)