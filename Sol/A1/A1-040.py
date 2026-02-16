cal = {1: 100, 2: 120, 3: 200, 4: 60}

total = 0

while True:
    menu = int(input())
    
    if menu == 5:
        print("Bye Bye")
        print("Total Calories:",total)
        break
    
    if menu in cal:
        total += cal[menu]