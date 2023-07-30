M = int(input()) #케이스 개수 
list_N = [] # n값 리스트로 저장



for _ in range(M): # n값 for문으로 list에서 꺼내기
    N = int(input())
    list_N.append(N)

for put in range(M): # a1 + a2 = a4라는 규칙 찾음
    n = list_N[put]
    a = 1
    b = 1
    c = 1
    for k in range(1, n+1): #찾는 값은 d가 아니라 마지막 단계에서의 a이므로
        d = a + b
        x = d - b #다음 단계를 위한 a,b,c값 변동이 아래 코드에서 이뤄지므로 미리 x값을 저장해서 이를 해결
        a, b, c = b, c, d 

    print(x)



