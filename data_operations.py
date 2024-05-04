import datetime

file_name = 'data.csv'
file_encoding = 'utf-8'

def run_save(namespace):
    """Выполнение команды сохранения заметки"""
    print("Выполнение команды сохранения заметки")
    with open(file_name, 'a', encoding=file_encoding) as file:
        file.write(f'{id(namespace.title)};{namespace.title};{namespace.msg};{datetime.datetime.utcnow()}\n')

def run_read_all():
    print("Выполнение команды вывода списка заметок")
    with open(file_name, 'r', encoding=file_encoding) as file:
        data = file.readlines()
        print(''.join(data))

def run_read(namespace):
    print("Выполнение команды вывода заметки по id")
    with open(f'{file_name}', 'r') as file:
        filedata = file.read()

    for line in filedata.split('\n'):
        if line.startswith(namespace.id):
            print(line)


def run_update(namespace):
    print("Выполнение команды обновления заметки по id")
    with open(f'{file_name}', 'r') as file:
        filedata = file.read()

    data = ''
    for line in filedata.split('\n'):
        if line.startswith(namespace.id):
            data += filedata.replace(f'{line}', f'{namespace.id};{namespace.title};{namespace.msg};{datetime.datetime.utcnow()}')

    if data == '':
        return

    with open(f'{file_name}', 'w') as file:
        file.write(data)

def run_delete(namespace):
    print("Выполнение команды удаления заметки по id")
    with open(f'{file_name}', 'r') as file:
        filedata = file.read()

    data = ''
    for line in filedata.split('\n'):
        if not line.startswith(namespace.id):
            data += f'{line}\n'

    if data == '':
        return

    with open(f'{file_name}', 'w') as file:
        file.write(data)

def run_date_filter(namespace):
    print("Выполнение команды фильтрации заметки по дате")
    with open(f'{file_name}', 'r') as file:
        filedata = file.read()

    data = ''
    for line in filedata.split('\n'):
        if line.__contains__(namespace.date):
            data += f'{line}\n'

    print(data)