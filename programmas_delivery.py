'''
cap = int(input())
n = int(input())
deliveries = list(int, input().split())
pickups = list(int, input().split())
left = cap # 배달해야 하는 남은 박스 수 
brings = 0 # 가
count = 0 #트럭 왕복 수

def deliverytruck(n):
    for a in range(n): 
        if deliveries[n-a] > 0:
            left =- deliveries[n-a] 

            if left > 0:
                deliveries[n-a] = 0
                continue
            
            elif left == 0:
                deliveries[n-a] = 0
                break

            else:
                deliveries[n-a] = -left
                left = 0
                break
        
        if brings < cap:
            brings += pickups[n-a]

            if brings < cap:
                pickups[n-a] = 0
                continue

            elif brings == cap:
                pickups[n-a] = 0
                break

            else: 
                pickups[n-a] = brings - cap
                brings = cap
                break
        
    count += 1
'''     
# -> 아 이렇게 하면 안됨... brings = 0이 아님 brings = 처음에 cap 으로 시작해야 해. 그리고 brings 와 left를 엮어서 생각해야 하는데.. 음 


# -> 답지 보고 이해하기 

def solution(cap, n, deliveries, pickups):
    answer = 0
    while deliveries or pickups : # if deliveries or pickups is not 0, this roop continues. 
        deliver_cap, pickup_cap = cap, cap
        while deliveries and deliveries[-1] == 0 :
            deliveries.pop()
        while pickups and pickups[-1] == 0 :
            pickups.pop()
        answer += max(len(deliveries), len(pickups))*2 # 어쨌든 배달하든 줍든 가야하니까. pop 통해서 뒤에서 0의 값은 제외하고 남김.
        
        while deliveries and deliver_cap > 0: # pop으로 마지막 요소들 box에 저장해서. deliver_cap과 pickup_cap 줄이기 
            box = deliveries.pop()
            if box <= deliver_cap :
                deliver_cap -= box
            else :
                deliveries.append(box - deliver_cap)
                break
        while pickups and pickup_cap > 0 :
            box = pickups.pop()
            if box <= pickup_cap :  
                pickup_cap -= box 
            else : 
                pickups.append(box - pickup_cap) 
                break 
         
    return answer 

n= int(input())
cap = int(input())
deliveries = list(map(int, input().split()))
pickups = list(map(int, input().split()))

result = solution(cap, n, deliveries, pickups)
print(result)