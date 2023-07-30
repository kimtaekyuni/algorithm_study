N = int(input())
P = list((map(int, input().split())))

sorted_P = sorted(P) #오름차순 정렬

time_list = [] # 한 명당 걸리는 시간 = time_list 요소 

for num in range(N): # 첫 번째 요소는 5번, 두 번째 요소는 4번 곱해지는 원리를 이용
    b = (N - num) * sorted_P[num] 
    time_list.append(b)

print(sum(time_list))