
NumberofSolutions=0

def initialize(board,n):
    for key in ['queen','row','column','diag_nw_se','diag_sw_ne']:
        board[key] = {}
    for i in range(n):
        board['queen'][i] = -1
        board['row'][i] = 0
        board['column'][i] = 0
    for  i in range(-(n-1),n):
        board['diag_nw_se'][i] = 0
    for i in range(2*n-1):
        board['diag_sw_ne'][i] = 0

def printboard(board):
    global NumberofSolutions
    NumberofSolutions+=1
    print ('Solution {}'.format(NumberofSolutions))
    for row in sorted(board['queen'].keys()):
        #print((row,board['queen'][row]), end ="")
        for i in range(8):
            if i == board['queen'][row]:
                print("{} ".format(i+1),end="")
            else:
                print("_ ",end="")
        print("\r")
    print('\r')

def free(i,j,board):
    return (board['row'][i] == 0 and board['column'][j] == 0 and board['diag_nw_se'][j-i] == 0 and board['diag_sw_ne'][j+i] == 0)


def addqueen(i,j,board):
    board['queen'][i] = j
    board['row'][i] = 1
    board['column'][j] = 1
    board['diag_nw_se'][j-i] = 1
    board['diag_sw_ne'][j+i] = 1

def removequeen(i,j,board):
    board['queen'][i] = -1
    board['row'][i] = 0
    board['column'][j] = 0
    board['diag_nw_se'][j-i] = 0
    board['diag_sw_ne'][j + i] = 0

def placequeen(i,board):
    n = len(board['queen'].keys())
    for j in range(n):
        if free(i,j,board):
            addqueen(i,j,board)
            if i == n-1:
                printboard(board)
            else:
                trysolution = placequeen(i+1,board)
            removequeen(i,j,board)

board = {}

n = 8

initialize(board,8)
if placequeen(0,board):
    printboard(board)
