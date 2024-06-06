class MatrixOperations:
    def __init__(self, matrix):
        self.orig = matrix
        self.matrix = matrix
        self.m = len(matrix)
        self.n = len(matrix[0])

    def getSize(self):
        return self.m, self.n

    def getMatrix(self):
        return self.matrix

    def printMatrix(self):
        for row in self.getMatrix():
            print(row)
        print('\n')

    def addMatrix(self, matrix):
        if not (self.getSize() == matrix.getSize()):
            return -1
        new_matrix = self.matrix.copy()
        for i in range(len(new_matrix)):
            for j in range(len(new_matrix[0])):
                new_matrix[i][j] = self.getMatrix()[i][j] + matrix.getMatrix()[j][i]
        return new_matrix
    
    def dotProduct(self, matrix, row, column):
        if not(self.getSize()[1] == matrix.getSize()[0]):
            return -1
        sum = 0
        for i in range(self.getSize()[1]):
            sum += self.getMatrix()[row][i] * matrix.getMatrix()[i][column]
        return sum

    def multiplyMatrix(self, matrix):
        if not(self.getSize()[1] == matrix.getSize()[0]):
            return -1
        new_matrix = []
        for i in range(self.getSize()[0]):
            new_matrix.append([])
            for j in range(matrix.getSize()[1]):
                new_matrix[i].append(self.dotProduct(matrix,i,j))
        return new_matrix
    
    def transposeMatrix(self):
        new_matrix = []
        for i in range(self.getSize()[1]):
            new_matrix.append([])
            for j in range(self.getSize()[0]):
                new_matrix[i].append(self.getMatrix()[j][i])
        return new_matrix

class SquareMatrix(MatrixOperations):
    def __init__(self, matrix):
        super().__init__(matrix)
        self.invertible = True
        for row in self.rowEchelonForm():
            if self.rowOfZeroes(row):
                self.invertible = False
                break
    
    def isInvertible(self):
        return self.invertible

    def traceMatrix(self):
        sum = 0
        for i in range(self.getSize()[0]):
            sum += self.getMatrix()[i][i]
        return sum

    def determinant(self):
        if not self.isInvertible():
            return 0
        product = 1
        new_matrix = SquareMatrix(self.getMatrix().copy()).rowEchelonForm()
        for i in range(len(new_matrix)):
            product *= new_matrix[i][i]
        return product
    
    def rowEchelonForm(self):
        new_matrix = self.getMatrix().copy()
        w = self.getSize()[0]
        for i in range(w): #iterate through all columns left to right
            if self.rowOfZeroes(new_matrix[i]) or new_matrix[i][i] == 0:
                continue
            for j in range(i+1,w): #iterate through all rows starting at the main diagonal (top to bottom)
                multiplier = new_matrix[j][i]
                for k in range(i,w): #change all rows below the starting row for the iteration to have the column with the leading 1 to be equal to 0
                    new_matrix[j][k] -= multiplier*new_matrix[i][k]/new_matrix[i][i]
        return new_matrix

    def reducedRowEchelonForm(self):
        new_matrix = SquareMatrix(self.getMatrix().copy()).rowEchelonForm()
        w = self.getSize()[0]
        for i in range(w): #iterate through all columns right to left
            r = w-i-1 #index of rightmost column/bottom row
            if self.rowOfZeroes(new_matrix[r]):
                continue
            for j in range(i+1,w): #iterate through all rows starting at the main diagonal (bottom to top)
                multiplier = new_matrix[w-j][w-i-1]
                for k in range(r): #change all rows the above row for the iteration to have the column value changed to 0
                    new_matrix[r-k-1][w-i-1] -= multiplier*new_matrix[r-k-1][w-i-1]/new_matrix[r][r]
        for i in range(w):
            multiplier = new_matrix[i][i]
            if multiplier == 1 or multiplier == 0:
                continue
            for j in range(i,w):
                new_matrix[i][j]/=multiplier
        return new_matrix
    
    def inverseMatrix(self): #assumes A is invertible and the form [A | I] [R | E] is already input as a matrix, meaning A and the identity matrix each take up only one quarter of the entire matrix inputted, while R and E are left blank so the matrix is square
        new_matrix = []
        rref_matrix = SquareMatrix(SquareMatrix(self.getMatrix()).reducedRowEchelonForm())
        w = int(self.getSize()[0]/2)
        for i in range(w):
            new_matrix.append(rref_matrix.getMatrix()[i][w:])
        return new_matrix


    def rowOfZeroes(self, row):
        for num in row:
            if not num == 0:
                return False
        return True

    
def matrixTester(matrix1, matrix2):
    matrix1 = MatrixOperations(matrix1)
    matrix2 = MatrixOperations(matrix2)
    #new_matrix = matrix1.addMatrix(matrix2) #add 2 matrices
    #new_matrix = matrix1.multiplyMatrix(matrix2) #multiply 2 matrices
    new_matrix = matrix2.transposeMatrix() #transpose
    return new_matrix

matrix1 = [[1,0],
           [2,3]]
matrix2 = [[1,2,3],
           [4,5,6],
           [7,8,9]]
matrix3 = [[1,2,3,4],
           [5,6,7,8],
           [9,10,11,12],
           [13,14,15,16]]
matrix4 = [[1,2,3,4,5],
           [6,7,8,9,10],
           [11,12,13,14,15],
           [16,17,18,19,20],
           [21,22,23,24,25]]
matrix5 = [[3,3,1],
           [0,1,0],
           [1,1,3]]
matrix5 = SquareMatrix(matrix5)
matrix6 = [[-2,0,7,7,-3,9],
           [1,-6,2,4,5,6],
           [4,3,9,9,-4,8],
           [5,9,0,2,8,1],
           [-2,3,4,7,6,8],
           [-4,-1,2,-1,3,2]]
matrix6 = SquareMatrix(matrix6)
matrix6.printMatrix()
SquareMatrix(matrix6.rowEchelonForm()).printMatrix()

imatrix7 = [[2,0,0,1,0,0],
           [0,3,0,0,1,0],
           [0,0,4,0,0,1],
           [0,0,0,0,0,0],
           [0,0,0,0,0,0],
           [0,0,0,0,0,0]]
imatrix7 = SquareMatrix(imatrix7)
imatrix7.printMatrix()
SquareMatrix(imatrix7.inverseMatrix()).printMatrix()
