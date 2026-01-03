n=int(input("enter how many rows you need:"))
for i in range(n):
    for j in range(n):
        if i>=j:
            print("*",end=" ")
    print()
        
            
