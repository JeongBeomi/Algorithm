def solution(board):
    answer = board[0][0]
    n, m = len(board), len(board[0])
    for i in range(1, n):
        for j in range(1, m):
            if board[i][j] == 1:
                # 정사각형의 크기는 현재위치에서 상, 좌, 좌상 좌표의 값의 영향을 받는다
                board[i][j] = 1 + min(board[i - 1][j], board[i - 1][j - 1], board[i][j - 1])
                # 최대값 갱신
                if answer < board[i][j]:
                    answer = board[i][j]

    return answer ** 2