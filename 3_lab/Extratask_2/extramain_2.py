import re


# вариант 1

def find_words(filename):
    file_to_check = open(filename)
    test_text = re.sub('\W+', ' ', file_to_check.read()).split()
    final_words = []
    for word in test_text:
        letter = re.search('[ауоиэыеёяюАУОИЭЫЕЁЯЮ]', word)
        flag = True
        if re.match('[А-ЯЁа-яё]*$', word):
            for checker in re.findall('[ауоиэыеёяюАУОИЭЫЕЁЯЮ]', word):
                if checker != letter[0]:
                    flag = False
            if flag:
                final_words.append(word)
    return sorted(final_words, key=len)


for i in range(1, 6):
    string_name = 'string_' + str(i) + '.txt'
    print('Тест ' + str(i))
    print(*find_words(string_name), sep='\n')
    print()
