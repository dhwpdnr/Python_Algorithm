import heapq

# 다익스트라 알고리즘
# 현재 노드에서 인접한 노드를 확인하고, 그 경로가 더 짧다면 업데이트
# dijkstra 함수는 그래프와 시작점을 입력으로 받아 최단 거리를 반환
def dijkstra(graph, start):
    # 최단 경로 저장 딕셔너리, 시작점의 거리는 0으로 설정
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # 우선순위 큐 (heapq 사용)
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # 이미 처리된 노드라면 스킵
        if current_distance > distances[current_node]:
            continue

        # 현재 노드의 인접 노드 확인
        for adjacent, weight in graph[current_node].items():
            distance = current_distance + weight

            # 더 짧은 경로 발견 시 업데이트
            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(priority_queue, (distance, adjacent))

    return distances


# 그래프를 딕셔너리로 표현 (인접 리스트)
# graph: 각 노드와 그 인접 노드를 딕셔너리로 표현
# 인접한 노드와 그 사이의 가중치를 포함한 인접 리스트 방식
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# 'A'에서 시작하는 다익스트라 알고리즘 실행
start_node = 'A'
shortest_paths = dijkstra(graph, start_node)

print(shortest_paths)
