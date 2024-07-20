MOD = 1000000007

def matrix_multiply(A, B):
    return [
        [(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % MOD, (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % MOD],
        [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % MOD, (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % MOD]
    ]

def matrix_power(matrix, power):
    result = [[1, 0], [0, 1]]
    base = matrix

    while power > 0:
        if power % 2 == 1:
            result = matrix_multiply(result, base)
        base = matrix_multiply(base, base)
        power //= 2
    
    return result

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    A = [[1, 1], [1, 0]]
    result_matrix = matrix_power(A, n - 1)
    return result_matrix[0][0]

n = int(input())
print(fibonacci(n))