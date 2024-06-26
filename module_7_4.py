import os
import time

directory = r"C:\Users\saffi\PycharmProjects\Lessons\Homeworks\07_module_hw"
directory_normalized = os.path.abspath(directory)

print(f'Исправленная директория:\n{directory_normalized}')
count = 0

for root, dirs, files in os.walk(directory_normalized):
    for file in files:
        count += 1
        print(f'{'<>' * 35}')
        filepath = os.path.join(root, file)
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%B.%Y %H:%M", time.localtime(filetime))
        create_time = os.path.getctime(filepath)
        formatted_create_time = time.strftime("%d.%B.%Y %H:%M", time.localtime(create_time))
        file_size = os.path.getsize(filepath)
        parent_dir = os.path.dirname(filepath)
        print(f'Обнаружен файл № {count}: {file} \nПуть:\n{filepath}\n'
              f'Размер: {file_size} байт\nВремя создания: {formatted_create_time}\n'
              f'Время изменения: {formatted_time}\nРодительская директория:\n{parent_dir}')
    print(f'{'<>' * 35}')
    print(f'\nВсего обнаружено файлов: {count}')
