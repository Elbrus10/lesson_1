base_сompany = {
    'yandex': 7000,
    'gazprom': 500,
    'microsoft': 2300,
    'perecrestok': 5400,
    'rosnano': 10,
    'appel': 10000,
    'biocad': 4030,
    'apteka': 299,
    'hiomi': 569,
    'wacom': 8901,
    'adidas': 4313,
    'acron': 6703
}


# Первый вариант - O(N*logN)
def sorted_1(base_сompany):
    list_from_dict = list(base_сompany.items())
    list_from_dict.sort(key=lambda i: i[1], reverse=True)
    for i in range(3):
        print(f"{list_from_dict[i][0]}: {list_from_dict[i][1]}")


# Второй вариант - O(N)
def sorted_2(base_сompany):
    input_max = {}
    list_d = dict(base_сompany)
    for i in range(3):
        maximum = max(list_d.items(), key=lambda k_v: k_v[1])
        del list_d[maximum[0]]
        input_max[maximum[0]] = maximum[1]
    print(input_max)


sorted_1(base_сompany)
sorted_2(base_сompany)
