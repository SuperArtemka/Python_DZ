# Телефонная книга

def Interfeis_contact():
    interfeis_contact = int(input('\n 1 Поиск' '\n 2 Добавление контакта'\
    '\n 3 Вывод всех контактов' '\n 4 Изменение контакта' '\n 5 Удаление контакта'\
     '\n 0 Выход' '\n Выберите действие:'))
    while interfeis_contact != 0:
        if interfeis_contact == 1:
            Find_contact()
        elif interfeis_contact == 2:
            Write_Contact()
        elif interfeis_contact == 4:
            Update_contact()
        elif interfeis_contact == 5:
            Delete_contact()
        else:
            Print_contacts()
        interfeis_contact = int(input('\n 1 Поиск' '\n 2 Добавление контакта'\
    '\n 3 Вывод всех контактов' '\n 4 Изменение контакта' '\n 5 Удаление контакта'\
     '\n 0 Выход' '\n Выберите действие:'))
        
def Write_Contact(telefon_list_name_file = 'Telefon_list.txt'):
    with open(telefon_list_name_file, 'a', encoding='UTF-8') as telefon_list:
        first_name = input("Введите фамилию: ")        
        last_name = input("Введите имя: ")
        telefon = input("Введите телефон: ")
        while len(telefon) != 11 or not telefon.isdigit():
            print('Номер телефона должен состоять из 11-ти цифр. Повторите')
            telefon = input("Введите телефон: ")
        telefon_list.write('\n' + last_name + ' ' +  first_name + ' ' +  telefon + '\n')


def Find_contact(telefon_list_name_file = 'Telefon_list.txt'):
    with open(telefon_list_name_file, 'r', encoding='UTF-8') as telefon_list:
        find_name = input('Поиск: ')
        lines = telefon_list.readlines()
        None_contact = True
        for i in lines:
            if find_name in i:
                print('Контакт найден:', i, end = '')
                None_contact = False
        if None_contact:
            print('Контакт не найден')


def Print_contacts(telefon_list_name_file = 'Telefon_list.txt'):
    with open(telefon_list_name_file, 'r', encoding='UTF-8') as telefon_list:
        lines = telefon_list.readlines()
        for i in lines:
            print(i, end = ' ')

def Update_contact():
    search_name = input('Введите фамилию контакта, который хотите изменить: ')
    with open('Telefon_list.txt', "r", encoding='UTF-8') as telefon_list:
        lines = telefon_list.readlines()
    with open('Telefon_list.txt', "r+", encoding='UTF-8') as telefon_list:
        None_contact = True
        for line in lines:
            contact = line.strip().split(', ')
            if search_name.lower() in contact[0].lower():
                new_second_name = input('Введите новую фамилию: ')
                new_first_name = input('Введите новое имя: ')
                new_phone = input('Введите новый номер телефона: ')
                telefon_list.write(line)
                telefon_list.write(f'{new_second_name}, {new_first_name}, {new_phone}')
                print('Контакт успешно изменен!')                        
                None_contact = False
        if None_contact:
            print('Контакт не найден')

def Delete_contact():
    search_name = input('Введите фамилию контакта, который хотите удалить: ')
    with open('Telefon_list.txt', "r", encoding='UTF-8') as telefon_list:
        lines = telefon_list.readlines()
    with open('Telefon_list.txt', "w", encoding='UTF-8') as telefon_list:
        contact_found = False
        for line in lines:
            contact = line.strip().split(', ')
            if search_name.lower() not in contact[0].lower():
                telefon_list.write(line)
            else:
                contact_found = True
        if contact_found:
            print('Контакт успешно удален!')
        else:
            print('Контакт не найден.')


Interfeis_contact()