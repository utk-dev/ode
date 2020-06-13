from matrix import Row, Matrix, SquareMatrix, det, adj
def cramer(eqs, varNames, api = False, ACCURACY = 4):
    ''' Cramer's Rule '''
    if len(eqs) != len(eqs[0])-1 or len(varNames) != len(eqs):
        raise Exception("Insufficient number of variables of equations.")
    var_count = len(varNames)
    delta_matrix = SquareMatrix([row[:-1] for row in eqs])
    delta = det(delta_matrix)

    if delta == 0:
        raise Exception("Δ = 0, Cramer's method failed!")

    result = []
    for i in range(var_count):
        local_matrix = SquareMatrix([row[:i] + [row[-1]] + row[i+1:-1] for row in eqs])
        result.append((varNames[i], round(det(local_matrix)/delta, ACCURACY)))

    if api:
        return result
    else:
        for name, value in result:
            print("{0} = {1:.{2}f}".format(name, value, ACCURACY))

def matrix_inversion(eqs, varNames, api = False, ACCURACY = 4):
    ''' Matrix Inversion Method '''
    if len(eqs) != len(eqs[0])-1 or len(varNames) != len(eqs):
        raise Exception("Insufficient number of variables of equations.")
    var_count = len(varNames)
    delta_matrix = SquareMatrix([row[:-1] for row in eqs])
    delta = det(delta_matrix)

    if delta == 0:
        raise Exception("Δ = 0, Matrix Inversion failed!")

    const_matrix = Matrix([[row[-1]] for row in eqs])
    adjoint = adj(delta_matrix)
    res = (adjoint*const_matrix)*(1/delta)  # actual solving step
    adjointArray = adjoint.toList()
    resArray = [q[0] for q in res]
    result = [delta, adjointArray]
    for i in range(var_count):
        result.append((varNames[i], round(resArray[i], ACCURACY)))

    if api:
        return result
    else:
        print("Determinant = {0:.{1}f}".format(delta, ACCURACY))
        print("Adjoint = " + str(adjointArray))
        for name, value in result[2:]:
            print("{0} = {1:.{2}f}".format(name, value, ACCURACY))

def gauss_elimination(eqs, varNames, api = False, ACCURACY = 4):
    ''' Gauss Elimination Method '''
    if len(eqs) != len(eqs[0])-1 or len(varNames) != len(eqs):
        raise Exception("Insufficient number of variables of equations.")
    var_count = len(varNames)
    M = SquareMatrix([row[:-1] for row in eqs])
    B = Matrix([[row[-1]] for row in eqs])

    # convert to lower triangular matrix
    for i in range(M.m-1):
        if M[i][i] == 0:
            found = False
            for j in range(i+1, M.m):
                if M[j][i] != 0:
                    M[j], M[i] = M[i], M[j]
                    B[j], B[i] = B[i], B[j]
                    found = True
                    break
            if not found:
                raise Exception("Cannot find a unique solution.")
        for j in range(i+1, M.m):
            factor = M[j][i]/M[i][i]
            M[j] = M[j] - (M[i]*factor)
            B[j] = B[j] - (B[i]*factor)
    
    result = [M.toList(), [p[0] for p in B.toList()]]
    value = [0 for _ in range(M.n)]   # solutions

    # substitue values back in the equations
    for i in range(M.m-1, -1, -1):
        for j in range(i+1, M.n):
            M[i][j] *= value[j]
            B[i][0] -= M[i][j]
        if M[i][i] == 0:
            raise Exception("Cannot find a unique solution.")
        value[i] = B[i][0]/M[i][i]

    for i in range(var_count):
        result.append((varNames[i], round(value[i], ACCURACY)))

    if api:
        return result
    else:
        print("Lower Triangular Matrix")
        mat = result[0]
        for row, c in zip(mat, result[1]):
            for elem in row:
                print("{0:.{1}f}".format(elem, ACCURACY), end = ' ')
            print("| {0:.{1}f}".format(c, ACCURACY))
        print("")
        print("Solution:")
        for name, val in result[2:]:
            print("{0} = {1:.{2}f}".format(name, val, ACCURACY))


def gauss_jordan(eqs, varNames, api = False, ACCURACY = 4):
    ''' Gauss Jordan Method '''
    if len(eqs) != len(eqs[0])-1 or len(varNames) != len(eqs):
        raise Exception("Insufficient number of variables of equations.")
    var_count = len(varNames)
    M = SquareMatrix([row[:-1] for row in eqs])
    B = Matrix([[row[-1]] for row in eqs])

    # convert to lower triangular matrix
    for i in range(M.m-1):
        if M[i][i] == 0:
            found = False
            for j in range(i+1, M.m):
                if M[j][i] != 0:
                    M[j], M[i] = M[i], M[j]
                    B[j], B[i] = B[i], B[j]
                    found = True
                    break
            if not found:
                raise Exception("Cannot find a unique solution.")
        for j in range(i+1, M.m):
            factor = M[j][i]/M[i][i]
            M[j] = M[j] - (M[i]*factor)
            B[j] = B[j] - (B[i]*factor)

    # convert to diagonal matrix
    for i in range(M.m-1, -1, -1):
        if M[i][i] == 0:
            raise Exception("Cannot find a unique solution.")
        for j in range(i-1, -1, -1):
            factor = M[j][i]/M[i][i]
            M[j] = M[j] - (M[i]*factor)
            B[j] = B[j] - (B[i]*factor)
    
    result = [M.toList(), [p[0] for p in B.toList()]]
    value = [0 for _ in range(M.n)]   # solutions

    # substitue values back in the equations
    for i in range(M.m):
        value[i] = B[i][0]/M[i][i]

    for i in range(var_count):
        result.append((varNames[i], round(value[i], ACCURACY)))

    if api:
        return result
    else:
        print("Diagonal Matrix")
        mat = result[0]
        for row, c in zip(mat, result[1]):
            for elem in row:
                print("{0:.{1}f}".format(elem, ACCURACY), end = ' ')
            print("| {0:.{1}f}".format(c, ACCURACY))
        print("")
        print("Solution:")
        for name, val in result[2:]:
            print("{0} = {1:.{2}f}".format(name, val, ACCURACY))


    
# eqs = [[10,-7,3,5,6],[-6,8,-1,-4,5],[3,1,4,11,2],[5,-9,-2,4,7]]
# var = ['x','y','z','u']    
    


    
