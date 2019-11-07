def countingValleys(n, s):
    level = 0
    valley = 0
    for i in range(n):
        if s[i] == 'U':
            level = level + 1
            if level == 0:
                valley = valley + 1
        else:
            level = level - 1
    print(valley)
countingValleys(8,"UDDDUDUU")

