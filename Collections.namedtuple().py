# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
n,data,s=int(input()),namedtuple('data',input().split()),0 
for i in range(n):
    s+=int(data(*input().split()).MARKS)   
print('{0:.2f}'.format(s/n))
    
