from itertools import combinations

N = int(input())
num = []
for i in range(1, 11):  # 자리수 -> 중복 없이니까 최대 10자리까지 가능
    for c in combinations(range(10), i):
        num.append(int(''.join(map(str, sorted(c, reverse=True)))))

num.sort()

if N <= len(num):
    print(num[N - 1])
else:
    print(-1)