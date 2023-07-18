N = int(input())
P = list((map(int, input().split())))

sorted_P = sorted(P)

time_list = []

for num in range(N):
    b = (N - num) * sorted_P[num] 
    time_list.append(b)

print(sum(time_list))
print(sorted_P)