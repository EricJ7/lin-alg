import numpy as np
import math

class Vector():

    iUnitVector = [1, 0, 0]
    jUnitVector = [0, 1, 0]
    kUnitVector = [0, 0, 1]

    xAxisReflectionMatrix = [[1, 0], [0, -1]]
    yAxisReflectionMatrix = [[-1, 0], [0, 1]]
    # reflect off line y = x
    lineReflectionMatrix = [[0, 1], [1, 0]]

    # will hold the greatest x, y, and z
    # to handle the limit setting on the plot
    limits = []

    def __init__(self, vector):
        self.vector = vector
        self.space = len(vector)

        # if limits is empty initially, the greatest
        # x, y, z components is the first vector object
        if not Vector.limits:
            for component in self.vector:
                Vector.limits.append(component)
        # otherwise, compare the new vector object with the
        # current components in limits
        else:
            for index in range(len(self.vector)):
                if self.vector[index] > Vector.limits[index]:
                    Vector.limits[index] = self.vector[index]


    # determines if an arbitrary number of vectors
    # in R2 or R3 space are linearly dependant or not
    # (set up matrix A, perform rref, compare rank of A, [A|b])
    def linearlyIndependant(self, *Vectors):
        """
        :type val: theta - angle in degrees
        :rtype: list [float] vector
        """

        independant = False

        augMatrix = []
        augMatrix.append(self.vector)

        for i in Vectors:
            augMatrix.append(i.vector)

        # append standard vector full of zeroes
        # solving system of homogeneous equations
        augMatrix.append([0, 0, 0])

        # put the augmented matrix into its rref


        return independant


    def dotProduct(self, Vector):
        """
        :type val: Vector Object
        :rtype: float
        """
        vectorDotProduct = 0

        for index in range(self.space):
            vectorDotProduct += (self.vector[index] * Vector.vector[index])

        return vectorDotProduct

    def userDefinedMatrixTransformation(self, Matrix):
        """
        :type val: Matrix Object, space (int)
        :rtype: list[float]
        """
        # validate that matrix multiplication is defined
        assert Matrix.space == len(self.matrix)

        product = []


        return product


    def crossProduct(self, Vector):
        """
        :type val: Vector Object
        :rtype: list[int/float]
        """
        # cross product is only defined in R3
        assert len(self.vector) == 3

        crossProduct = []

        crossProduct.append((self.vector[1] * Vector.vector[2]) \
         - (self.vector[2] * Vector.vector[1]))

        crossProduct.append((self.vector[2] * Vector.vector[0]) \
         - (self.vector[0] * Vector.vector[2]))

        crossProduct.append((self.vector[0] * Vector.vector[1]) \
         - (self.vector[1] * Vector.vector[0]))

        return crossProduct


    # matrix transformation to reflect
    # vector off y axis
    def vectorReflectionYAxis(self):
        """
        :type val: None
        :rtype: float
        """

        product = []

        return product


    # matrix transformation to reflect
    # vector off of the x axis
    def vectorReflectionXAxis(self):
        """
        :type val: None
        :rtype: float
        """

        product = []

        return product


    # matrix transformation to rotate a vector theta
    # radians counterclockwise
    # treat negative degrees to rotate below x axis
    def vectorRotationXAxis(theta):
        from matrix import Matrix
        """
        :type val: theta - angle in degrees
        :rtype: list [float] vector
        """
        assert theta > 0

        radians = degreesToRadians(theta)

        # rotation matrix:
        #   [cos0  -sin0]
        #   [sin0  cos0]
        # x' = xcos0 - ysin0
        # y' = xsin0 + ycos0

        # initialize rotation matrix
        rotationMatrix = [[math.cos(radians), -math.sin(radians)], \
        [math.sin(radians), math.cos(radians)]]

        # perform matrix multiplication on given vector
        matrix = Matrix(self.vector)
        resultant = matrix.matrixMultiplicaton(rotationalMatrix)

        return resultant


    def degreesToRadians(self, degrees):
        """
        :type val: degrees (float/int)
        :rtype: float
        """

        return degrees * (math.pi/180)


    def vectorMagnitude(self):
        """
        :type val:
        :rtype: float
        """

        if self.space == 3:
            magnitude = math.sqrt(((self.vector[0]) ** 2) + (self.vector[1] ** 2) \
        + ((self.vector[2]) ** 2))
        else:
            magnitude = math.sqrt(((self.vector[0]) ** 2) + ((self.vector[1]) ** 2))

        return magnitude

    def findFactor(self, n):
        """
        :type val: n (int)
        :rtype: list [int]
        """

        factors = []
        for i in range(1, n + 1):
            if n % i == 0:
                factors.append(i)

        return factors


    def vectorAddition(self, Vector):
        """
        :type val: Vector Object
        :rtype: list[int/float]
        """

        vectorSum = []

        for index in range(self.space):
            vectorSum.append(self.vector[index] + Vector.vector[index])

        return vectorSum


    def vectorSubtraction(self, Vector):
        """
        :type val: Vector Object
        :rtype: list[int]
        """

        vectorDifference = []

        for index in range(self.space):
            vectorDifference.append(self.vector[index] - Vector.vector[index])

        return vectorDifference

    # returns a list with the same
    # values as the vector objects
    # used in plot.py
    def vectorToList(self):
        """
        :type val: None
        :rtype: list[float]
        """
        list = []
        for value in self.vector:
            list.append(value)

        return list


    def getLimts(self):
        """
        :type val: None
        :rtype: list[float]
        """

        return Vector.limits


    def __repr__(self):
        if self.space == 3:
            return f"Vector(x={self.vector[0]}, y={self.vector[1]}, z={self.vector[2]})"
        else:
            return f"Vector(x={self.vector[0]}, y={self.vector[1]})"
