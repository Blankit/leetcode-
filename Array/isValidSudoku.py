#coding:utf-8
# print
'''
排除所有格填入的都是','的情况
'''
class Solution(object):
    def isDuplicate(self,nums):
        dic = {}
        for num in nums:
            if num != '.':
                if num not in dic:
                    num = num
                    dic[num] = 1
                else:
                    dic[num] += 1
        for t in dic.values():
            if t>1:
                return False
        return True
    def tran(self,board):
        board_9 = []
        for k in range(3):
            for m in range(3):
                temp = []
                for i in range(3):
                    for j in range(3):
                        temp += board[3 * k + i][3 * m + j]
                # print temp
                board_9.append(temp)
        return board_9
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        board_t = map(list, zip(*board))
        board_9 = self.tran(board)
        count = 0
        for matrix in (board,board_t,board_9):
            for arr in matrix:
                t = self.isDuplicate(arr)
                if not t:
                    return False
        return True


# board = [
#   ["5","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ]

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