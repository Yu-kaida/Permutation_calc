from itertools import permutations

balls = list(map(int, input().split()))
num = int(input())

res = list(permutations(balls, num))
print("----------------------------------")
print("答え：" + str(len(res)) + "通り")
print("----------------------------------")