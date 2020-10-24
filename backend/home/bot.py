from checkWinner import isWinner
xo = ['X', 'O']
pts = [-1, 1]


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
