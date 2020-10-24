def isWinner(board, sym):
    return (	((board[1] == sym) and (board[2] == sym) and (board[3] == sym)) or
             ((board[1] == sym) and (board[4] == sym) and (board[7] == sym)) or
             ((board[1] == sym) and (board[5] == sym) and (board[9] == sym)) or
             ((board[2] == sym) and (board[5] == sym) and (board[8] == sym)) or
             ((board[3] == sym) and (board[6] == sym) and (board[9] == sym)) or
             ((board[4] == sym) and (board[5] == sym) and (board[6] == sym)) or
             ((board[7] == sym) and (board[8] == sym) and (board[9] == sym)) or
             ((board[3] == sym) and (board[5] == sym) and (board[7] == sym))		)
