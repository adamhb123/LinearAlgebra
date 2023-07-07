def subtract(A,B):
    n_rows, n_cols = len(A), len(A[0])
    resultant = [[0 for _ in range(n_cols)] for k in range(n_rows)]
    for row in range(n_rows):
        for col in range(n_cols):
            resultant[row][col] = A[row][col] - B[row][col]
    return resultant

def test_subtract():
    import numpy as np
    tests = []
    for m in range(1,10):
        for p in range(1,10):
                A = np.random.randint(0,10,size=(m,p))
                B = np.random.randint(0,10,size=(m,p))
                mine = np.array(subtract(A,B))
                theirs = np.subtract(A,B)
                tests.append(np.array_equiv(mine, theirs))
    if all(tests):
        print("All tests passed!")

if __name__=="__main__":
    test_subtract()