class Matrix(object):
    def __init__(self, values):
        self.values = values

    def __repr__(self):
        return f'<Matrix values="{self.values}">'

    @property
    def cols(self):
        # The number of values in the x-axis of the matrix
        # We can get this as the length of the first list
        #    in the matrix
        return len(self.values[0])

    @property
    def rows(self):
        # The number of values in the y-axis of the matrix
        # We can get this as the total number of lists in the list
        return len(self.values)

    def __matmul__(self, other):
        # Create a empty result list of the required size
        # It is assumed that compatible lists are provided
        #    but size checking could be added here
        result = [[0 for i in range(other.cols)] for j in range(self.rows)]

        # iterate through rows of X
        for i in range(self.rows):
            # iterate through columns of Y
            for j in range(other.cols):
                # iterate through rows of Y
                for k in range(other.rows):
                    result[i][j] += self.values[i][k] * other.values[k][j]

        return Matrix(result)
