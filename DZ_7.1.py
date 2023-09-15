# ВинниПух Парам пам-пам

def ritm(str):
    str = str.split()
    list_1 = []
    for word in str:
        sum_w = 0
        for i in word:
            if i in 'аеёиоуыэюя':
                sum_w += 1
        list_1.append(sum_w)
    return len(list_1) == list_1.count(list_1[0])
str_1 = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
if ritm(str_1):
        print('Парам пам-пам')
else:
    print('Пам парам')