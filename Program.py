import datetime
import csv
import re
from Classes import Contact


contact_list = list()
contact_list_csv = "contact_list.csv"


# Создание нового контакта и запись его в csv файл
def create_contact():
    print("Для того чтобы пропустить пункт и оставить его пустым введите: _")
    new_contact = Contact("", "", "", "", "", "")

    # Ввод имени
    while True:
        try:
            new_contact.first_name = input("Имя: ")
        except ValueError:
            print("Неверный формат имени, присутствуют недопустимые символы")
        else:
            break

    # Ввод фамилии
    while True:
        try:
            new_contact.last_name = input("Фамилия: ")
        except ValueError:
            print("Неверный формат фамилии, присутствуют недопустимые символы")
        else:
            break

    # Ввод даты рождения
    while True:
        try:
            new_contact.birth_date = datetime.datetime \
                .strptime(input("Дата рождения в формате ДД.ММ.ГГГГ: "), "%d.%m.%Y").date()
        except ValueError:
            print("Неверный формат даты или дата не может быть позднее текущего дня")
        else:
            break

    # Ввод наименования компании
    new_contact.company_name = input("Компания: ")

    # Ввод E-Mail
    while True:
        try:
            new_contact.email = input("E-Mail: ")
        except ValueError:
            print("Неверный формат E-Mail")
        else:
            break

    # Ввод номера телефона
    while True:
        try:
            new_contact.phone_number = input("Номер телефона в формате +7(___)___-__-__: ")
        except ValueError:
            print("Неверный формат номера")
        else:
            break

    contact_list.append(new_contact)

    # Создание словаря из контакта
    contact_dict = {"first name": new_contact.first_name, "last name": new_contact.last_name,
                    "birth date": new_contact.birth_date, "company name": new_contact.company_name,
                    "email": new_contact.email, "phone number": new_contact.phone_number}

    # Добавление записи в csv
    with open(contact_list_csv, "a", newline="") as file:
        columns = ["first name", "last name", "birth date", "company name", "email", "phone number"]
        data_writer = csv.DictWriter(file, fieldnames=columns)
        # writer.writeheader()
        data_writer.writerow(contact_dict)


# Загрузка списка контактов из csv
def load_contact_list():
    with open(contact_list_csv) as file:
        data_reader = csv.DictReader(file)
        for line in data_reader:
            contact_list.append(Contact(line["first name"], line["last name"],
                                        line["birth date"], line["company name"],
                                        line["email"], line["phone number"]))


# Отображение списка контактов
def show_contact_list():
    for contact in contact_list:
        print(contact)


# Поиск по имени
def find_by_first_name(name):
    regex = r"(?i)\b{}".format(name)
    counter = 0
    for contact in contact_list:
        if re.search(regex, contact.first_name):
            print(contact)
            counter += 1
    print("Найдено: {}".format(counter))


# Поиск по фамилии
def find_by_last_name(name):
    regex = r"(?i)\b{}".format(name)
    counter = 0
    for contact in contact_list:
        if re.search(regex, contact.last_name):
            print(contact)
            counter += 1
    print("Найдено: {}".format(counter))


# Полная очистка списка контактов/восстановление contact_list.csv
def clear_contact_list():
    with open(contact_list_csv, "w", newline="") as file:
        columns = ["first name", "last name", "birth date", "company name", "email", "phone number"]
        data_writer = csv.DictWriter(file, fieldnames=columns)
        data_writer.writeheader()
    contact_list.clear()
    print("Файл contact_list.csv был сброшен, список контактов очищен.")


# Вызов команд для работы со списком контактов
def command_dialog():
    print("help - для вызова справки")
    while True:
        command = input(">>> ")

        if command == "show":
            show_contact_list()
        if command == "create":
            create_contact()
        if command == "find_fn":
            find_by_first_name(input("Искать по имени:"))
        if command == "find_ln":
            find_by_last_name(input("Искать по фамилии:"))
        if command == "clear":
            clear_contact_list()
        if command == "quit":
            break
        if command == "help":
            print("Список команд:\nshow - показать список контактов\ncreate - добавить контакт\n"
                  "find_fn - поиск по имени\nfind_ln - поиск по фамилии\nclear - полная очистка списка контактов\n"
                  "quit - выйти из программы\nhelp - справка")



