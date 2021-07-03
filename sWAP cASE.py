def swap_case(s):
    return''.join(map(change,s))
def change(c):
    if str.islower(c):
        return str.upper(c)
    return str.lower(c)


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
    print(change())
