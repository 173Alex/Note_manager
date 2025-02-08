from time import sleep                          # Добавление библиотеки по задержке времени
from datetime import datetime                   # Модуль предоставляет классы для обработки времени и даты разными способами

note = {}                                       # Создаём словарь

date_name = ''
date_format = ''
# Функция Форматирования даты заметки
def format_date(variant=0):
    global date_name, date_format
    date_formats = [{'дд-мм-гггг': '%d-%m-%Y'}, {"гггг-мм-дд": "%Y-%m-%d"}]               # Словарь отображающий необходимый формат даты
    date_name, date_format = date_formats[variant].popitem()
    return date_name, date_format
# Функция Добавления текущей даты заметки в словарь
def add_current_date():
    now = datetime.now()                                                # Текущая дата/время (<class 'datetime.datetime'>)
    current_date = now.date()                                           # Текущая дата в формате 'гггг-мм-дд' (<class 'datetime.date'>)
    date_name, date_format = format_date()
    current_date_format_str = current_date.strftime(date_format)        # Представление текущей даты в формате 'дд-мм-гггг' (<class 'str'>)
    note["Create_date"] = current_date_format_str                       # Добавление в словарь текущей даты в формате 'дд-мм-гггг'
    print(f"Текущая дата: {current_date_format_str}")                   # Вывод текущей даты в консоль
    return current_date
# Добавляем дату истечения заметки в словарь
def check_issue_date_input():
    while True:
        issue_date_format_str = input(f"Введите срок истечения заметки (в формате {date_name}): ")
        # print(type(issue_date_format_str), issue_date_format_str)
        try:
            issue_date = datetime.strptime(issue_date_format_str, date_format).date()
            issue_date_format_str = issue_date.strftime(date_format)
            break
        except ValueError:
            print("Неверный формат даты. Убедитесь, что вводите дату в формате день-месяц-год, например: 31-12-2025.\n")
            sleep(2)
    note["Issue_date"] = issue_date_format_str
    return issue_date

# Перебор склонений день/дня/дней (plural russian days)
def plural_days(deadline):
    days = ['день', 'дня', 'дней']
    if deadline % 10 == 1 and deadline % 100 != 11:
        return days[0]
    elif 2 <= deadline % 10 <= 4 and (deadline % 100 < 10 or deadline % 100 >= 20):
        return days[1]
    return days[2]
# Функция Сравнение даты дедлайна заметки с текущей датой
def comparison_dates():
    print()
    # current_date_calc = add_current_date()  # Создаём переменную - текущая дата заметки для вычислений
    # issue_date_calc = check_issue_date_input()  # Создаём переменную - дата истечения срока заметки для вычислений
    deadline = current_date_calc - issue_date_calc
    if deadline.days == 0:
        print("Внимание! Если задание заметки ещё не выполнено, то срок выполнения истекает сегодня.")
    elif deadline.days > 0:
        print(f"Внимание! Срок выполнения задания заметки истёк {deadline.days} {plural_days(deadline.days)} назад!")
    elif deadline.days < 0:
        positive_deadline = deadline.days * -1
        print(f"До окончания срока выполнения задания заметки - {positive_deadline} {plural_days(positive_deadline)}!")
    sleep(4)

# Проверка даты дедлайна
current_date_calc = add_current_date()                                  # Создаём переменную - текущая дата заметки для вычислений
issue_date_calc = check_issue_date_input()                              # Создаём переменную - дата истечения срока заметки для вычислений
comparison_dates()

# Функция Вывода данных
def data_output(dict_):                                         # Вывод данных
    for key, value in dict_.items():                            # items() - это метод словарей, возвращает итерируемый объект, позволяющий получить пары "ключ-значение" словаря.
        if isinstance(value, list):                             # Проверка функцией isinstance() принадлежности значения "note" классу "list"
            print(f'{key}: {', '.join(value)}')                 # Вывод пары "ключ-значение" словаря "note" с разделением значений символом ', '
        else:
            print(f'{key}: {value}')                            # Вывод пары "ключ-значение" словаря "note" (если значение "note" не принадлежит классу "list")

# Выводим собранные данные
print("\n Собранные данные о заметке: ")
data_output(note)