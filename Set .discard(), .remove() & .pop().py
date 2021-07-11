n = int(input())
s=set(map(int,input().split()))
for i in range(int(input())):
    c=list(input().split())
    if c[0]=="pop":
        s.pop()
    elif c[0]=='discard':
        s.discard(int(c[1]))
    elif c[0]=='remove':
        s.remove(int(c[1]))
sm=0
for i in s:
    sm+=i
print(sm)
        

 
