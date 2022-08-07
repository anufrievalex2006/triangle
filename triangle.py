row = 10; sp = row-1
for i in range(row):
    for j in range(sp):
        print(" ",end="")
    for j in range(i+1):
        print("* ",end="")
    sp -= 1
    print("")
