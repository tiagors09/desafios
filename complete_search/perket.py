n = int(input())

s = 1
b = 0

for i in range(n):
  ingredients = [int(i) for i in input().split()]
  s *= ingredients[0]
  b += ingredients[1]

print(b - s)
