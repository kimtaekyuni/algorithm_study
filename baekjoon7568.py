N = int(input()) # input은 값 넣을 수 있는 녀석 만드는 녀석

sizelist = [] # list 형성 

for _ in range(N): #작성한 n만큼 x,y값 작성할 수 있도록 map함수 사용
    x,y = map(int,input().split()) # map 
    sizelist.append((x,y))

for size in sizelist:
    rank = 1 
    for compare_size in sizelist:
        if size[0] < compare_size[0] and size[1] < compare_size[1]: 
            rank += 1 #for 두 번 쓰는 거에 익숙해지기
    
    print(rank, end=' ') # end는 끝나고 빈칸 



'''
N = int(input())
sizeList = []

for _ in range(N):
    x, y = map(int, input().split())
    sizeList.apepend((x,y))

for size in sizeList:
    rank = 1
    for compare_size in sizeList:
        if size[0] < compare_size[0] and size[1] < compare_size[1];
            rank += 1
    
    print('rank', end=' ')

'''

