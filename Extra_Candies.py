candies=list(map(int,input().split()))
ec=int(input())
l=list()
for i in candies:
    if i+ec>=max(candies):
        l.append('true')
    else:
        l.append('false')
print(l)
