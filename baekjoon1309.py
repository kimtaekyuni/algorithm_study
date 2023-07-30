n = int(input())

def fibonacci(n):
    a, b = 3, 7  # 초기값 설정
    for _ in range(3, n + 1):
        a, b = b, 2 * b + a  # 값을 계산하여 갱신
    return b

print(fibonacci(n) % 9901)
 