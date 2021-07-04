if __name__ == '__main__':
    s = input()
    
    for i in [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper]:
         print( any(i(c) for c in s))
