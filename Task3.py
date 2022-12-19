# 3. В файле, содержащем фамилии студентов и их оценки, изменить на буквы в верхнем регистре тех студентов, которые имеют средний балл более «4».


from typing import List


def change_list(file: List[str], for_change: str) -> str:
    new_list = ''
    for i in file:
        if i.count(for_change):
            i = i.upper()
        string = i + '\n'
        new_list += string
    return new_list


new_list = open('list1.txt', 'r', encoding='utf-8')
lines_read = new_list.read().split('\n')
new_list.close()

result_list = change_list(lines_read, for_change='5')

new_list = open('list1.txt', 'w', encoding='utf-8')
new_list.write(result_list)
new_list.close()
