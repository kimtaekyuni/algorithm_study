N, K =map(int, input().split())
if N >= K: # 콘센트 넣는게 총 넣어야 하는 경우보다 많을 때는 아예 플러그를 뺼 필요 X
    print(0)
    exit()

elec_list = list(map(int, input().split())) # 넣어야 하는 콘센트 입력 

plug = set() #중복되지 않은 고유한 원소들로 이루어진 집합. 
cnt = 0 

def find_latest(idx): #다 플러그에 넣으면서 max_idx값 업로드하면서 수정 
    result = 0
    max_idx = -1 #max_idx가 0인 경우 그 값의 idx값이 넘어가야 하므로 초기값을 -1로 설정. -100으로 하든 뭘로 하든 상관 x
    for num in plug : # plug요소 하나씩 num에 넣으면서 
        try :
            num_idx = elec_list[idx:].index(num) # idx수 이후 요소부터 num 이 등장하는 제일 빠른 수
        except:
            num_idx = K #마지막일 때 예외 
        if max_idx < num_idx : # 제일 멀리 있는 idx 계속 찾기 
            result, max_idx = num, num_idx # 값 업로드 

    return result

for idx, num in enumerate(elec_list): # idx는 요소 순서, num에는 요소값 들어감
    plug.add(num) # 지금 꼽아야 하는 거  없음 추가. plug가 set이라서 발생..
    if len(plug) > N: # 꼽아야 하는 물품 확인 (없으면 바로 print(cnt)하면 됨)
        cnt += 1 # 꼽아야 하는 물품이 콘센트 총 가능 수 보다 많음으로 꽂기
        lastest_used = find_latest(idx) # 제일 마지막에 사용하는 것 찾기
        plug.discard(lastest_used) #제일 마지막에 재사용하는 것 삭제
    
print(cnt)


