N = int(input()) 

A = list(map(int, input().split()))
answer = 0

for a in range(N): # 시간 복잡도는 극악이지만 하나하나 다 체크하기 
    start = A[a] 
    number_length = 1
    for b in range(a+1, N): #앞에서부터 순서대로 만약에 number_length가 카운트 되면 start를 A[b]로 바꿔서 계속 증가 수열이 유지될 수 있도록 설정
        if start < A[b]:
            number_length += 1    
            start = A[b]
        
    answer = max(answer, number_length) #비교 후 항상 최댓값만 업로드

print(answer)
