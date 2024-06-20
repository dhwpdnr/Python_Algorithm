# 인접행렬로 구현한 방향 그래프
V, E = 6, 8
edge = [0, 1, 0, 2, 0, 5, 0, 6, 4, 3, 5, 3, 5, 4, 6, 4]

adj_matrix = [[0] * (V + 1) for _ in range(V + 1)]

for i in range(E):
    num1, num2 = edge[2 * i], edge[2 * i + 1]
    adj_matrix[num1][num2] = 1

# 인접행렬로 구현한 무방향 그래프
V, E = 6, 8
edge = [0, 1, 0, 2, 0, 5, 0, 6, 4, 3, 5, 3, 5, 4, 6, 4]

adj_matrix = [[0] * (V + 1) for _ in range(V + 1)]

for i in range(E):
    num1, num2 = edge[2 * i], edge[2 * i + 1]
    adj_matrix[num1][num2] = 1
    adj_matrix[num2][num1] = 1

# 인접 리스트로 구현한 방향 그래프
V, E = 6, 8
edge = [0, 1, 0, 2, 0, 5, 0, 6, 4, 3, 5, 3, 5, 4, 6, 4]

# 인접 리스트를 생성하여 각 정점에 연결된 간선 정보를 저장할 배열
adj_list = [[] for _ in range(V + 1)]

for i in range(E):
    # 현재 간선을 구성하는 시작 정점과 끝 정점을 num1, num2 변수에 할당
    # 2*i와 2*i+1은 edge 리스트에서 간선 정보를 가져오기 위한 인덱스
    num1, num2 = edge[2 * i], edge[2 * i + 1]
    # num1 정점에 연결된 간선의 끝 정점 num2를 adj_list 리스트에 추가
    # num1 정점과 num2 정점이 방향성을 가진 간선으로 연결되어 있다는 정보를 인접 리스트에 저장
    adj_list[num1].append(num2)

# 인접 리스트로 구현한 무방향 그래프
V, E = 6, 8
edge = [0, 1, 0, 2, 0, 5, 0, 6, 4, 3, 5, 3, 5, 4, 6, 4]

# 인접 리스트를 생성하여 각 정점에 연결된 간선 정보를 저장할 배열
adj_list = [[] for _ in range(V + 1)]

for i in range(E):
    # 현재 간선을 구성하는 시작 정점과 끝 정점을 num1, num2 변수에 할당
    # 이때 2*i와 2*i+1은 edge 리스트에서 간선 정보를 가져오기 위한 인덱스
    num1, num2 = edge[2 * i], edge[2 * i + 1]
    # num1 정점에 연결된 간선의 끝 정점 num2를 adj_list에 추가
    # 이것은 num1 정점과 num2 정점이 연결되어 있다는 정보를 인접 리스트에 저장하는 것을 의미
    adj_list[num1].append(num2)
    # 무방향 그래프이기 때문에 num2 정점에도 num1 정점을 연결된 간선의 끝 정점으로 추가
    # 이것은 num2 정점과 num1 정점이 연결되어 있다는 정보를 인접 리스트에 저장하는 것을 의미
    adj_list[num2].append(num1)

# 간선 리스트로 구현한 방향 그래프
V = 7
edge = [(1, 2), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 2), (3, 4), (3, 4), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1),
        (5, 2), (5, 4), (6, 4)]

agj_list = [[] for _ in range(V)]

for u, v in edge:
    # 시작 정점 u와 끝 정점 v를 추출하여 adj_list에 각각의 정점을 연결
    # 방향 그래프이므로 u 정점에 v를 추가
    adj_list[u].append(v)

# 간선 리스트로 구현한 무방향 그래프
V = 7
edge = [(1, 2), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 2), (3, 4), (3, 4), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1),
        (5, 2), (5, 4), (6, 4)]

agj_list = [[] for _ in range(V)]

for u, v in edge:
    # 시작 정점 u와 끝 정점 v를 추출하여 adj_list에 각각의 정점을 연결
    # 무방향 그래프이므로 u 정점에 v를, v 정점에 u를 추가
    adj_list[u].append(v)
    adj_list[v].append(u)
