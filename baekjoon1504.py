#입력칸 시작
import sys
import heapq
input = sys.stdin.readline # 더 빠른 입력을 위한 것
INF = int(1e9) 

N, E = map(int, input().split())
graph = [[] for _ in range(N+1)] # graph list 생성 (정점 개수 + 1개 만큼)

for _ in range(E): # 양 방향이므로 
    a, b, c = map(int, input().split()) 
    graph[a].append((b, c)) 
    graph[b].append((a, c)) 

def dijkstra(start): 
    distance = [INF] * (N + 1) # 시작 정점 - 각 정점까지의 최단 거리 저장 리스트. 모두 무한대로 초기화
    q =[] #최소 힙을 활용해 최단 거리를 관리할 우선순위 큐
    heapq.heappush(q, (0, start)) #최단거리 q에 (0,start)쌍 삽입 
    distance[start] = 0 #시작 정점의 최단거리를 0으로 설정 

    while q: # 우선순위 큐가 비어있지 않을 때까지 반복
        dist, now =  heapq.heappop(q) #우선순위 큐에서 가장 최단 거리를 가진 정점을 꺼내어 dist와 now에 할당

        if distance[now] < dist: # 이미 해당 정점까지의 최단거리가 더 짧은 경우 해당 정점을 무시하고 다음 반복으로 진행
            continue

        for i in graph[now]: # 현재 정점과 연결된 모든 인접 정점들에 대해 반복
            c = dist + i[1] #현재 정점을 거쳐서 i[0]까지의 거리를 계산 / i[1]은 현재 정점과 인접 정점 사이의 가중치

            if distance[i[0]] > c: #시작 정점으로부터 인접 정점까지의 거리가 c보다 크면 해당 거리를 업데이트하고 우선순위 큐에 (거리, 정점) 쌍을 삽입
                distance[i[0]] = c
                heapq.heappush(q, (c, i[0]))
    return distance

c1, c2 = map(int, input().split())

original_distance = dijkstra(1) 
c1_distance = dijkstra(c1)
c2_distance = dijkstra(c2)

c1_path = original_distance[c1] + c1_distance[c2] + c2_distance[N]
c2_path = original_distance[c2] + c2_distance[c1] + c1_distance[N]

result = min(c1_path, c2_path)
print(result if result < INF else -1)


#입력칸 끝

# 경우의 수 2개 1)  c1, c2 순서 / 2) c2, c1 순서 
# 각 포인트까지의 최소값 구하고 더하기 ㄱㄱ

#situation 1) 1에서 v1, v2, N 순서 

#1부터 v1 최단거리 






