def maxsubarray(A):
    alen = len(A)
    left = []
    right = []
    sumleft = 0
    sumright = 0
    for i in range(alen):
        if A[i] < 0:
            for j in range(i):
                left.append(A[j])
            for x in range(i+1, alen):
                right.append(A[x])

    for i in range(len(left)):
        sumleft += left[i]

    for i in range(len(right)):
        sumright += right[i]

    if sumleft is sumright and len(left) is len(right):
        if left[0] < right[0]:
            print(left," is larger than ", right, " because the first element in first list is smaller than the first element of second list")
        else:
            print(right, " is larger than ", left," because the first element in first list is smaller than the first element of second list")
    elif sumleft is sumright:
        if len(left) > len(right):
            print(left, " is larger than ", right," as lenght of the list in the previous list is larger than the second list")
        else:
            print(right, " is larger than ", left," as sum of the elements in the previous list is larger than the second list")
    elif sumleft > sumright:
        print(left, " is larger than ",right," as sum of the elements in the previous list is larger than the second list")
    else:
        print(right, " is larger than ", left," as sum of the elements in the previous list is larger than the second list")


A = [5, 3, 2, -3, 9, 1, 2]

(maxsubarray(A))

