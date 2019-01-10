class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = [[] for i in range(9)]
        cols = [[] for i in range(9)]
        cells = [[] for i in range(9)]

        for i, row in enumerate(board):
            for j, num in enumerate(row):
                if num != '.':
                    k = (i // 3) * 3 + j // 3
                    if num in rows[i] + cols[j] + cells[k]:
                        return False
                    rows[i].append(num)
                    cols[j].append(num)
                    cells[k].append(num)
        return True

board = [[".",".","5",".",".",".",".",".","6"],
[".",".",".",".","1","4",".",".","."],
[".",".",".",".",".",".",".",".","."],
[".",".",".",".",".","9","2",".","."],
["5",".",".",".",".","2",".",".","."],
[".",".",".",".",".",".",".","3","."],
[".",".",".","5","4",".",".",".","."],
["3",".",".",".",".",".","4","2","."],
[".",".",".","2","7",".","6",".","."]]
A = Solution()
b = A.isValidSudoku(board)
print b