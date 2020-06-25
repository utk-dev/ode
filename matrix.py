class Row:
    ''' A python list with some extra features of a 1xn Matrix (Vector) '''
    def __init__(self, initvalues):
        if isinstance(initvalues, list) and len(initvalues) > 0:
            self.vector = initvalues
        else:
            raise Exception("Row must be initialised with a non empty list")
    def __getitem__(self, index):
        return self.vector[index]
    def __setitem__(self, index, value):
        self.vector[index] = value
    def __len__(self):
        return len(self.vector)
    def __str__(self):
        return str(self.vector)

    def __add__(self, elem):
        if isinstance(elem, Row) and len(self) == len(elem):
            result = []
            for i in range(len(self)):
                result.append(self[i] + elem[i])
            return Row(result)
        else:
            raise Exception("A Row can only be added to another Row of same length")

    def __sub__(self, elem):
        if isinstance(elem, Row) and len(self) == len(elem):
            result = []
            for i in range(len(self)):
                result.append(self[i] - elem[i])
            return Row(result)
        else:
            raise Exception("A Row can only be subtracted from another Row of same length")

        
    def __mul__(self, elem):
        if isinstance(elem, int) or isinstance(elem, float):
            result = []
            for i in range(len(self)):
                result.append(elem*self[i])
            return Row(result)
        else:
            raise Exception("A Row can only be multiplied with a scalar")
    

    def __eq__(self, elem):
        if isinstance(elem, Row):
            return self.vector == elem.vector
        else:
            raise Exception("A Row can only be compared to another row")
    def __ne__(self, elem):
        if isinstance(elem, Row):
            return self.vector != elem.vector
        else:
            raise Exception("A Row can only be compared to another row")

    
class Matrix:
    ''' A python list of lists with Mathematical Matrix-like features '''
    def __init__(self, initvalues):
        if isinstance(initvalues[0], list):
            self.rows = [Row(line) for line in initvalues]
        elif isinstance(initvalues[0], Row):
            self.rows = initvalues
        self.m = len(self.rows)
        self.n = len(self.rows[0])

    def __getitem__(self, index):
        return self.rows[index]
    def __setitem__(self, index, value):
        self.rows[index] = value
    def __len__(self):
        return self.m
    def __str__(self):
        result = ""
        for row in self.rows:
            result += str(row) + " "
        return result

    def __add__(self, elem):
        if isinstance(elem, Matrix) and elem.m == self.m and elem.n == self.n:
            result = []
            for i in range(self.m):
                result.append(self[i] + elem[i])
            return Matrix(result)
        else:
            raise Exception("Incompatible addition")
    def __sub__(self, elem):
        if isinstance(elem, Matrix) and elem.m == self.m and elem.n == self.n:
            result = []
            for i in range(self.m):
                result.append(self[i] - elem[i])
            return Matrix(result)
        else:
            raise Exception("Incompatible subtraction")

    def __mul__(self, elem):
        if isinstance(elem, Matrix) and self.n == elem.m:
            result = [[0 for i in range(elem.n)] for j in range(self.m)]

            for i in range(self.m):
                for j in range(elem.n):
                    for k in range(self.n):
                        result[i][j] += self[i][k]*elem[k][j]

            return Matrix(result)
        elif isinstance(elem, int) or isinstance(elem, float):
            result = []
            for i in range(self.m):
                result.append(self[i]*elem)
            return Matrix(result)
        else:
            raise Exception("Incompatible multiple multiplication")

    def toList(self):
        res = []
        for i in range(self.m):
            r = []
            for j in range(self.n):
                r.append(self[i][j])
            res.append(r)
        return res
            
class SquareMatrix(Matrix):
    ''' A Square Matrix'''
    def __init__(self, initvalues):
        if len(initvalues) == len(initvalues[0]):
            super(SquareMatrix, self).__init__(initvalues)
        else:
            raise Exception("Square matrix needs equal dimensions.")
    
def transpose(M):
    ''' Transpose of a Matrix '''
    if not isinstance(M, Matrix):
        raise Exception("Cannot convert into a Matrix implicitly.")
    res = []
    for i in range(M.n):
        row = []
        for j in range(M.m):
            row.append(M[j][i])
        res.append(row)
    return Matrix(res)

def det(M):
    ''' Determinant of a Square Matrix '''
    if not isinstance(M, SquareMatrix):
        raise Exception("Determinant is defined only on square matrices.")
    if M.m == 1:
        return M[0][0]
    elif M.m == 2:
        return M[0][0]*M[1][1] - M[1][0]*M[0][1]
    else:
        s = 0
        for i in range(M.n):
            sub = []
            for j in range(1, M.m):
                row = []
                for k in range(0, i):
                    row.append(M[j][k])
                for l in range(i+1, M.n):
                    row.append(M[j][l])
                sub.append(row)
            s += ((-1)**(i))*M[0][i]*det(SquareMatrix(sub))
        return s

def adj(M):
    ''' Adjoint of a Square Matrix '''
    if not isinstance(M, SquareMatrix):
        raise Exception("Adjoint is defined only on square matrices.")
    A = []
    for i in range(M.m):
        R = []
        for j in range(M.n):
            cofactor = []
            for k in range(M.m):
                if k == i:
                    continue
                row = []
                for l in range(M.n):
                    if l == j:
                        continue
                    row.append(M[k][l])
                cofactor.append(row)
            # print(cofactor)
            R.append(((-1)**(i+j))*(det(SquareMatrix(cofactor))))
        A.append(R)
    return SquareMatrix(transpose(SquareMatrix(A)).rows)


