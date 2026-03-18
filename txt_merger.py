'''
txt_merger.py

Утилита для объединения текстовых файлов (.txt) в один файл.

Программа рекурсивно проходит по указанной директории и всем её
вложенным папкам, находит текстовые файлы и последовательно
объединяет их содержимое в один результирующий файл.

Результат работы программы — файл result.txt,
содержащий объединённое содержимое всех найденных txt-файлов.
'''

import os

folder = '.'              # корневая папка, где находится утилита txt_merger.py
output_file = 'result.txt'

with open(output_file, 'w', encoding='utf-8') as outfile:
    for root, dirs, files in os.walk(folder):
        for filename in files:
            if filename.endswith('.txt') and filename != output_file:
                filepath = os.path.join(root, filename)

                with open(filepath, 'r', encoding='utf-8') as infile:
                    # outfile.write(f'--- {filepath} ---\n')
                    outfile.write(infile.read())
                    outfile.write('\n\n')

print('Готово. Все txt-файлы объединены в result.txt')