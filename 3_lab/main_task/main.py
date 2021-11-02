import re


# искомый смайлик
# =<(

# создаем функцию проверки файла с текстом на количество смайликов
def count_smiles(filename):
    pattern = re.compile(r'=<\(')
    file_to_check = open(filename)
    test_string = file_to_check.read()
    return len(pattern.findall(test_string))


# Запускам пять тестов для проверки написанной функциий
for i in range(1, 6):
    string_name = 'string_' + str(i) + '.txt'
    print("Количество смайликов в тесте номер: " + str(i) + " равно " + str(count_smiles(string_name)))
