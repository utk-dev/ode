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


    
