n=int(input('enter a number'))
p=int(input('enter a number'))
c=0
t=1
def prime(n,p,c,t):
if n%t==0:
c+=1
if c==p:
return t
else:
return prime(n,p,c,t+1)
elif p>c and t>=n:
return 0
else:
return prime(n,p,c,t+1)
print(prime(n,p,c,t))
