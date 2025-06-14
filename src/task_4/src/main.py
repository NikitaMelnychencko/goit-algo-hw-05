from services.NotebookServices import NotebookServices
from services.DataServices import DataServices
from helper.color_loger import log_error

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

welcome_bunner = """
 █████╗ ███████╗███████╗██╗███████╗████████╗ █████╗ ███╗   ██╗████████╗    ██████╗  ██████╗ ████████╗
██╔══██╗██╔════╝██╔════╝██║██╔════╝╚══██╔══╝██╔══██╗████╗  ██║╚══██╔══╝    ██╔══██╗██╔═══██╗╚══██╔══╝
███████║███████╗███████╗██║███████╗   ██║   ███████║██╔██╗ ██║   ██║       ██████╔╝██║   ██║   ██║
██╔══██║╚════██║╚════██║██║╚════██║   ██║   ██╔══██║██║╚██╗██║   ██║       ██╔══██╗██║   ██║   ██║
██║  ██║███████║███████║██║███████║   ██║   ██║  ██║██║ ╚████║   ██║       ██████╔╝╚██████╔╝   ██║
╚═╝  ╚═╝╚══════╝╚══════╝╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝       ╚═════╝  ╚═════╝    ╚═╝

"""

commands = """
  Commands:
  ---------
  1. hello
  2. add <username> <phone>
  3. change <username> <phone>
  4. phone <username>
  5. all
  6. close, exit
  ---------
"""


def main():
    data = DataServices()
    contacts = NotebookServices(data.get_init_data())
    print(welcome_bunner)
    print("Welcome to the assistant bot!")
    print(commands)


    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        match  (command.lower()):
            case "hello":
                print("How can I help you?")
            case "add":
                value = contacts.add_contact(args)
                if value:
                    print(value)
            case "change":
                value = contacts.change_contact(args)
                if value:
                    print(value)
            case "phone":
                value = contacts.get_contact(args[0])
                if value:
                    print(value)
            case "all":
                value = contacts.get_all_contacts()
                if value:
                    print(value)
            case "exit" | "close":
                all_contacts = contacts.get_all_contacts()
                data.save_data(all_contacts)
                print("Good bye!")
                break
            case _:
                log_error("Invalid command.")

if __name__ == "__main__":
    main()
