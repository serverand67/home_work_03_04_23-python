"""
Создать телефонный справочник. 
Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в
текстовом файле
3. Пользователь может ввести одну из
характеристик для поиска определенной
записи(Например имя или фамилию
человека)
4. Возможность импорта и экспорта данных в
формате .txt.
5. Возможность изменения данных
6. Возможность удаления данных
"""
import re

# функция записи данных в телефонную книгу
def recording_person_data():           
    surname = input("Фамилия: ").title()
    name = input("Имя: ").title()
    middle_name = input("Отчество: ").title()
    phone_number = input("Телефон: ").title()
    data = open("phonebook.txt", "a", encoding="utf-8")
    data.writelines(f"Фамилия: {surname} Имя: {name} Отчество: {middle_name} Телефон: {phone_number}\n")
    data.close()

# функция поиска записи в телефонной книге
def search():     
    looking_for = input("Введите данные для поиска: ").title()
    with open("phonebook.txt", "r", encoding="utf-8") as data:
        for line in data:
            if looking_for in line:
                print(line)
            
# функция печать (вывода) телефонной книги на экран
def print_phonebook():       
    with open("phonebook.txt", "r", encoding="utf-8") as data:
        for line in data:
            print(line)

# функция импортф из другого (указанного) файла
def import_data():     
    imp_phonebook = input("Введите ссылку: ")
    with open(imp_phonebook, "r", encoding="utf-8") as data:
        with open("phonebook.txt", "a+", encoding="utf-8") as data_1:
            for line in data:
                if line not in data_1.readlines():
                    data_1.write(line)
            data_1.write("\n")
        print("Данные импортированны успешно.")

# функция экспорта в другой (указанный) файл
def export_data():      
    exp_phonebook = input("Введите ссылку: ")
    with open("phonebook.txt", "r", encoding="utf-8") as data_1:
        with open(exp_phonebook, "a+", encoding="utf-8") as data:
            for line in data_1:
                if line not in data.readlines():
                    data.write(line)
            data.write("\n")
        print("Данные экспортированны успешно.")

# функция изменений данных записи в телефонной книге
def chenge_text_in_line():
    with open("phonebook.txt", "r+", encoding="utf-8") as data:
        text = data.read()
        old_text = input("введите данные, которые хотите изменить: ").title()
        new_text = input("введите новые данные: ").title()
        text = text.replace(old_text, new_text)
        data.seek(0)      # метод seek(0) используется для перехода на самый первый символ
        data.write(text)  # записывает измененные данные в фйл
        data.truncate()   # очищает
        print("Данные изменены успешно.")

# 1-й вариант - функция удаления записи в телефонной книге
# перезаписывает файл, за исключением записи
# с указанными данными 

def delete_line():   # 
    line_to_delete = input("Введите данные для удаления: ").title()
    # Открываем файл на чтение и считываем все его строки в список
    with open("phonebook.txt", "r+", encoding="utf-8") as data:
        lines = data.readlines()       # записываем текст в переменную 

    # Открываем файл на запись и перезаписываем все строки кроме заданной
    with open("phonebook.txt", "w", encoding="utf-8") as data_1:        
        for line in lines:
            # if line.strip('\n') != line_to_delete:
            if line_to_delete not in line:
                data_1.write(line)
        print("Данные удалены успешно.")

# 2-й вариант - функция удаления записи в телефонной книге
# перезаписывает файл, за исключением записи
# с указанными данными 

# def delete_line():
        # Открываем файл на чтение и считываем все его строки в список
#     with open("phonebook.txt", "r+", encoding="utf-8") as data:
#         lines = data.readlines()      # записываем текст в переменную
#         line_to_delete = input("Введите данные для удаления: ").title()
#         pattern = re.compile(re.escape(line_to_delete))

  # Открываем файл на запись и перезаписываем все строки кроме заданной
#     with open("phonebook.txt", "w", encoding="utf-8") as data_1:
#         for line in lines:
#             result = pattern.search(line)
#             if result is None:
#                 data_1.write(line)

                    
#  Вывод меню на экран
                        
print("""Меню:
1 - добавление записи 
2 - Поиск 
3 - Вывод на экран 
4 - Импорт в файл
5 - Экспорт в файл 
6 - Внести изменения в запись
7 - Удалить запись
8 - Выход
""")

action = int(input("Выберите действия: "))    # указать действие цифрой

if action == 1:
    recording_person_data()
elif action == 2:
    search()
elif action == 3:
    print_phonebook()
elif action == 4:
    import_data()
elif action == 5:
    export_data()
elif action == 6:
    chenge_text_in_line()
elif action == 7:
    delete_line()
else:
    print("""
Нет такой команды.
Попробуйте еще раз.
""")


# recording_person_data()   # запись данных
# search()                  # поиск данных
# print_phonebook()         # вывод данных на экран
# import_data()             # ссылку на файл из которого копируем
# export_data()             # ссылку на файл в который копируем
# chenge_text_in_line()     # изменения данных в записи
# delete_line()             # удаление конкретной записи
