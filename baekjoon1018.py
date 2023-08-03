N, M = map(int,input().split()) 
original = [] #원래 바둑판
count = [] 

for _ in range(N):
    original.append(input()) #M은 알아서 맞춰서 써도 되니까 N만. 입력값이 뭔지 보고 생각하기

for a in range(N-7): #시작지점 설정 (가로 세로니까 a, b로)
    for b in range(M-7):
        draw1 = 0 #시작점이 B인경우 
        draw2 = 0 #시작점이 W인경우 
        for i in range(a, a+8): # 한 줄씩 비교하며 draw 값 늘리기
            for j in range(b, b+8): 
                if (i+j) % 2 == 0: 
                    if original[i][j] != 'W':
                        draw1 += 1
                    if original[i][j] != 'B':
                        draw2 += 1
                else:
                    if original[i][j] != 'B':
                        draw1 += 1
                    if original[i][j] != 'W':
                        draw2 += 1
                        
        count.append(min(draw1, draw2)) #첫 칸이 흰색이거나 검은색인 경우만 존재 -> 두 가지 경우 count하고 min값 업로드
        

print(min(count))              
