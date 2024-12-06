def custom_write(file_names, strings):
    strings_positions = {}
    line_number = 1
    file = open(file_names, 'a', encoding='utf-8')
    for string in strings:
        byte_position = file.tell()
        file.write(str(string) + '\n')
        strings_positions[(line_number, byte_position)] = string
        line_number += 1
    file.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)