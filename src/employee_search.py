# This allows for a list function output for the user to use arrow keys to move up & down menu.
import inquirer

# This allows for coloured text output in the terminal.
import colorama
from colorama import Fore, Back, Style
colorama.init()

# To search for an employee need to import the list of Employee instances.
from employee import employee_list

# Allows the user to return to the main menu.
from return_main_menu import go_back_to_main_menu

# Centres output in terminal.
from print_centre import print_centre


def employee_search():
    """Function to create a way for the user to search for an employee by name in LIST OF EMPLOYEES using arror keys."""
    employee_names = []
    for employee in employee_list:
        employee_names.append(employee.name)
    
    print("\n")
    print_centre(f"{Fore.MAGENTA}LIST OF EMPLOYEES") 
    print("\n")

    questions = [
    inquirer.List(
        "Employees",
        message=f"{Fore.CYAN}Please select an employee from the list using the arrow keys, and then press enter.",
        choices= employee_names + ["Return to Main Menu"],)]
    selection = inquirer.prompt(questions)
    
    # Create list of employee names (employe_names).
    for name in employee_names:
        if selection["Employees"] == name:
            # Search through employee list:
            for employee in employee_list:
                # Check if employee name matches employee list name:
                if name == employee.name:
                    return employee
        if selection["Employees"] == "Return to Main Menu":
            go_back_to_main_menu()

           
            