from utils.functions import get_operations_list, get_executed_operations, sort_executed_list_per_date, get_first_5_operation, print_executed_operation

operations = get_operations_list("C:/Users\TTe4e\py_project\kursovaya3\src\operations.json")
executed_operations = get_executed_operations(operations)
sort_executed_list = sort_executed_list_per_date(executed_operations)
first_5_operations = get_first_5_operation(sort_executed_list)
print_executed_operation(first_5_operations)
