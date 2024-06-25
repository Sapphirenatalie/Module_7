file_name = 'Byron.txt'
with open(file_name, mode='r', encoding='utf8') as file:
    file_content = file.read()
    print(file_content)

print(file.closed)

# Использование оператора with open(file_name...) отличается от простого использования file.close() тем,
# что оператор with open(file_name...) закрывает автоматически файл после прочтения
# и нет необходимости использовать функцию close().
# Оператор вызывает 2 встроенных метода - __enter()__ и __exit()__.
# Так как он закрывает файл, то получается меньше кода.
