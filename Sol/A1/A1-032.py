num = int(input())

for i in range(3):
    stars = num - (2*i)
    
    if stars > 0:
        print("*" * stars)
    else:
        print()