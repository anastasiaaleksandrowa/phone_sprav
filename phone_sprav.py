#функция для добавления, измения и удаления контакта
phone_book = {}
def add_contact (last_name, first_name, middle_name, phone_number):
    contact_id = len(phone_book)+1
    phone_book[contact_id]={'last_name': last_name, 'first_name': first_name, 'middle_name': middle_name, 'phone_number': phone_number}
def update_contact (contact_id, last_name, first_name, middle_name, phone_number):
    if contact_id in phone_book:
        phone_book[contact_id]= {'last_name': last_name, 'first_name': first_name, 'middle_name': middle_name, 'phone_number': phone_number}
    else:
        print("контакт не найден")
def delete_contact(contact_id):
    if contact_id in phone_book:
        del phone_book[contact_id]
    else:
         print("контакт не найден")

# функция поиска контакта по имени 
def search_contact(search_key):
    for contact_id, contact_info in phone_book.items():
        if search_key.lower() in contact_info ['last_name'].lower() or search_key.lower() in contact_info ['first_name'].lower():
            print (f"ID: {contact_id}")
            print (f"Фамилия: {contact_info['last_name']}")
            print (f"имя: {contact_info['first_name']}")
            print (f"отчество: {contact_info['middle_name']}")
            print (f"номер телефона: {contact_info['phone_number']}")

# функция для сохранения данных в текстовом файле с возможностью импорта 
def export_phone_book (filename):
    with open(filename, 'w') as file:
        for contact_id, contact_info in phone_book.items ():
            file.write (f"{contact_id}, {contact_info['last_name']}, {contact_info['first_name']}, {contact_info['middle_name']}, {contact_info['phone_number']}n")
def import_phone_book (filename):
    with open (filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            contact_id, last_name, first_name, middle_name, phone_number = line.strip().split(',')
            phone_book [int (contact_id)] = {'last_name': last_name, 'first_name': first_name, 'middle_name': middle_name, 'phone_number': phone_number}

# блок для копирования данных из одного файла в другой через ввод пользователем номера строки
# функция для хранения строк из файла
def read_file(filename):
    data = []
    with open(filename, 'r') as file:
        for line in file:
            data.append(line.strip())
    return data
# функция для чтения данных из файла по строчно
def write_file (filename,data):
    with open (filename, 'w') as file:
        for line in data:
            file.write(line + 'n')
