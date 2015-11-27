from tkinter import Tk, RAISED, BOTH, LEFT, TOP, RIGHT, BOTTOM, messagebox
from tkinter.ttk import Frame, Button, Style, Label, Entry
from tinydb import Query

class CreateCustomerView(Frame):
  def __init__(self, master):
    self.master = master
    self.master.title("3d Printer - Create customer")
    self.controller = None
    self.entries = []
  
  def register(self, controller):
    self.controller = controller
  
  def initialize_ui(self):
    default_padding = {'padx': 10, 'pady' : 10}
    
    labels = ["Name", "Surname", "Email",  "Cellphone"]
    for label in labels:
      frame = Frame(self.master)
      Label(frame, text = label, style="BW.TLabel").pack(default_padding)
      entry = Entry(frame)
      entry.pack(default_padding)
      entries.append(entry)
      frame.pack(expand = True, fill = "x")

    args = ["name", "surname", "email",  "cellphone"]
    save_customer_function = lambda : self.controller.save_customer(dict(zip(args, e.get() for e in entries))) 
    button_frame = Frame(self.master)
    Button(self.button_frame, text = "Create Customer", command = self.controller.save_customer).pack(default_padding)
    button_frame.pack(expand = True, fill = "x")
  
class CreateCustomerModel(object):
  def __init__(self):
    self.db = TinyDB('/db/db.json')

  def save_customer(self, **kwargs):
    return db.insert(kwargs)
  
  def run_take_picture_script(self, customer_id):
    pass
  
  def run_update_script(self, customer_id):
    pass  

class ApplicationController(object):
  def __init__(self, model, view):
    self.model = model
    self.view = view
    self.view.register(self)
  
  def save_customer(self, **kwargs):
    customer_id = self.model.save_customer(**kwargs)
    
    #TODO Redirect to next view
  
  def run_take_picture_script(self):
    pass
  
  def run_update_script(self):
    pass
  
root = Tk()
create_customer_view = CreateCustomerView(root)
create_customer_model = CreateCustomerModel()
controller = ApplicationController(create_customer_model, create_customer_view)

root.mainloop()

