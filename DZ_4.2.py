# Черника карельская
n = int( input( 'Введите количество кустов: ' ) )
list = [ int(x) for x in input( 'Введите количество соседних кустов: ' ).split() ]
n = len(list)
list = list + list[:2]
m = 0
for i in range(n):
    m = max( m, list[i] + list[i+1] + list[i-1] )
print(m)