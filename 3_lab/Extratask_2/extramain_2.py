import re


# вариант 1

def find_words(filename):
    file_to_check = open(filename)
    test_text = file_to_check.read()
    final_words = re.findall(r'\b([йцкнгшщзхъфвпрлджчсмтьб]*([ауоиэыеёяю])[йцкнгшщзхъфвпрлджчсмтьб]*((\2){1,}[йцкнгшщзхъфвпрлджчсмтьб]*)*)\b', test_text)
#    print(final_words)
    final = []
    for i in final_words:
        final.append(i[0])
    return sorted(final, key=len)


for i in range(1, 6):
    string_name = 'string_' + str(i) + '.txt'
    words_list = find_words(string_name)
    print('Тест ' + str(i))
    if len(words_list) != 0:
        print(*words_list, sep='\n')
        print()
    else:
        print("Нет подходящих слов")
        print()
