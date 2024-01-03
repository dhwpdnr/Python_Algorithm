import sys


# 덧셈하여 타켓을 만들 수 있는 배열의 두숫자의 인덱스를 리턴
# 입력 : nums = [2, 7, 11, 15]  target = 9
# 출력 [0, 1]
# 브루트 포스
# 시간 복잡도 = O(n^2)
def two_sum_bp(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


# in을 이용한 탐색
# target에서 첫번째 값을 뺀 값이 존재하는지 확인하는 방식
# 시간 복잡도 = O(n^2)
# 같은 시간 복잡도라도 브루트포스 방식보다 빠르다
def two_sum_in(nums, target):
    for i, n in enumerate(nums):
        complement = target - n
        if complement in nums[i + 1:]:
            return [nums.index(n), nums[i + 1:].index(complement) + (i + 1)]


# 첫번째 수를 뺀 결과를 키로 조회
# 시간 복잡도 = O(n)
# 이전 방식에서 조회하는 방식 개선
def two_sum_key(nums, target):
    nums_map = {}
    # 키와 값을 바꿔서 딕셔너리로 저장
    for i, num in enumerate(nums):
        nums_map[num] = i

    # 타켓에서 첫번째 수를 뺀 결과를 키로 조회
    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]:
            return [i, nums_map[target - num]]


# 조회 구조 개선
# 이전 방식과 큰 차이는 없으나, 반복문을 한번 줄임으로 코드가 간결해짐
def two_sum_key(nums, target):
    nums_map = {}
    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target - num], i]
        nums_map[num] = i


# 투포인터 방식
# 위 문제는 합을 이루는 값이 아닌 인덱스를 구하는 문제라서
# 정렬이 필요한 투포인터를 사용 할 수 없다
def two_sum_two_pointer(nums, target):
    left = 0
    right = len(nums) - 1
    while left != right:
        if nums[left] + nums[right] < target:
            left += 1
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            return [left, right]


q = two_sum_key([2, 7, 11, 15], 9)
assert q == [0, 1]
print(q)


# 빗물 트래핑
# 높이를 입력 받아 비 온 후 얼마나 많은 물이 쌓일 수 있는지 계산
# 입력 : [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# 출력 : 6


# 투포인터를 최대로 이용
# 최대 높이의 막대까지 각각 좌우기둥의 최대높이와 현재 높이와의 차이 만큼 더해간다
# 시간 복잡도 : O(n)
def trap_two_pointer(height):
    if not height:
        return 0

    volume = 0
    left = 0
    right = len(height) - 1
    left_max = height[left]
    right_max = height[right]

    while left < right:
        left_max = max(height[left], left_max)
        right_max = max(height[right], right_max)

        # 더 높은 쪽을 향해 투포인터 이동
        if left_max <= right_max:
            volume += left_max - height[left]
            left += 1
        else:
            volume += right_max - height[right]
            right -= 1
    return volume


# 스택을 활용
# 현재 높이가 이전 높이보다 높을 때 (꺾이는 부분)을 기준으로 격차만큼 물 높이를 채운다
# 시간 복잡도 : O(n)
def trap_stack(height):
    stack = []
    volume = 0
    for i in range(len(height)):
        # 변곡점을 만나는 경우
        while stack and height[i] > height[stack[-1]]:
            # 스택에서 꺼내기
            top = stack.pop()
            if not len(stack):
                break
            # 이전과의 차이만큼 물 높이 처리
            distance = i - stack[-1] - 1
            waters = min(height[i], height[stack[-1]]) - height[top]
            volume += distance * waters
        stack.append(i)
    return volume


q = trap_stack([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
assert q == 6
print(q)


# 주식 시장에서 한번의 거래로 낼 수 있는 최대의 이득
# 입력
# [7,1,5,4,6,4]
# 출력
# 5


# 브루트 포스
def max_profit_bp(prices):
    max_price = 0

    for i, price in enumerate(prices):
        for j in range(i, len(prices)):
            max_price = max(prices[j] - price, max_price)

    return max_price


# 지점과 현재값과의 차이 계산
def max_profit(prices):
    profit = 0
    min_price = sys.maxsize
    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)
    return profit


q = max_profit([7, 1, 5, 4, 6, 4])
assert q == 5
print(q)
