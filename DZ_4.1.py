# Сравнение двух вводимых множеств

firstSetLen = int(input('Введите количество элементов первого множества: '))
secondSetLen = int(input('Введите количество элементов второго множества: '))

setOne = set()
for i in range(firstSetLen):
    setOne.add(input('Введите элемент первого множества: '))
print(setOne)
setTwo = set()
for i in range(secondSetLen):
    setTwo.add(input('Введите элемент второго множества: '))
print(setTwo)
res = sorted(set(setOne)&set(setTwo))
print(f"Пересекающиеся числа данных множеств: {res}")    