class Matrix(object):
    def __init__(self, values):
        self.values = values
        self.col = len(self.values[0])
        self.row = len(self.values)

    def __repr__(self):
        return f'<Matrix values="{self.values}">'

    def __matmul__(self, other):
        if self.col != other.row:
            raise ValueError(
                ("Numbers rows first matrix != number columns " "second matrix")
            )
        # Create a empty result list of the required size
        # It is assumed that compatible lists are provided
        #    but size checking could be added here
        result = [[0 for i in range(other.col)] for j in range(self.row)]

        # iterate through rows of X
        for i in range(self.row):
            # iterate through columns of Y
            for j in range(other.col):
                # iterate through rows of Y
                for k in range(other.row):
                    result[i][j] += self.values[i][k] * other.values[k][j]

        return Matrix(result)

    def __rmatmul__(self, other_mat):
        new_self = Matrix(self.values)
        return new_self @ other_mat

    def __imatmul__(self, other_mat):
        self.values = self.__matmul__(other_mat).values
        return self

