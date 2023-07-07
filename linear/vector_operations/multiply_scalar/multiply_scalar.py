def multiply_scalar(scalar, A):
    n_rows, n_cols = len(A), len(A[0])
    resultant = [[0 for _ in range(n_cols)] for k in range(n_rows)]
    for row in range(n_rows):
        for col in range(n_cols):
            resultant[row][col] = scalar * A[row][col]
    return resultant

def test_multiply_scalar():
    import numpy as np
    tests = []
    for m in range(1,10):
        for p in range(1,10):
                A = np.random.randint(0,10,size=(m,p))
                scalar = np.random.randint(0,100)
                mine = np.array(multiply_scalar(scalar,A))
                theirs = np.multiply(scalar,A)
                tests.append(np.array_equiv(mine, theirs))
    if all(tests):
        print("All tests passed!")

if __name__=="__main__":
    test_multiply_scalar()