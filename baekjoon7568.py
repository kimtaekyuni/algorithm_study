N = int(input()) # input은 값 넣을 수 있는 녀석 만드는 녀석

sizelist = [] # list 형성 

for _ in range(N): #작성한 n만큼 x,y값 작성할 수 있도록 map함수 사용
    x,y = map(int,input().split()) # map 
    sizelist.append((x,y))

for size in sizelist: 
    rank = 1 # 기본 랭킹을 1로 설정. size는 sizelist의 요소들이 돌아가며 설정
    for compare_size in sizelist: # sizelist의 요소들이 돌아가며 comparesize로 설정
        if size[0] < compare_size[0] and size[1] < compare_size[1]:  # 비교 랭크가 더 크면 size요소 rank더하기 
            rank += 1 #for 두 번 쓰는 거에 익숙해지기 
    
    print(rank, end=' ') # end는 끝나고 빈칸 



