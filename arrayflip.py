def binflip(a):
    n = len(a)

    for i in range(n):
        for j in range(n):
            if a[i] or a[j] is 0:
                a[i] = 1
                a[j] = 1
            else:
                a[i] = 0
                a[j] = 0

    return a, i, j

a = [0, 1, 0, 1]
print(binflip(a))


