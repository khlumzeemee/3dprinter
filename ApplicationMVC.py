from tkinter import Tk, RAISED, BOTH, LEFT, TOP, RIGHT, BOTTOM, messagebox
from tkinter.ttk import Frame, Button, Style, Label, Entry
from tinydb import Query

class ApplicationController(Tk):
  def __init__(self, *args, **kwargs):
      Tk.__init__(self, *args, **kwargs)
  
      # the container is where we'll stack a bunch of frames
      # on top of each other, then the one we want visible
      # will be raised above the others
      container = Frame(self)
      container.pack(side="top", fill="both", expand=True)
      container.grid_rowconfigure(0, weight=1)
      container.grid_columnconfigure(0, weight=1)
  
      self.frames = {}
      for F in (CreateCustomerView, ExecuteScriptView):
          frame = F(container, self)
          self.frames[F] = frame
          # put all of the pages in the same location;
          # the one on the top of the stacking order
          # will be the one that is visible.
          frame.grid(row=0, column=0, sticky="nsew")
  
      self.show_frame(StartPage)
  
  def show_frame(self, c):
      '''Show a frame for the given class'''
      frame = self.frames[c]
      frame.tkraise()
      
  def save_customer(self, * args, **kwargs):
    customer_id = self.model.save_customer(*args, **kwargs)
    
    show_frame(ExecuteScriptView)

  def run_take_picture_script(self):
    pass
  
  def run_update_script(self):
    pass
            
class CreateCustomerView(Frame):
  def __init__(self, master, controller):
    self.master = master
    self.master.title("3d Printer - Create customer")
    self.controller = controller
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

class ExecuteScriptView(Frame):
  def __init__(self, master, controller):
    self.master = master
    self.master.title("3d Printer - Execute script")
    self.controller = controller

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
  
  def show_frame(self, c):
        '''Show a frame for the given class'''
        frame = self.frames[c]
        frame.tkraise()  
  
app = ApplicationView()
app.mainloop()

root = Tk()
toplevel_view = Toplevel(root)

create_customer_view = CreateCustomerView(root)
create_customer_model = CreateCustomerModel()
controller = ApplicationController(create_customer_model, create_customer_view)

root.mainloop()

