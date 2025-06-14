from helper.color_loger import  log_warning

class NotebookServices:
  def __init__(self, initial_contacts=None):
    self.contacts = initial_contacts if initial_contacts else {}

  def add_contact(self, args):
    if len(args) != 2:
      log_warning("Please provide name and phone number")
      return ""
    name, phone = args
    self.contacts[name] = phone
    return f"Contact {name} added."


  def check_contact(self, name):
    if name in self.contacts:
      return True
    else:
      return False


  def change_contact(self, args):
    if len(args) != 2:
      log_warning("Please provide name and phone number")
      return ""
    name, phone = args
    if not self.check_contact(name):
      log_warning(f"Contact {name} not found.")
      answer = input("Create new contact? (y/n)")
      if answer.lower() == "y":
        return self.add_contact(args)
    else:
      self.contacts[name] = phone
      return f"Contact {name} changed."

  def get_contact(self, name):
    if not self.check_contact(name):
      log_warning(f"Contact {name} not found.")
      return ""

    return f"Contact {name}: {self.contacts[name]}"

  def get_all_contacts(self):
    return self.contacts
