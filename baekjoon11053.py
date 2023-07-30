N = int(input())

A = list(map(int, input().split()))
answer = 0

for a in range(N):
    start = A[a]
    number_length = 1
    for b in range(a+1, N):
        if start < A[b]:
            number_length += 1    
            start = A[b]
        
    answer = max(answer, number_length)

print(answer)
