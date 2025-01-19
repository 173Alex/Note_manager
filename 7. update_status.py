from time import sleep              # Добавление библиотеки по задержке времени
note = {}                           # Создаём словарь

# Запрашиваем информацию у пользователя и добавляем её в словарь
note["Имя пользователя:"] = input("Введите имя пользователя: ").capitalize()
note["Описание заметки:"] = input("Введите описание заметки: ").capitalize()
note["Статус заметки:"] = input("Введите статус заметки (например - 'Выполнено', 'В процессе', 'Отложено'): ").capitalize()
create_date = input("Введите дату создания заметки в формате 'день.месяц.год - ХХ.ХХ.ХХХХ': ")
correct_create_date = create_date[:5]                                                              # Представление корректного отображения даты создания заметки формата 'ДД.ММ - XX.XX'
note["Дата создания заметки:"] = correct_create_date
issue_date = input("Введите дату истечения заметки в формате 'день.месяц.год - ХХ.ХХ.ХХХХ': ")
correct_issue_date = issue_date[:5]                                                                # Представление корректного отображения даты истечения заметки 'ДД.ММ - XX.XX'
note["Дата истечения заметки:"] = correct_issue_date

# Добавляем заголовки в словарь
note["Заголовки заметки:"] = []
for i in range(100):                                                                                # Условно выбрано количество заметок 100 штук
    title = input(f"Введите заголовок {i + 1} заметки (для завершения ввода - кликните клавишу 'Enter'): ").capitalize()
    if title == '':                                                                                 # Условие для завершения ввода от пользователя
        break                                                                                       # Окончание цикла после пустого ввода
    if title in note["Заголовки заметки:"]:                                                         # Проверка уникальности введённого заголовка
        print(" Введённый заголовок уже имеется в списке. Укажите другой заголовок.\n")             # Не решена проблема с продолжением счёта аргумента "i" при повторном вводе заголовка
        sleep(4)
    else:
        note["Заголовки заметки:"].append(title)                                                    # Добавление заголовка в словарь методом ".append"
    print(" Введённые заголовки заметки: ")                                                         # Вывод на экран всех введённых заголовков заметок сразу после ввода от пользователя
    for values_ in note["Заголовки заметки:"]:                                                      # Цикл для перебора значений словаря по ключу для построчного вывода "list"
        print(f'- {values_}')
    print()

# Функция по выводу данных
def data_output():                                              # Вывод данных
    for key, value in note.items():                             # items() - это метод словарей, возвращает итерируемый объект (особый DictView объект), позволяющий получить пары "ключ-значение" словаря.
        print(key, value)                                       # Вывод каждой пары "ключ-значение" словаря "note"
        # print(key, *value)                                    # Попытка №1 вывода списка в более "красивом" виде - неудачно
        # print(key, *value, sep=', ')                          # Попытка №2 вывода списка в более "красивом" виде - неудачно

# Выводим собранные данные
print("\n Собранные данные о заметке: ")
data_output()

# Функция по проверке и изменению статуса заметки
def check_note_status():                                        # Проверка и изменение статуса заметки
    sleep(3)
    print(f'\n Текущий статус заметки: ', note["Статус заметки:"])
    question_status = input('Статус заметки изменился? (Да/Нет): ').capitalize()
    if question_status == 'Да':

        # Изменение статуса заметки
        done_note_status = "Выполнено"
        in_progress_note_status = "В процессе"
        delay_note_status = "Отложено"
        while True:
            number_of_new_note_status = input(f"Выберите новый статус заметки:\n "
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
                print("Неправильный ввод. Введите цифру и  только из трёх вариантов: 1, 2, 3\n")
                sleep(4)
        note.update({"Статус заметки:": new_note_status})

        # Выводим обновлённые данные
        sleep(3)
        print("\n Обновлённые данные о заметке: ")
        data_output()
    else:
        # Выводим актуальные данные
        sleep(3)
        print("\n Актуальные данные о заметке: ")
        data_output()

# Проверка статуса заметки
check_note_status()