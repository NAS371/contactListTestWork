import datetime
import re


class Contact:

    def __init__(self, first_name, last_name, birth_date, company_name, email, phone_number):
        self.__first_name = str(first_name)
        self.__last_name = str(last_name)
        self.__birth_date = birth_date
        self.__company_name = str(company_name)
        self.__email = str(email)
        self.__phone_number = str(phone_number)

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name):
        if first_name == "_":
            self.__first_name = ""
        elif not re.fullmatch(r"\b[A-ZА-Яa-zа-я'-]+\b", first_name):
            raise ValueError("Присутствуют недопустимые символы для имени")
        else:
            self.__first_name = first_name

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name):
        if last_name == "_":
            self.__last_name = ""
        elif not re.fullmatch(r"\b[A-ZА-Яa-zа-я'-]+\b", last_name):
            raise ValueError("Присутствуют недопустимые символы для фамилии")
        else:
            self.__last_name = last_name

    @property
    def birth_date(self):
        return self.__birth_date

    @birth_date.setter
    def birth_date(self, birth_date):
        if birth_date <= datetime.date.today():
            self.__birth_date = birth_date
        else:
            raise ValueError("Дата рождения не может быть позже текущего дня")

    @property
    def company_name(self):
        return self.__company_name

    @company_name.setter
    def company_name(self, company_name):
        if company_name == "_":
            self.__company_name = ""
        else:
            self.__company_name = company_name

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        if email == "_":
            self.__email = ""
        elif not re.fullmatch(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", email):
            raise ValueError("Некорректный E-Mail")
        else:
            self.__email = email

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        if phone_number == "_":
            self.__phone_number = ""
        elif not re.fullmatch(r"\+7\(\w{3}\)\w{3}-\w{2}-\w{2}", phone_number):
            raise ValueError("Некорректный номер телефона")
        else:
            self.__phone_number = phone_number

    def __str__(self):
        return " Имя: {} \t Фамилия: {} \n День рождения: {} \t Компания: {} \n E-Mail: {} \t Номер телефона: {} \n" \
               "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"\
            .format(self.__first_name, self.__last_name, self.__birth_date
                    , self.__company_name, self.__email, self.__phone_number)




