import numpy as np
import math
from vector import Vector

class Matrix:
    def __init__(self, *vectors):
        self.matrix = []

        for vector in vectors:
            self.matrix.append(vector)

        self.dim = len(self.matrix)

    def matrixDeterminant(self):
        """
        :type val: None
        :rtype: float
        """

        determinant = 0

        # ad - bc
        if self.space == 2:
            determinant = (self.matrix[0][0] * self.matrix[2][2]) - \
            (self.matrix[0][1] * self.matrix[1][0])

        # 3x3 matrix, perform cofactor expansion
        #else:

        return determinant

    # function to determine the minor of a matrix
    def matrixMinor(self, i, j):
        n = self.dim

        # validate that the cofactors i and j
        # are both less than the space of the matrix
        # (cant take cofactors of 4 if dim = 3)
        assert i < n and j < n


        return

    def matrixInverse(self):
        """
        :type val: None
        :rtype: float
        """

        inverse = []

        # inverse doesnt exist
        if self.determinant() == 0:
            return
        #else:

        return inverse

    # computes the rref for the matrix object
    def reducedRowEchelonForm(self, constantVector):
        """
        :type val: Vector object - solution vector, contained to right of augmented matrix
        :rtype: list [float][float]
        """

        # augmented matrix will contain the original
        # 2d matrix, with the constant vectors
        augMatrix = []

        for vector in self.matrix:
            augMatrix.append(vector)
        augMatrix.append(constantVector.vector)


        return rref


    def matrixTranspose(self):
        """
        :type val: None
        :rtype: list [float]
        """

        transpose = []

        for n in range(len(self.matrix[0])):
            row = []
            for element in self.matrix:
                row.append(element[n])
            transpose.append(row)

        return transpose


    # solves a system of equations represented
    # by a matrix
    def solve(self):
        """
        :type val: None
        :rtype: list [float]
        """


        return


    def rank(self):
        """
        :type val: None
        :rtype: rank (int)
        """


        return rank


    # multiplies two matrices together
    def matrixMultiplicaton(self, *Matrices):
        """
        :type val: Matrices (object)
        :rtype: list[float][float]
        """
        productMatrix = []
        m = []

        for matrix in Matrices:
            m.append(matrix)

        # validate that matrix multiplication is defined
        # i.e (mxn) (nxp) --- > (mxp)
        assert (len(self.matrix) == len(givenMatrix[0]))


        return productMatrix

    def matrixToList(self):
        """
        :type val: None
        :rtype: list[int][int]
        """
        list = []

        for row in self.matrix:
            list.append(row)

        return

    def __repr__(self):

        if self.dim == 3:
            return f"Matrix({self.matrix[0]}\n{self.matrix[1]}\n{self.matrix[2]})"
        else:
            return f"Matrix({self.matrix[0]}\n{self.matrix[1]})"
