def dot(A,B):
    rows_A, rows_B, cols_A, cols_B = len(A), len(B), len(A[0]), len(B[0])
    if not (cols_A == rows_B):
        raise Exception("Invalid input matrices")
    m, p, n = rows_A, cols_B, cols_A
    C = [[0 for c in range(cols_B)] for r in range(rows_A)]
    for i_m in range(m):
        for i_p in range(p):
            C_sub_elems = []
            for i_n in range(n):
                C_sub_elems.append(A[i_m][i_n] * B[i_n][i_p])
            C[i_m][i_p] = sum(C_sub_elems) 
    return C
            
def dot_test():
    import numpy as np
    tests = []
    for m in range(1,10):
        for p in range(1,10):
            for n in range(1, 10):
                A = np.random.randint(0,10,size=(m,n))
                B = np.random.randint(0,10,size=(n,p))
                mine = np.array(dot(A,B))
                theirs = np.dot(A,B)
                tests.append(np.array_equiv(mine, theirs))
    if all(tests):
        print("All tests passed!")


if __name__=="__main__":
    dot_test()
 