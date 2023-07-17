N, M = map(int, input().split())
cake = list(map(int, input().split()))

print(cake)

res = 0
start = 0

end = max(cake)

while start <= end:
    mid = (start + end) // 2
    total =  0 
    for l in cake:
        if l>=mid:
            total+=l-mid
        
    if total >= M:
        if mid > res:
            res=mid
        
        start = mid +l
    else: 
        end = mid -l

print(res)

