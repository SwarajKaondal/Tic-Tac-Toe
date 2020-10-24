xo = ['X', 'O']
pts = [-1, 1]


def isWinner(board, sym):
    return (((board[1] == sym) and (board[2] == sym) and (board[3] == sym)) or
            ((board[1] == sym) and (board[4] == sym) and (board[7] == sym)) or
            ((board[1] == sym) and (board[5] == sym) and (board[9] == sym)) or
            ((board[2] == sym) and (board[5] == sym) and (board[8] == sym)) or
            ((board[3] == sym) and (board[6] == sym) and (board[9] == sym)) or
            ((board[4] == sym) and (board[5] == sym) and (board[6] == sym)) or
            ((board[7] == sym) and (board[8] == sym) and (board[9] == sym)) or
            ((board[3] == sym) and (board[5] == sym) and (board[7] == sym)))


def gameComplete(board):
    for i in board[1:]:
        if i == ' ':
            return False
    return True


def checkVacancies(board):
    v = []
    for i in range(1, 10):
        if board[i] == ' ':
            v.append(i)
    return v


def calcScore(state, sym):
    vacancies = checkVacancies(state)

    if isWinner(state, xo[((sym+1) % 2)]):
        return (len(vacancies)+1)*(pts[((sym+1) % 2)])

    if len(vacancies) == 0:
        return 0

    score = {}
    for i in vacancies:
        state[i] = xo[sym]
        score[i] = calcScore(state, ((sym+1) % 2))
        state[i] = ' '

    if sym == 1:
        return max(list(score.values()))
    else:
        return min(list(score.values()))


def compInput(state, sym):
    if sym == 'O':
        sym = 1
    else:
        sym = 0

    vacancies = checkVacancies(state)
    score = {}
    for i in vacancies:
        state[i] = xo[sym]
        score[i] = calcScore(state, ((sym+1) % 2))
        state[i] = ' '

    if (max(score.values()) == 0) and (min(score.values()) == 0) and (9 in list(score.keys())):
        score[9] = 3

    return max(score, key=score.get)


def getCompInput(board):
    data = [False, -1]
    winner = 0
    move = 1
    if isWinner(board, 'X'):
        data[winner] = 'X'
        return data
    elif gameComplete(board):
        data[winner] = 'T'
        return data

    pos = compInput(board, 'O')
    data[move] = pos
    board[pos] = 'O'
    if isWinner(board, 'O'):
        data[winner] = 'O'
        return data

    if gameComplete(board):
        data[winner] = 'T'
        return data

    return data
