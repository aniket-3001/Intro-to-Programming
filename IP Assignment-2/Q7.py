import json


def read_from_file(file_name):  # read the existing address book from given file

    try:
        with open(file_name, 'r') as f:
            return json.load(f)
    except:  # in case we run the program for the first time and addrbook.txt does not exist
        return {}


def write_in_file(file_name):  # write the current dictionary in a file
    with open(file_name, 'w') as f:
        return json.dump(address_book, f, indent=4, sort_keys=True)


def add_entry(name, address, phone, email):  # add new entry into the address book
    global address_book

    if name in address_book:
        address_book[name].append(
            {"address": address, "phone": phone, "email": email})

    else:
        address_book[name] = [
            {"address": address, "phone": phone, "email": email}]

    print("Entry added successfully")


def del_entry(name):  # delete an entry from the address book
    global address_book

    if name not in address_book:
        print("No entry found with the given name")

    elif len(address_book[name]) > 1:
        print("Multiple entries found with the given name. Please provide the following details of the entry you would like to delete:")
        print()
        address = input("Enter Address: ")
        phone = input("Enter Phone No.: ")
        email = input("Enter Email: ")
        print()
        for index, entry in enumerate(address_book[name]):
            if entry["address"] == address and entry["phone"] == phone and entry["email"] == email:
                del address_book[name][index]
                print("Entry deleted successfully")
                return
        print("No entry matching_entries with the given details")

    else:
        del address_book[name]
        print("Entry deleted successfully")


# find matching entries in the address book given a partial name
def find_partial_name(str):
    global address_book
    matching_entries = {}

    for name in address_book:
        if str in name:  # condition to check for partial name
            matching_entries[name] = address_book[name]

    if len(matching_entries) != 0:
        print(f"matching entries: {matching_entries}")
    else:
        print("No matching entries found")


def find_entry(var):  # find a particular entry by providing phone no. or email (var)
    global address_book
    for name, list in address_book.items():
        if len(list) > 1:
            for c in list:
                if var in c.values():
                    d = {name: c}
                    print("The entry is:", d)
                    return
        else:
            if var in (list[0]).values():
                d = {name: list[0]}
                print("The entry is:", d)
                return
    print("No entry found having the given phone no./email id")


# merge friend's address book with yours and return your modified address book i.e address_book
def merge_address_books(friend_book):
    global address_book
    for name in friend_book:
        if name in address_book:
            address_book[name].extend(friend_book[name])
        else:
            address_book[name] = friend_book[name]
    print("Your friend's address book has been merged into your address book")


address_book = read_from_file("IP Assignment-2/addrbook.txt")

print("Welcome to your Address Book")
print("Please select one of the below options to perform an operation on your address book:")
print()
print("1: Add an entry")
print("2: Delete an entry")
print("3: Find all matching entries by providing a partial name")
print("4: Find a specific entry by giving a phone number or email")
print("5. Merge friend's address book with yours")
print("6: Exit")
print()

# set the menu
while True:
    choice = input("enter choice: ")
    print()

    if choice == '1':
        name = input("Enter name: ")
        address = input("Enter address: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        print()
        add_entry(name, address, phone, email)

    elif choice == '2':
        name = input("Enter name of the person whose entry you want deleted: ")
        print()
        del_entry(name)
        print()

    elif choice == '3':
        name = input(
            "Enter the partial name of the persons you want to find: ")
        print()
        find_partial_name(name)
        print()

    elif choice == '4':
        var = input(
            "Enter phone number or email of the person you want to find: ")
        print()
        find_entry(var)
        print()

    elif choice == '5':
        dict = read_from_file("IP Assignment-2/ankur's_address_book.json")
        merge_address_books(dict)
        print()

    elif choice == '6':
        address_book = write_in_file("IP Assignment-2/addrbook.txt")
        print("Exit successful. Thank you!.")
        break

    else:
        print("The option you have selected does not exist. Please try again.")
        print()
