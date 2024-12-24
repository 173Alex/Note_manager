# Создаём словарь
note = {}
# Запрашиваем информацию у пользователя
note["Имя пользователя"] = input("Введите имя пользователя: ")
note["Описание заметки"] = input("Введите описание заметки: ")
note["Статус заметки"] = input("Введите статус заметки (например - 'Выполнена', 'Не выполнена'): ")
note["Дата создания заметки"] = input("Введите дату создания заметки в формате 'день.месяц.год - ХХ.ХХ.ХХХХ': ")
note["Дата истечения заметки"] = input("Введите дату истечения заметки в формате 'день.месяц.год - ХХ.ХХ.ХХХХ': ")

# Добавляем заголовки в словарь
note ["Заголовки заметок"] = []
for i in range(3):
    title = input(f"Введите заголовок {i + 1} заметки: ")
    note["Заголовки заметок"].append(title)

print()
# Выводим собранные данные
print("\nСобранные данные о заметке: ")
for key, value in note.items():
    print(f"{key.capitalize()}: {value}")