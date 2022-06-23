def add(x, y):
    return x + y


t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(add(a, b))
