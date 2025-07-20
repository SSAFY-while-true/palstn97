H, W = map(int, input().split())
arr = list(map(int, input().split()))

total = 0

for i in range(1, W - 1):
    l = max(arr[:i])
    r = max(arr[i + 1:])
    now = min(l, r)

    if now - arr[i] >= 0:
        total += (now - arr[i])

print(total)