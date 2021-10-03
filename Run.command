#!/usr/local/bin/python3
from Program import command_dialog
from Program import load_contact_list
from Program import clear_contact_list
# import os

# cwd = os.getcwd()  # Get the current working directory (cwd)
# files = os.listdir(cwd)  # Get all the files in that directory
# print("Files in %r: %s" % (cwd, files))

print("Добро пожаловать в список контактов!")
try:
    load_contact_list()
except FileNotFoundError:
    print("Создан новый contact_list.csv")
    clear_contact_list()
    load_contact_list()

command_dialog()
