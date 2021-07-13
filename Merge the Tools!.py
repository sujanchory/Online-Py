def merge_the_tools(string, k):
    # your code goes here
    s=str()
    c=0
    for i in string:
        c+=1
        if i not in s:
            s+=i
        if c==k:
            print(s)
            c=0
            s=str()
            

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
