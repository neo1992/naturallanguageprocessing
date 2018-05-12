def spiralmatrix(A):
    numrow = len(A)
    numcol = len(A[0])

    top = 0
    bottom = numrow
    right = numcol
    left = 0
    direction=0

    B = []

    while top < bottom and left < right:
        if direction is 0:
            for i in range(left, right):
                B.append(A[top][i])
            top += 1
        elif direction is 1:
            for i in range(top, bottom):
                B.append(A[i][right])
            right -= 1
        elif direction is 2:
            for i in range(right, left, -1):
                B.append(A[bottom][i])
            bottom -= 1
        elif direction is 3:
            for i in range(bottom, top, -1):
                B.append(A[left][i])
            left += 1
        direction = (direction+1) % 4
    return B

a = [
        [1,2,3],
        [4,5,6],
        [7,8,9]

    ]

print(spiralmatrix(a))