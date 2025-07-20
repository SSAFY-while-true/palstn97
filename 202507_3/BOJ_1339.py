N = int(input())
words = []
for _ in range(N):
    words.append(input())

weights = {}    # 가중치의 총합을 저장할 딕셔너리

for w in words:
    l = len(w)
    for i, c in enumerate(w):   # 각 단어에 대해 알파벳의 자릿수별 가중치
        v = 10 ** (l - i - 1)
        if c in weights:
            weights[c] += v
        else:
            weights[c] = v

sorted_weights = sorted(weights.items(), key=lambda x: x[1], reverse=True)  # 가중치 기준으로 내림차순 정렬
# 가중치가 큰 알파벳이 가장 앞으로 오게 만들기 -> 차례대로 9부터 할당
num = 9
total = 0
for c, w in sorted_weights:
    total += w * num    # 가중치 * 숫자
    num -= 1

print(total)