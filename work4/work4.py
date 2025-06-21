def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    if len(args) > 1:
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    else:
        return "Missing arguments."

def change_contact(args, contacts):
    if len(args) > 1:
        name, phone = args
        contacts[name] = phone
        return "Contact changed."
    else:
        return "Missing arguments."

def show_phone(args, contacts):
    if args:
        name = args[0]
        if contacts.get(name):
            return f"{name}: {contacts.get(name)}"
        else:
            return "Contact missing."
    else:
        return "Missing arguments."
    
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        if user_input:
            command, *args = parse_input(user_input)
        else:
            command = None

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
            if contacts:
                print(contacts)
            else:
                print("List is empty.")
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()