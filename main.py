from cli_parser import createParser
from data_operations import *



if __name__ != '__main__':
    pass
else:
    parser = createParser()
    namespace = parser.parse_args()

    print(namespace)

    if namespace.command == "add":
        run_save(namespace)
    elif namespace.command == "read_all":
        run_read_all()
    elif namespace.command == "read":
        run_read(namespace)
    elif namespace.command == "update":
        run_update(namespace)
    elif namespace.command == "delete":
        run_delete(namespace)
    elif namespace.command == "filter":
        run_date_filter(namespace)
    else:
        parser.print_help()
