def saveThePrisoner(n, m, s):
    r = m % n
    if ((r + s - 1)% n == 0):
        return n
    else:
        return((r + s - 1) % n)
print(saveThePrisoner(7,19,2))

#  res = (s + m-1) % n
#     return res if res != 0 else n