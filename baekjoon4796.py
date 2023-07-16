case = 1
results=[]

while True:
    L, P, V = map(int, input().split()) #L: 사용 가능한 날짜, P: 사용 가능한 날짜 1차 범위, V: 휴가 기간

    if L == 0 and P == 0 and V == 0:
        break

    def divide(V, P):
        c = V // P # 몫
        d = V % P # 나머지
        return c, d 

    c, d = divide(V, P)
    availble_use=0

    while c != 0 or d > L :
        if c >= 1:
            availble_use += L
            c -= 1
        else:
            availble_use += L 
            d = 0

    availble_use += d

    results.append((case, availble_use))
    case += 1

for case, result in results:
    print("Case {}:{}".format(case, availble_use))