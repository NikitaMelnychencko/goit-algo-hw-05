from helper.color_loger import  log_warning
from decorators.error_decorators import input_error

class NotebookServices:
  def __init__(self, initial_contacts=None):
    self.contacts = initial_contacts if initial_contacts else {}

  @input_error
  def add_contact(self, args):
    if len(args) != 2:
      raise ValueError("Please provide name and phone number")
    name, phone = args
    self.contacts[name] = phone
    return f"Contact {name} added."

  @input_error
  def check_contact(self, name):
    if name in self.contacts:
      return True
    else:
      return False

  @input_error
  def add_contact_by_exception(self, args):
    def foo():
      answer = input("Create new contact? (y/n)")
      if answer.lower() == "y":
        return print(self.add_contact(args))
    return foo

  @input_error
  def change_contact(self, args):
    if len(args) != 2:
      raise ValueError("Please provide name and phone number")
    name, phone = args
    if not self.check_contact(name):
        raise Warning({"massage": f"Contact {name} not found.", "callback": self.add_contact_by_exception(args)})
    else:
      self.contacts[name] = phone
      return f"Contact {name} changed."

  @input_error
  def get_contact(self, name):
    if not self.check_contact(name):
      raise Warning({"massage":f"Contact {name} not found."})

    return f"Contact {name}: {self.contacts[name]}"

  @input_error
  def get_all_contacts(self):
    return self.contacts
