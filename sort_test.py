# 버블 정렬
# 배열의 아이템을 쭉 살펴보면서 연달아 있는 아이템 2개의 순서가 잘못되어 있는것을 발견하면 두 아이템을 바꾼다
# 시간 복잡도 : O(n^2)

def bubble_sort(A):
    for i in range(1, len(A)):
        for j in range(0, len(A - 1)):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[i]


# 퀵정렬 분할 정복 알고리즘으로 피벗이라는 개념을 통해
# 피벗보다 작으면 왼쪽, 크면 오른쪽과 같은 방식으로 파티셔닝하면서 쪼개나간다
def quick_sort(A, hi, lo):
    def partition(lo, hi):
        pivot = A[hi]
        left = lo
        for right in range(lo, hi):
            if A[right] < pivot:
                A[left], A[right] = A[right], A[left]
                left += 1
        A[left], A[hi] = A[hi], A[left]
        return left

    if lo < hi:
        pivot = partition(lo, hi)
        quick_sort(A, lo, pivot - 1)
        quick_sort(A, pivot + 1, hi)


# 구간 병합
# 겹치는 구간을 병합
# 입력: [[1, 3], [2, 6], [8, 10], [15, 18]]
# 출력: [[1, 6], [8, 10], [15, 18]]

# 정렬하여 병합
# 시간 복잡도 : O(n log n)
def merge(intervals):
    merged = []
    for i in sorted(intervals, key=lambda x: x[0]):
        if merged and i[0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], i[1])
        else:
            merged += i,
    return merged


q = merge([[1, 3], [2, 6], [8, 10], [15, 18]])
assert q == [[1, 6], [8, 10], [15, 18]]
print(q)
