
n = int(input('Введите количество монеток: '))
k = 0
for i in range(n):
    v = int(input('Введите 0 или 1: '))
    if v == 1:
        k += 1
print(k if k<n/2 else n-k)