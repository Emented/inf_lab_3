import re


# вариант 3

# ищем все фамилии в тексте и помещаем их в массив
def find_surnames(filename):
    file_to_check = open(filename)
    test_text = file_to_check.read()
    surnames = re.findall(r'\b[А-Яё][а-яё]+ [А-ЯЁ].[А-ЯЁ].', test_text)
    return surnames


# пробегаемся по тестам и выводим фамилии, обрезая инициалы
for i in range(1, 6):
    string_name = 'string_' + str(i) + '.txt'
    finalSurnames = find_surnames(string_name)
    if len(finalSurnames) == 0:
        print('Тест ' + str(i))
        print("Нет фамилий")
        print()
    else:
        print('Тест ' + str(i))
        for surname in sorted(finalSurnames):
            print(surname[:-5])
        print()
