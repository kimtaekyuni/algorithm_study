from collections import deque #bfs에 사용할 deque import 

N = int(input()) #입력
apt = [[int(x) for x in list(input())] for _ in range(N)] # 아파트 입력

dx = [1, -1, 0, 0] # y 변화량 선언 좌, 우
dy = [0, 0, 1, -1] # x 변화량 선언 위, 아래

def bfs(i, j):
    global apt #apt 변수를 전역 변수로 설정 
    q = deque() #양쪽에서 append가 가능한 것
    q.append([i,j]) 
    apt[i][j] = 0 # 지금 위치 
    cnt = 1
    while q: # q 가 있을 때 까지
        x, y = q.popleft() # deque에 있는 제일 왼쪽 값 없애면서 대입 
        for i in range(4):
            nx = x + dx[i] # 좌우 비교
            ny = y + dy[i] # 위, 아래 비교 
            if 0 <= nx < N and 0 <= ny < N and apt[nx][ny] == 1: # 유효한 범위 안에 있는지
                apt [nx][ny] = 0 # 움직인 곳은 0 으로 변환 
                q.append([nx, ny]) # 현재값 넣기 
                cnt += 1
    return cnt




house = []

for i in range(N):
    for j in range(N):
        if apt[i][j] == 1:
            house.append(bfs(i,j)) # 반환값을 결과값 리스트에 추가

print(len(house)) # 결과값 리스트의 원소 개수 출력 
house.sort() #정렬
for i in house: print(i) # 정렬된 원소 하나씩 출력 