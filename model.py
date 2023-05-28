from datetime import datetime
from tabulate import tabulate
from os import path
import csv
import view as v

db_file = 'notes.csv'
notebook = []
last_id = 0
headers = ['ID', 'Дата', 'Заголовок', 'Текст']


def read_file():
    global notebook, db_file, last_id, headers
    while True:
        if path.exists(db_file):
            with open(db_file, mode='r', encoding='utf-8', newline='') as file:
                reader = csv.reader(file, delimiter=';')
                notebook = [line for line in reader]
            last_id = int(notebook[-1][0])
            return notebook
        else:
            v.create_data()
            ask_user = input('Хотели бы вы создать новую базу данных (y/n): ')
            if ask_user.lower() == 'y':
                with open(db_file, mode='w', encoding='utf-8', newline='') as file:
                    writer = csv.writer(file, delimiter=';')
                    writer.writerow(headers)
                id_num = last_id + 1
                print('Пожалуйста, создайте новую заметку.')
                note_date = datetime.now().strftime("%Y-%m-%d %H:%M")
                note_title = input('Введите заголовок: ')
                note_text = input('Введите текст: ')
                new_note = [str(id_num), note_date, note_title, note_text]
                add_data(new_note)
                print('Заметка успешно сохранена.')
                input(v.next)
                break
            elif ask_user.lower() == 'n':
                v.exit()
                exit()
            else:
                v.error_view()


def write_file(new_db):
    with open(db_file, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        for line in new_db:
            writer.writerow(line)


def add_data(new_data):
    with open(db_file, mode='a', encoding='utf-8', newline='\n') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(new_data)


def create_note():
    read_file()
    id_num = last_id + 1
    note_date = datetime.now().strftime("%Y-%m-%d %H:%M")
    note_title = input('Введите заголовок: ')
    note_text = input('Введите текст ')
    new_note = [str(id_num), note_date, note_title, note_text]
    add_data(new_note)
    print('Заметка успешно сохранена.')
    input(v.next)


def find_note(num_id):
    read_file()
    index_id = 0
    for i in range(1, len(notebook)):
        if notebook[i][0] == num_id: index_id = i
    return index_id


def show_all():
    read_file()
    result = [[line[i] for i in range(3)] for line in notebook]
    print(tabulate(result, headers='firstrow', tablefmt='pipe', stralign='center'))
    input(v.next)


def search_by_id():
    read_file()
    search = input('Введите ID заметки для поиска: ')
    if search == '':
        v.error_view()
    else:
        result = searching(id_note=search)
        if len(result) == 0:
            print('Заметка не найдена.')
        else:
            print(tabulate(result, headers=headers, maxcolwidths=[None, None, None, 100]))
    input(v.next)


def search_by_date():
    read_file()
    search = input('Введите дату создания или изменения\n'
                   '(в формате ГГГГ-MM-ДД, где ГГГГ - год, MM - месяц, ДД - день, ПРИМЕР: 2020-01-01): ')
    search_result = searching(date_note=search)
    if len(search_result) == 0:
        print('Заметки с такой датой не найдены.')
    else:
        result = [[line[i] for i in range(3)] for line in search_result]
        print(tabulate(result, headers=['ID', 'Дата', 'Заголовок']))
    input(v.next)


def searching(id_note='', date_note=''):
    result = []
    for row in notebook:
        if id_note != '' and row[0] != id_note: continue
        if date_note != '' and row[1].find(date_note): continue
        result.append(row)
    return result


def change_note():
    id_num = input('Введите ID для редактирования: ')
    ch_id_ind = find_note(id_num)
    if ch_id_ind == 0:
        print('Заметка не найдена.')
    else:
        print('Заметка найдена.')
        print(*notebook[ch_id_ind], sep='\t')
        ask_user = input("Подтвердите свой выбор (y/n): ")
        if ask_user.lower() == 'y':
            note_date = datetime.now().strftime("%Y-%m-%d %H:%M")
            note_title = input('Введите заголовок: ')
            note_text = input('Введите текст: ')
            notebook[ch_id_ind] = [str(id_num), note_date, note_title, note_text]
            write_file(notebook)
            print(f'Заметка с ID {id_num} была успешно изменена!')
            input(v.next)
        elif ask_user.lower() == 'n':
            print(f'Заметка с ID {id_num} не была изменена!')
            input(v.next)
        else:
            v.error_view()


def del_note():
    id_num = input('Введите ID удаляемой заметки: ')
    del_id_index = find_note(id_num)
    if del_id_index == 0:
        print('Заметка не найдена.')
    else:
        print('Заметка найдена.')
        print(*notebook[del_id_index], sep='\t')
        ask_user = input("Подтвердите удаление (y/n): ")
        if ask_user.lower() == 'y':
            note_date = datetime.now().strftime("%Y-%m-%d %H:%M")
            notebook[del_id_index] = [str(id_num), '', f'<Deleted {note_date}>', '']
            write_file(notebook)
            print(f'Заметка с ID {id_num} была успешно удалена!')
            input(v.next)
        elif ask_user.lower() == 'n':
            print(f'Заметка с ID {id_num} не была удалена!')
            input(v.next)
        else:
            v.create_data()
