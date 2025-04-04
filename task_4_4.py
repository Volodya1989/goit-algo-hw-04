def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    if len(args) < 2:
        return "Invalid command. Usage: add name phone"
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    if len(args) < 2:
        return "Invalid command. Usage: change username phone"
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return 'Contact updated.'
    else:
        return f'Contact {name} was not found.'


def show_phone(args, contacts):
    if len(args) != 1:
        return "Invalid command. Usage: phone username."
    name = args[0]
    if name in contacts:
        return f"Phone number for {name}: {contacts[name]}"
    else:
        return f"Error: Contact {name} not found."


def show_all(contacts):
    if not contacts:
        return "No contacts found."
    result = "\n".join(
        [f"{name}: {phone}" for name, phone in contacts.items()])
    return result


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_phone(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
