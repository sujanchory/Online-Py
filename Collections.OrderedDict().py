# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
d=OrderedDict()
#ordered_dictionary= OrderedDict()
for i in range(int(input())):
    p=input().rpartition(' ')
    #print(p)
    item, blank, price=p
    if item not in d:
        d[item]= int(price)
    else:
        d[item]+=int(price)
for i in d.items():     
 print(*i)        

