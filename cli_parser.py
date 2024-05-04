import sys
import argparse

version = "0.1.0"

def createParser():
    parser = argparse.ArgumentParser(
        prog='notion',
        description='''Консольная программа для работы с заметками.''',
        epilog='''(c) Май 2024. Автор программы, как всегда, не несет никакой ответственности ни за что.''',
        add_help=False
    )
    parent_group = parser.add_argument_group(title='Параметры')
    parent_group.add_argument('--help', '-h', action='help', help='Справка')
    parent_group.add_argument('--version', '-v',
                              action='version',
                              help='Номер версии',
                              version='%(prog)s {}'.format(version))

    subparser = parser.add_subparsers(
        dest='command',
        title='Команды',
        description='Команды, которые должны быть переданы в качестве первого параметра программе %(prog)s'
    )

    save_parser = subparser.add_parser(
        'add',
        help='Добавить заметку',
        add_help=False
    )

    read_all_parser = subparser.add_parser(
        'read_all',
        help='Вывести список заметок',
        add_help=False
    )

    read_parser = subparser.add_parser(
        'read',
        help='Вывести заметку по id',
        add_help=False
    )

    update_parser = subparser.add_parser(
        'update',
        help='Обновить заметку по id',
        add_help=False
    )

    delete_parser = subparser.add_parser(
        'delete',
        help='Удалить заметку по id',
        add_help=False
    )

    date_filter = subparser.add_parser(
        'filter',
        help='Отфильтровать по дате',
        add_help=False
    )

    save_group = save_parser.add_argument_group(title='Параметры команды add')
    save_group.add_argument('--help', '-h', action='help', help='Справка')

    read_all_group = read_all_parser.add_argument_group(title='Параметры команды read_all')
    read_all_group.add_argument('--help', '-h', action='help', help='Справка')

    read_group = read_parser.add_argument_group(title='Параметры команды read')
    read_group.add_argument('--help', '-h', action='help', help='Справка')

    update_group = update_parser.add_argument_group(title='Параметры команды update')
    update_group.add_argument('--help', '-h', action='help', help='Справка')

    delete_group = delete_parser.add_argument_group(title='Параметры команды delete')
    delete_group.add_argument('--help', '-h', action='help', help='Справка')

    date_filter_group = date_filter.add_argument_group(title='Параметры команды фильтрации по дате')
    date_filter_group.add_argument('--help', '-h', action='help', help='Справка')

    save_group.add_argument(
        '--title',
        required=True,
        help='Название заметки',
        metavar='ИМЯ'
    )
    save_group.add_argument(
        '--msg',
        help='Тело заметки',
        metavar='СООБЩЕНИЕ'
    )

    read_group.add_argument(
        '--id',
        required=True,
        help='Id заметки',
        metavar='ID'
    )

    update_group.add_argument(
        '--id',
        required=True,
        help='Id заметки',
        metavar='ID'
    )
    update_group.add_argument(
        '--title',
        required=True,
        help='Название заметки',
        metavar='ИМЯ'
    )
    update_group.add_argument(
        '--msg',
        help='Тело заметки',
        metavar='СООБЩЕНИЕ'
    )

    delete_group.add_argument(
        '--id',
        required=True,
        help='Id заметки',
        metavar='ID'
    )

    date_filter_group.add_argument(
        '--date',
        required=True,
        help='Дата в формате utc. Шаблон гггг-мм-дд',
        metavar='Дата'
    )
    return parser