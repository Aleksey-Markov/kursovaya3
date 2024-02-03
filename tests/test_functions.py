import pytest
from utils.functions import get_operations_list, get_executed_operations, sort_executed_list_per_date, get_first_5_operation, print_executed_operation
from src.main import operations, executed_operations, sort_executed_list, first_5_operations, print_executed_operation


@pytest.fixture
def coll():
    return "C:/Users\TTe4e\py_project\kursovaya3\src\operations.json"


def test_get_operations_list(coll):
    assert get_operations_list(coll) == get_operations_list("C:/Users\TTe4e\py_project\kursovaya3\src\operations.json")


def test_sort_executed_list_per_date():
    assert sort_executed_list_per_date(executed_operations) == sorted(sort_executed_list, key=lambda x: x.get("date"), reverse=True)


def test_get_executed_operations():
    assert get_executed_operations(operations) == executed_operations


def test_get_first_5_operation():
    assert get_first_5_operation(sort_executed_list) == first_5_operations
