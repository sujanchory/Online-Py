def cp(n):
    if n==1 or n==3 or n==5 or n==7 or n==2:
        return 0
    elif n==8:
        return 2
    else :
        return 1
def cpsum(t):
    s=0
    while t:
        rem=t%10
        t//=10
        s+=cp(rem)
    return s
t=int(input())
print(cpsum(t))
