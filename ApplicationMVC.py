from tkinter import Tk, RAISED, BOTH, LEFT, TOP, RIGHT, BOTTOM, messagebox, StringVar, IntVar
from tkinter.ttk import Frame, Button, Style, Label, Entry, Radiobutton
from tinydb import TinyDB, Query
import scripts.takepicture as takepicture

class ApplicationController(Tk):
  def __init__(self, *args, **kwargs):
      Tk.__init__(self, *args, **kwargs)

      container = Frame(self)
      self.title("3d Printer")

      #This fied is populated on the first view
      #and displayed on the second
      self.customer_id = StringVar()
      
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

      self.model = CreateCustomerModel()
  
      self.show_frame(CreateCustomerView)
  
  def show_frame(self, c):
      '''Show a frame for the given class'''
      frame = self.frames[c]
      frame.tkraise()
      
  def save_customer(self, customer):
    """Save customer and go to next page"""
    customer_id = self.model.save_customer(customer)
    
    if customer_id:
      self.customer_id.set(customer_id)
      print(self.customer_id.get())
      self.show_frame(ExecuteScriptView)
    else:
      messagebox.showerror(message = "All fields are mandatory, please fill in all the fields")


  def run_take_picture_script(self, customer_id, picture_mode):
    """Example of executing outside python script"""
    return self.model.run_take_picture_script(customer_id, picture_mode)
  
  def run_update_script(self):
    pass



          
class CreateCustomerView(Frame):
  """View to enter customer information"""
  def __init__(self, master, controller):
    Frame.__init__(self,master)
    self.master = master
    self.controller = controller
    self.entries = []
    self.initialize_ui()
  
  def initialize_ui(self):
    default_padding = {'padx': 10, 'pady' : 10}
    
    labels = ["Name", "Surname", "Email",  "Cellphone"]
    for label in labels:
      frame = Frame(self)
      Label(frame, text = label, style="BW.TLabel").pack(default_padding, side = LEFT)
      entry = Entry(frame)
      entry.pack(default_padding, side = RIGHT)
      self.entries.append(entry)
      frame.pack(expand = True, fill = "x", side = TOP)
      
    button_frame = Frame(self)
    Button(button_frame, text = "Create Customer", command =  self.save_customer).pack(default_padding)
    button_frame.pack(expand = True, fill = "x")

  def save_customer(self):
    print("saving customer")

    args = ["name", "surname", "email",  "cellphone"]
    customer = dict(zip(args, (e.get() for e in self.entries)))
    print (customer)
    return self.controller.save_customer(customer) 




class ExecuteScriptView(Frame):
  """View to execute scripts"""
  def __init__(self, master, controller):
    Frame.__init__(self,master)
    self.master = master
    self.controller = controller

    self.initialize_ui()

  def initialize_ui(self):
    default_padding = {'padx': 10, 'pady' : 10}

    customer_frame = Frame(self)
    self.customer_id_label = Label(customer_frame, text = "Customer id:", style="BW.TLabel")
    self.customer_id_label.pack(default_padding, side = LEFT)

    self.customer_id_value = Label(customer_frame,style="BW.TLabel")
    self.customer_id_value["textvariable"] = self.controller.customer_id
    self.customer_id_value.pack(default_padding, side = LEFT)

    customer_frame.pack(expand = True, fill = "x")

    self.take_picture_frame = Frame(self, border = 10)
    
    self.picture_mode = IntVar()
    Radiobutton(self.take_picture_frame, text = "Light", variable = self.picture_mode, value = 1).pack(side = LEFT)
    Radiobutton(self.take_picture_frame, text = "Dark", variable = self.picture_mode, value = 2).pack(side = LEFT)
    
    self.button_take_picture = Button(self.take_picture_frame, text = "Take picture", command = self.take_picture)
    self.button_take_picture.pack(expand = True, fill = "x", side = BOTTOM)

    self.take_picture_frame.pack(expand = True)
    
    self.button_update = Button(self, text = "Update", command = self.controller.run_update_script)
    self.button_update.pack(expand = True, fill = "x")

  def take_picture(self):
    return self.controller.run_take_picture_script(self.controller.customer_id.get(), self.picture_mode.get())



    
class CreateCustomerModel(object):
  """Application business logic"""
  def __init__(self):
    pass

  def save_customer(self, customer):

    if not self.validate(customer):
      return None
    
    db = TinyDB('db/db.json')
    return db.insert(customer)

  def validate(self, customer):
    return customer['name'] and customer['surname'] and customer['email'] and customer['cellphone']
   
  
  def run_take_picture_script(self, customer_id, picture_mode):
    return takepicture.take_picture(customer_id, picture_mode)
  
  def run_update_script(self, customer_id):
    pass   

def main():
  app = ApplicationController()
  app.mainloop() 

if __name__ == '__main__':
    main()


