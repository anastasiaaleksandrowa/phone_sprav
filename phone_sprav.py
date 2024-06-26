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
# функция для записи данных в файл построчно
def copy_line (sourse_file, target_file):
    sourse_data = read_file (sourse_file)
    target_data = read_file (target_file)
    print (f"исходный файл {sourse_file} содержит:")
    for i, line in enumerate (sourse_data, start=1):
        print (f"строка {i}: {line}")
    Line_num = int (input("введите номер строки для копирования: "))
    if Line_num <= len(sourse_data):
        target_data.append (sourse_data[Line_num - 1])
        write_file (target_file, target_data)
        print (f"строка {Line_num} скопирована в файл {target_file}")
    else:
        print (" неверный номер строки")
    

# консольный интерфейс для ввода и вывода
while True:
    print("1. добавить контакт")
    print("2. обновить контакт")
    print("3. удалить контакт")
    print("4. найти контакт")
    print("5. экспорт телефоного справочника")
    print("6. импорт телефоного справочника")
    print("7. копирование данных из одного файла в другой по номеру строки")
    print("8. выход")
    choice = input (" введите на свой выбор: ")
    if choice == '1':
        last_name = input("введите фамилию: ")
        first_name = input("введите имя: ")
        middle_name = input("введите отчество: ")
        phone_number = input("введите номер: ")
        add_contact(last_name, first_name, middle_name, phone_number)
    elif choice =='2':
        contact_id = int (input(" введите ID для обновления: "))
        last_name = input("введите фамилию: ")
        first_name = input("введите имя: ")
        middle_name = input("введите отчество: ")
        phone_number = input("введите номе: ")
        update_contact(contact_id, last_name, first_name, middle_name, phone_number)
    elif choice == '3':
        contact_id = int (input("введите ID для удаления контакта: "))
        delete_contact(contact_id)
    elif choice == '4':
        search_key = input ("введите имя или фамилию для поиска: ")
        search_contact(search_key)
    elif choice == '5':
        export_file = input ("введите имя файла для экспорта: ") 
        export_phone_book (export_file)
    elif choice == '6':
        import_file = input ("введите имя файла для импорта: ")
        import_phone_book (import_file)
    elif choice == '7':
        if __name__ == "__main__":
            source_file = "sourse.txt"
            target_file = "target.txt"
            copy_line (source_file, target_file)
    elif choice == '8':
        break
    else:
        print("неверный ввод")
 