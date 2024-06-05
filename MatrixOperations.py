class MatrixOperations:
    def __init__(self, matrix):
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
        if not (self.getSize()[0] == self.getSize()[1]):
            del self
        self.invertible = True
        for row in self.rowEchelonForm():
            if self.rowOfZeroes(row):
                self.invertible = False
                break
    
    def traceMatrix(self):
        sum = 0
        for i in range(self.getSize()[0]):
            sum += self.getMatrix()[i][i]
        return sum

    def determinant(self):
        sum = 0
        #get to ref then multiply main diagonal together then subtract bottom right 2x2 matrix
        return sum
    
    def rowEchelonForm(self):
        new_matrix = self.getMatrix().copy()
        w = self.getSize()[0]
        for i in range(w): #iterate through all columns left to right
            if self.rowOfZeroes(new_matrix[i]):
                continue
            for j in range(i+1,w): #iterate through all rows starting at the main diagonal (top to bottom)
                multiplier = new_matrix[j][i]
                for k in range(i,w): #change all rows below the starting row for the iteration to have the column with the leading 1 to be equal to 0
                    new_matrix[j][k] -= multiplier*new_matrix[i][k]/new_matrix[i][i]
        return new_matrix
    
    def rowOfZeroes(self, row):
        for num in row:
            if not num == 0:
                return False
        return True

    
def matrixTester(matrix1, matrix2):
    temp = matrix2
    matrix1 = MatrixOperations(matrix1)
    matrix2 = MatrixOperations(matrix2)
    #new_matrix = matrix1.addMatrix(matrix2) #add 2 matrices
    #new_matrix = matrix1.multiplyMatrix(matrix2) #multiply 2 matrices
    #new_matrix = matrix2.transposeMatrix() #transpose
    new_matrix = temp
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
new_matrix = MatrixOperations(matrixTester(matrix1, matrix2))
#matrix1 = MatrixOperations(matrix1)
#matrix2 = MatrixOperations(matrix2)
#matrix1.printMatrix()
#matrix2.printMatrix()
new_matrix.printMatrix()

square_matrix = SquareMatrix(matrix4)
ref_matrix = square_matrix.rowEchelonForm()
ref_matrix = SquareMatrix(ref_matrix)
ref_matrix.printMatrix()
trace = square_matrix.traceMatrix()
#print(trace)
