N = int(input())
# 사면체 수를 리스트에 저장
bomb = []
layer = 1   # 현재 층 수
total = 0

while total <= N:
    total += (layer * (layer + 1)) // 2
    bomb.append(total)
    layer += 1

dp = [float('inf')] * (N + 1)
dp[0] = 0

for b in bomb:
    for i in range(b, N + 1):   # i는 지금까지 쌓은 대포알 개수
        dp[i] = min(dp[i], dp[i - b] + 1)   # 최소 사면체 수가 dp[N]

print(dp[N])