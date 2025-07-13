N = int(input())
tower = list(map(int, input().split()))
hit = [0] * N   # 수신하는 곳

stack = []

for i in range(N):
    while stack:
        if tower[i] > tower[stack[-1]]: # 현재 탑이 왼쪽 탑보다 높으면 신호 보낼 수 없기에 pop
            stack.pop()
        else:
            hit[i] = stack[-1] + 1  # 그렇지 않다면 수신이 가능하기에 break
            break
    stack.append(i)

print(*hit)