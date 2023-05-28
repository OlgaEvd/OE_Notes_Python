import view as v
import model as m
from tabulate import tabulate

def actions():
    while True:
        v.menu()
        user_command = input(v.number)
        if user_command == '0':
            v.exit()
            exit()
        elif user_command == '1':
            m.show_all()
        elif user_command == '2':
            m.search_by_id()
        elif user_command == '3':
            m.search_by_date()
        elif user_command == '4':
            m.create_note()
        elif user_command == '5':
            m.change_note()
        elif user_command == '6':
            m.del_note()
        elif user_command not in ['0', '1', '2', '3', '4', '5', '6']:
            v.error()
            continue
        else:
            break
