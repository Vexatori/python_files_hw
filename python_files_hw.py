def input_name():
  return input("Enter name: ")

def input_surname():
  return input("Enter surname: ")

def input_patronumic():
  return input("Enter patronumic: ")

def input_phone():
  return input("Enter phone: ")

def input_address():
  return input("Enter address: ")

def create_contact():
  return f"{input_surname()} {input_name()} {input_patronumic()} {input_phone()} {input_address()}\n"

def add_contact():
  new_contact = create_contact()
  with open("phone_dict.txt", "a", encoding="UTF-8") as file_data:
    file_data.write(new_contact)
  print()

def print_phonebook():
  with open("phone_dict.txt", "r", encoding="UTF-8") as file_data:
    print(file_data.read())

def search_contact():
  searchable_text = str(input("Enter searchable text: ")).lower()

  print(
    "Search possible variants:\n"
    "1. Surname\n"
    "2. Name\n"
    "3. Patronumic\n"
    "4. Phone\n"
    "5. Address\n"
  )
  search_variant = input("Enter your search choice: ")
  while search_variant not in ['1', '2', '3', '4', '5']:
    print("There is no variant you chosen, please try again")
    search_variant = input("Enter your search choice: ")
  search_variant = int(search_variant)

  with open("phone_dict.txt", "r", encoding="UTF-8") as file_data:
    contacts_str = file_data.read()
    contacts_list = [contact for contact in contacts_str.split("\n") if contact != '']
  # matched_contacts = list(filter(lambda str: searchable_text in str.lower(), contacts_list))
  for contact in contacts_list:
    contact_values = contact.split()
    # if searchable_text in contact.lower():
    #   print(contact)
    if searchable_text in contact_values[search_variant - 1].lower():
      print(contact)

def copy_all_file_data():
  pass

def copy_file_line():
  pass

def ui():
  with open("phone_dict.txt", "a", encoding="UTF-8"):
    pass

  user_choice = 0
  while user_choice != 4:
    print(
      "Menu:\n"
      "1. Add new contact\n"
      "2. Print all data\n"
      "3. Search contact\n"
      "4. Copy all data to file\n"
      "5. Copy line to file\n"
      "6. Exit\n"
    )
    user_choice = input("Enter action: ")
    while user_choice not in ['1', '2', '3', '4', '5', '6']:
      print("There is no such value in the menu, please try again")
      user_choice = input("Enter action: ")

    user_choice = int(user_choice)
    match user_choice:
      case 1:
        add_contact()
      case 2:
        print_phonebook()
      case 3:
        search_contact()
      case 4:
        copy_all_file_data()
      case 5:
        copy_file_line()
      case 6:
        print("Closing program...")

ui()