# 유효한 괄호
# 입력 : ()[]{}
# 출력 : true

# 스택을 활용한 유효 괄호 확인
def is_valid(s):
    stack = []
    table = {
        ")": "(",
        "}": "{",
        "]": "["
    }
    for c in s:
        if c not in table:
            stack.append(c)
        elif not stack or table[c] != stack.pop():
            return False
    return len(stack) == 0


q = is_valid("()[]{}")
assert q == True
print(q)


# 매일의 화씨 온도를 리스트로 입력 받아서 더 따뜻한 날씨를 위해서는 며칠을 더 기다려야 하는지를 출력
# 입력 : T = [73, 74, 75, 71, 69, 72, 76, 73]
# 출력 : [1, 1, 4, 2, 1, 1, 0, 0]
def daily_temperature(T):
    answer = [0] * len(T)
    stack = []
    for i, cur_temp in enumerate(T):
        while stack and cur_temp > T[stack[-1]]:
            last = stack.pop()
            answer[last] = i - last
        stack.append(i)
    return answer


q = daily_temperature([73, 74, 75, 71, 69, 72, 76, 73])
assert q == [1, 1, 4, 2, 1, 1, 0, 0]
print(q)


