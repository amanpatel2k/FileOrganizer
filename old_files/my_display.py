from prettytable import PrettyTable

def mydisplay(data_list):
    if not isinstance(data_list, list):
        raise TypeError("Input must be a list")

    if not data_list:
        print("List is empty.")
        return

    table = PrettyTable()
    table.field_names = ["#", "Absolute Path"]

    for index, item in enumerate(data_list, start=1):
        table.add_row([index, item])
    
    print(table)
