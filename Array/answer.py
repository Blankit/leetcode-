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
# # board_9 = []
# # for k in range(3):
# #     for m in range(3):
# #         temp = []
# #         for i in range(3):
# #             for j in range(3):
# #                 temp += board[3*k+i][3*m+j]
# #         print temp
# #         board_9.append(temp)
# # print board_9
# # print len(board_9)
# # print board_t
#
# board_t = map(list, zip(*board))
# print board
# print board_t
# print board

board = [[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]]
if board == ['.']:
    print True
else:
    print False
bard = [[],[],[]]
if board:
    print True
else:
    print False