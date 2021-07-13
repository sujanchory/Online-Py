def print_formatted(number):
    # your code goes here
    S=len('{0:b}'.format(number))
    for i in range(1,number+1):
      print('{0:{s}d} {0:{s}o} {0:{s}X} {0:{s}b}'.format(i,s=S))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
