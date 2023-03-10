# This allows for coloured text output in the terminal
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

# This allows for shell commands in the terminal.
import os

# Import file for function employee_search to run.
from employee_search import employee_search

# Import file for function list_employees to run.
from list_employee import list_employee


def list_one_employee():
    """Function to list one employee's attributes from database."""
    employee = employee_search()
    os.system('clear')
    if employee:
        print(f"{Fore.MAGENTA}{Style.BRIGHT}\nEmployee listed:\n")
        list_employee(employee)
        list_one_employee()

        