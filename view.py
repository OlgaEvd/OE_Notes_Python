def menu():
    print("\n"
        "******************** Приложение Заметки*********************\n"
          "* 1 - Показать все заметки                                 *\n"
          "* 2 - Найдите заметку по ID и показать её                  *\n"
          "* 3 - Найти все заметки по дате последнего изменения       *\n"
          "* 4 - Добавить новую заметку                               *\n"
          "* 5 - Редактировать                                        *\n"
          "* 6 - Удалить                                              *\n"
          "* 0 - Выход                                                *\n"
          "************************************************************")


def exit():
    print("\n""Выход из заметок\n")


def error_view():
    print('Неверный ввод. Попробуйте еще раз, пожалуйста.')


def create_data():
    print('Файл базы данных не существует или был поврежден.')


number = 'Пожалуйста, введите выбранный вами номер:'

next = 'Чтобы продолжить, нажмите Enter'