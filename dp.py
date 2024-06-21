# 앞에서 계산한 식을 배열에 미리 저장하여 연산속도를 증가시키는 프로그래밍
# 계산한 건 다시 계산하지 않는 게 중요

# 피보나치 수열
def fibo(x):
    if x == 1 or x == 2:
        return 1  # 첫번째와 두번째 수열은 1이므로 1을 return
    return fibo(x - 1) + fibo(x - 2)  # 3번째 부터는 x-1번째, x-2번째 수열의 합을 통해 수열을 구함


print(fibo(4))

# 다이나믹 프로그래밍 방식
# 탑다운(하향식, 메모이제이션 사용. 위=>아래)
# 바텀업(상향식. 아래=>위)

# 탑다운
# (1) 한 번 계산한 결과를 메모리 공간에 메모한다.(메모이제이션)
# - 같은 문제를 다시 호출하면, 메모한 결과를 그대로 가져온다
# -값을 기록해놓는다는 점에서 캐싱이라고도 함. 보통 dp, d 등의 이름으로 선언된다.
# (2) 재귀함수가 사용된다.

d = [0] * 100  # dp 테이블 초기화


def fibo(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:  # 이미 계산한 적이 있는 문제라면 그대로 반환
        return d[x]
    d[x] = fibo(x - 1) + fibo(x - 2)  # 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
    return d[x]


# 바텀업
# 작은 문제 + 작은문제 => 큰 문제가 되는 형식
# 반복문을 이용한다.

d = [0] * 100  # dp 테이블 초기화
d[1] = 1
d[2] = 1
n = 99  # 피보나치 수열의 99번째 수열을 구하기 위해

for i in range(3, n + 1):
    d[i] = d[i - 1] + d[i - 2]

print(d[n])
