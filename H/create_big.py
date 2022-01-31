import random

N = 200_000
K = random.randrange(N * (N + 1) // 2) + 1
MAX_V = 10 ** 9

print(N, K)
print(' '.join(str(random.randrange(MAX_V + 1)) for _ in range(N)))