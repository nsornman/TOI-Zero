num = int(input())

values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
romans = ["M", "CM", "D", "CD", "C", "XC", "L", "XL","X", "IX", "V", "IV", "I"]

result = ""

i = 0
while num > 0:
    if num >= values[i]:
        result += romans[i]
        num -= values[i]
    else:
        i += 1

print(result)
