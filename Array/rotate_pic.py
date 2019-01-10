class Solution(object):

    def trans(self, matrix):
        l = len(matrix)
        for i in range(l):
            for j in range(i, l):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        l = len(matrix)

        self.trans(matrix)
        for i in range(l):
            for j in range(l/2):
                matrix[i][j],matrix[i][l-j-1] = matrix[i][l-j-1],matrix[i][j]



# matrix = [
#   [ 5, 1, 9,11],
#   [ 2, 4, 8,10],
#   [13, 3, 6, 7],
#   [15,14,12,16]
# ]
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# for i in matrix:
#     print i
A = Solution()
b = A.rotate(matrix)
# print '*'*20
# for i in matrix:
#     print i
print matrix