board = [
    [5, 3, 0,  0, 7, 0,  0, 0, 0],
    [6, 0, 0,  1 ,9, 5,  0, 0, 0],
    [0, 9, 8,  0, 0, 0,  0, 6, 0],
    
    [8, 0, 0,  0, 6, 0,  0, 0, 3],
    [4, 0, 0,  8, 0, 3,  0, 0, 1],
    [7, 0, 0,  0, 2, 0,  0, 0, 6],

    [0, 6, 0,  0, 0, 0,  2, 8, 0],
    [0, 0, 0,  4, 1, 9,  0, 0, 5],
    [0, 0, 0,  0, 8, 0,  0, 7, 9]
]
length = len(board)
width = len(board[0])

def Printboard(board):
    for i in range(length):
        if i % 3 == 0:
            print('----------------------')
        
        for j in range(width):
            if j % 3 == 0 and j != 0:
                print('| ', end='')
            print(board[i][j], end=' ')
        print('')

def Solve(board):
    if not Findspace(board):
        return True
    box = Findspace(board)
    for i in range(1, 10):
        if Valid(board, i, box):
            Fill(board, i, box)
            if Solve(board):
                return True
            Fill(board, 0, box)
    return False

def Findspace(board):
    for i in range(length):
        for j in range(width):
            if board[i][j] == 0:
                return (i, j)
    return False

def Valid(board, val, box):
    x = box[0]
    y = box[1]
    for i in range(width):
        if board[x][i] == val:
            return False
    for i in range(length):
        if board[i][y] == val:
            return False
    sx = (x // 3) * 3
    sy = (y // 3) * 3
    for i in range(sx, sx + 3):
        for j in range(sy, sy + 3):
            if board[i][j] == val:
                return False
    return True

def Fill(board, val, box):
    board[box[0]][box[1]] = val


'''Main Code'''

if Solve(board):
    Printboard(board)
else:
    print('No solution')