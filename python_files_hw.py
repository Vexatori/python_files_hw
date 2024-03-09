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
  for contact in contacts_list:
    contact_values = contact.split()
    if searchable_text in contact_values[search_variant - 1].lower():
      print(contact)

def copy_all_file_data():
  file_copy_path = input("Enter file name: ")
  source_file = open("phone_dict.txt", "r", encoding="UTF-8")
  copy_file = open(file_copy_path, 'a', encoding="UTF-8")
  for line in source_file:
    copy_file.write(line)
  source_file.close()
  copy_file.close()

def copy_file_line():
  source_file = open("phone_dict.txt", "r", encoding="UTF-8")
  contacts_str = source_file.read()
  contacts_arr = [contact for contact in contacts_str.split("\n") if contact != '']
  source_file.close()

  line_copy_number = input("Enter the number of line in the source file to copy: ")
  phonebook_len = len(contacts_arr)
  while line_copy_number not in [str(i) for i in range(1, phonebook_len + 1)]:
    print(f"There are only {phonebook_len} lines in phonebook, please try again")
    line_copy_number = input("Enter the number of line to copy: ")

  line_copy_number = int(line_copy_number)
  file_copy_path = input("Enter file name: ")
  with open(file_copy_path, 'a', encoding="UTF-8") as copy_file:
    copy_file.write(f"{contacts_arr[line_copy_number - 1]}\n")

def ui():
  with open("phone_dict.txt", "a", encoding="UTF-8"):
    pass

  user_choice = 0
  while user_choice != 6:
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