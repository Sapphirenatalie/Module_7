file_name = "test"
strings = ['Text for tell.', 'Используйте кодировку utf-8.', 'Because there are 2 languages!', 'Спасибо!']


def custom_write(file_name, strings):
    count = 0
    dictionary = {}
    with open('test.txt', 'w', encoding='utf8') as fw:
        for line in strings:
            count += 1
            dictionary[(count, fw.tell())] = line
            fw.write(line + '\n')
    for keys, values in dictionary.items():
        print((keys, values))


custom_write('test', strings)
