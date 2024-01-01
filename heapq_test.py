import heapq

# 힙은 모든 부모 노드가 자식보다 작거나 같은 값을 갖는 이진 트리


# 빈 리스트에 추가
heap = []
heapq.heappush(heap, 50)
heapq.heappush(heap, 10)
heapq.heappush(heap, 20)
print(f"heap : {heap}")
print()

# 힙 자료형으로 변환
heap2 = [50, 10, 20]
heapq.heapify(heap2)

print(f"heap2 : {heap2}")
print()

# 가장 작은 원소를 힙에서 제거함과 동시에 그를 결괏값으로 리턴
result = heapq.heappop(heap)

print(f"heapq.heappop(heap) : {result}")
print(f"heap : {heap}")
print()

# 원소를 삭제하지 않고 가져오기
result2 = heap[0]

print(f"heap[0] : {result2}")
print(f"heap : {heap}")
print()

# 최대힙 만들기
heap_items = [1, 3, 5, 7, 9]

max_heap = []
for item in heap_items:
    heapq.heappush(max_heap, (-item, item))

print(f"max_heap : {max_heap}")

max_item = heapq.heappop(max_heap)[1]
print(f"max_item : {max_item}")
