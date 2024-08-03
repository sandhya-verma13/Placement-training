n=int(input("Enter the number of rows : "))
l=1
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end="")
    for k in range(0,i):
        if k==0 or 1==0:
            l=1
        else:
            l = l * (i - k)//k
        print(l,end="")
    print()
    
