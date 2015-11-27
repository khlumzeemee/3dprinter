from tkinter import Tk, RAISED, BOTH, LEFT, TOP, RIGHT, BOTTOM, messagebox
from tkinter.ttk import Frame, Button, Style, Label, Entry
from tinydb import Query

class CreateCustomerView(Frame):
  def __init__(self, master):
    self.master = master
    self.master.title("3d Printer - Create customer")
    self.controller = None
    self.entries = {}
  
  def register(self, controller):
    self.controller = controller
  
  def initialize_ui(self):
    default_padding = {'padx': 10, 'pady' : 10}
    
    elements = {"name": "Name", "surname": "Surname", "email": "Email", "cellphone" : "Cellphone"}
    for k,v in elements.iteritems():
      frame = Frame(self.master)
      Label(frame, text = v, style="BW.TLabel").pack(default_padding)
      entries[k] = Entry(frame)
      entries[k].pack(default_padding)
      frame.pack(expand = True, fill = "x")
    
    customer = dict(((k, v.get()) for k,v in self.entries.iteritems()))

    save_customer_function = lambda : self.controller.save_customer(customer)
    button_frame = Frame(self.master)
    Button(self.button_frame, text = "Create Customer", command = self.controller.save_customer).pack(default_padding)
  
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

