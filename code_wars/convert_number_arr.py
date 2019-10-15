n = 326376

def digitize(n):
    # rev = map(int, str(n))
    n = list(str(n))
    n.reverse()   
    for i in n:
        i = int(i)
    return n

print(digitize(n))