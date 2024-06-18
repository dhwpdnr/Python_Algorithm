"""
퇴각검색이라고도 불리며 이는 한정 조건을 가진 문제를 풀려는 전략이다.
어떤 문제를 푸는데 있어 모든 경우의 수를 시도하여 문제의 정답을 찾아나간다.
그러나 이때, 한정조건을 가지고 있어서 불필요한 경우의 수를 시도하지 않는다.ㄴ
"""
import sys

li = [[1, 5, 3], [2, 5, 7], [5, 3, 5]]
chk = [False] * 3
m = sys.maxsize


def backtracking(row, score):
    if row == 4:  # 재귀함수를 마치는 조건
        if score < m:
            return
    for i in range(1, 4):
        if chk[i] == False:  # 백트래킹에서의 한정조건
            chk[i] = True
            backtracking(row + 1, score + li[row][i])
            chk[i] = False
    return


backtracking(1, 0)
print(m)
