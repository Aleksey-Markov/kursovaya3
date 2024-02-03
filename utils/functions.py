import json
from datetime import datetime


def get_operations_list(file):
    '''
    функция возвращающая список операций
    '''
    with open(file, encoding='utf-8-sig') as file:
        operations_list = json.load(file)
    return operations_list


def get_executed_operations(operations_list):
    '''
    возвращает только успешные операции
    '''
    executed_list = []
    for operation in operations_list:
        if operation.get("state") == "EXECUTED":
            executed_list.append(operation)
    return executed_list


def sort_executed_list_per_date(executed_list):
    '''
    сортирует операции по дате
    '''
    sorted_executed_list = sorted(executed_list, key=lambda x: x.get("date"), reverse=True)
    return sorted_executed_list


def get_first_5_operation(sorted_executed_list):
    '''
    возвращает первые 5 операций
    '''
    sort_list = sorted_executed_list[:5]
    return sort_list


def print_executed_operation(first_5_operation):
    '''
    выводит информацию об операциях в нужном формате
    '''
    for operation in first_5_operation:
        date_str = operation["date"]
        date_format = "%Y-%m-%dT%H:%M:%S.%f"
        date_object = datetime.strptime(date_str, date_format)
        new_date_format = "%d.%m.%Y"
        new_date_str = date_object.strftime(new_date_format)
        operation["date"] = new_date_str

        if operation["description"] == "Перевод организации":
            stars_card = operation["from"][-10:-4]
            operation["from"] = operation["from"].replace(stars_card, '******')
            new_from = ''
            for i, digit in enumerate(operation["from"][-16:]):
                new_from += digit
                if (i+1) % 4 == 0:
                    new_from += ' '
            operation["from"] = operation["from"][:-16] + new_from

        if "Счет" in operation["to"]:
            operation["to"] = operation["to"][:5] + '**' + operation["to"][-4:]

        if operation.get("from") is not None:
            if "Счет" in operation["from"]:
                operation["from"] = operation["from"][:5] + '**' + operation["from"][-4:]

        operations = (f'{operation["date"]} {operation["description"]} \n'
                      f'{operation.get("from")} {operation["to"]} \n'
                      f'{operation["operationAmount"]["amount"]} {operation["operationAmount"]["currency"]["name"]} \n')

        if operation.get("from") is None:
            operations = operations[:28] + operations[33:]

        print(operations)
