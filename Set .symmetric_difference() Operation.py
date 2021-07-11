# Enter your code here. Read input from STDIN. Print output to STDOUT
a=int(input())
a1=set(map(int,input().split()))
b=int(input())
b1=set(map(int,input().split()))
c=(a1^b1)
print(len(c))
