N = int(input())
B = list(map(int, input().split()))

cnt = 0
A = [0 for _ in range(len(B))]

while A != B:
    # 홀수 처리하기 -> -1
    for i in range(len(B)):
        if B[i] % 2 == 1:
            B[i] -= 1
            cnt += 1

    # 짝수 처리하기
    if all(j == 0 or j % 2 == 0 for j in B):    # 모든 원소가 0이거나 짝수일 경우
        if A != B:
            B = [(j // 2) for j in B]
            cnt += 1

print(cnt)