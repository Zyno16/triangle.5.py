l = int(input("enter the number"))
for i in range (1,l+1):
    for j in range(1,l+1):
        if i == 1 or j == 1 or i == j or i == l or j == l or j == l-i+1:
            print("*",end ="")
        else:
            print(" ",end ="")

    print()
    