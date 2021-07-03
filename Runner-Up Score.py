if __name__ == '__main__':
    n = int(input())
    arr =list(map(int, input().split()))
    m=max(arr)
    #print(m)
    c=arr.count(m)
    #print(c)
    for i in range(c):
        arr.remove(m)
    print(max(arr))
    
