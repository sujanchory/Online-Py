a=list(map(int,input().split()))
c=0
for i in range(len(a)):
    for j in range (i,len(a)):
        if a[i]==a[j]and i<j:
            print(i,j)
            c+=1
print(c)
