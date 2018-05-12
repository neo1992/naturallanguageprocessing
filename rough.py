def repeatedNumber(A):
    n = len(A)
    sumofsquares = 0
    for i in A:
        sumofsquares += i * i
    s = (n * (n + 1)) / 2
    sa = sum(A)
    a_minus_b = sa - s
    sum_of_squares = (n * (n + 1) * (2 * n + 1)) / 6
    a2_minus_b2 = sumofsquares - sum_of_squares
    a_plus_b = a2_minus_b2 / a_minus_b
    a = (a_plus_b + a_minus_b) / 2
    b = a_plus_b - a
    return (a, b), s, sa, sum_of_squares, sumofsquares

a = [1, 3, 2, 1, 5, 7, 6, 9, 4, 11, 8]
print(repeatedNumber(a))