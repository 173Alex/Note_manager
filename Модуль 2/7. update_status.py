from time import sleep              # Добавление библиотеки по задержке времени
note = {}                           # Создаём словарь

# Запрашиваем информацию у пользователя и добавляем её в словарь
note["Username"] = input("Введите имя пользователя: ").capitalize()
note["Content"] = input("Введите описание заметки: ").capitalize()
note["Status"] = input("Введите статус заметки (например - 'Выполнено', 'В процессе', 'Отложено'): ").capitalize()
create_date = input("Введите дату создания заметки в формате 'день.месяц.год - ХХ.ХХ.ХХХХ': ")
correct_create_date = create_date[:5]                                                              # Представление корректного отображения даты создания заметки формата 'ДД.ММ - XX.XX'
note["Create_date"] = correct_create_date
issue_date = input("Введите дату истечения заметки в формате 'день.месяц.год - ХХ.ХХ.ХХХХ': ")
correct_issue_date = issue_date[:5]                                                                # Представление корректного отображения даты истечения заметки 'ДД.ММ - XX.XX'
note["Issue_date"] = correct_issue_date

# Добавляем заголовки в словарь
note["Titles"] = []
while True:                                                                                  # Бесконечный цикл с возможностью прерывания от пользователя
    title = input(f"Введите заголовок {len(note['Titles']) + 1} заметки "
                  f"(для завершения ввода - кликните клавишу 'Enter'): ").capitalize()
    if title == '':                                                                          # Условие для завершения ввода от пользователя
        break                                                                                # Окончание цикла после пустого ввода
    if title in note["Titles"]:                                                              # Проверка уникальности введённого заголовка
        print(" Введённый заголовок уже имеется в списке. Укажите другой заголовок.\n")
        sleep(4)
    else:
        note["Titles"].append(title)                                                         # Добавление заголовка в словарь методом ".append"
    print(" Введённые заголовки заметки: ")                                                  # Вывод на экран всех введённых заголовков заметок сразу после ввода от пользователя
    for values_ in note["Titles"]:                                                           # Цикл для перебора значений словаря по ключу для построчного вывода "list"
        print(f'- {values_}')
    print()

# Функция по выводу данных
def data_output(dict_):                                         # Вывод данных
    for key, value in dict_.items():                            # items() - это метод словарей, возвращает итерируемый объект, позволяющий получить пары "ключ-значение" словаря.
        if isinstance(value, list):                             # Проверка функцией isinstance() принадлежности значения "note" классу "list"
            print(f'{key}: {', '.join(value)}')                 # Вывод пары "ключ-значение" словаря "note" с разделением значений символом ', '
        else:
            print(f'{key}: {value}')                            # Вывод пары "ключ-значение" словаря "note" (если значение "note" не принадлежит классу "list")

# Выводим собранные данные
print("\n Собранные данные о заметке: ")
data_output(note)

# Функция по проверке и изменению статуса заметки
def check_note_status():                                        # Проверка и изменение статуса заметки
    sleep(3)
    print(f'\n Текущий статус заметки: ', note["Status"])
    question_status = input('Статус заметки изменился? (Да/Нет): ').capitalize()
    if question_status == 'Да' or question_status == 'Д':

        # Изменение статуса заметки
        done_note_status = "Выполнено"
        in_progress_note_status = "В процессе"
        delay_note_status = "Отложено"
        while True:
            number_of_new_note_status = input(f"\nВыберите цифру или введите новый статус заметки:\n "
                                              f"1. {done_note_status}\n "
                                              f"2. {in_progress_note_status}\n "
                                              f"3. {delay_note_status}\n "
                                              f"Ваш выбор: ").capitalize()
            if number_of_new_note_status == "1" or number_of_new_note_status == "Выполнено":
                print(f"Статус заметки успешно обновлён на: {done_note_status}")
                new_note_status = done_note_status
                break
            elif number_of_new_note_status == "2" or number_of_new_note_status == "В процессе":
                print(f"Статус заметки успешно обновлён на: {in_progress_note_status}")
                new_note_status = in_progress_note_status
                break
            elif number_of_new_note_status == "3" or number_of_new_note_status == "Отложено":
                print(f"Статус заметки успешно обновлён на: {delay_note_status}")
                new_note_status = delay_note_status
                break
            else:
                print("Неправильный ввод. Введите цифру или напишите статус.\n")
                sleep(4)
        note.update({"Status": new_note_status})

        # Выводим обновлённые данные
        sleep(3)
        print("\n Обновлённые данные о заметке: ")
        data_output(note)
    elif question_status == 'Нет' or question_status == 'Н' or question_status == '':        # Отказ от изменения статуса заметки
        # Выводим актуальные данные
        sleep(3)
        print("\n Актуальные данные о заметке: ")
        data_output(note)
    else:                                                       # Выводим сообщение о неправильном вводе
        sleep(2)
        print("\nНеправильный ввод. Введите Да/Нет или оставьте поле пустым.")
        check_note_status()

# Проверка статуса заметки
check_note_status()