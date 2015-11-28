from tkinter import Tk, RAISED, BOTH, LEFT, TOP, RIGHT, BOTTOM, messagebox, Toplevel
from tkinter.ttk import Frame, Button, Style, Label, Entry
from tinydb import Query, TinyDB

class Application(Frame):
  """ Main class """
  
  def __init__(self,master):
    Frame.__init__(self,master)
    self.master = master
    self.initUI()
  
  def initUI(self):
    self.master.title("3D Printer")
    self.style = Style()
    
    #Create two screens
    self.create_customer = CreateCustomer(self)
    self.execute_script = ExecuteScript(self)
    

class CreateCustomer(Frame):
  """Create customer screen"""
  
  def __init__(self, master):
    Frame.__init__(self,master)
    
    self.master = master
    self.frame = Frame(self.master)
    self.initUI()
  
  def initUI(self):
    self.master.title("3D Printer - Add Customer")
    self.style = Style()

    default_padding = {'padx': 10, 'pady' : 10}

    #TODO change alignment    
    #Left frame for labels
    self.left_frame = Frame(self.master)
    
    self.name_label = Label(self.left_frame, text = "Name", style="BW.TLabel")
    self.name_label.pack(default_padding)

    self.surname_label = Label(self.left_frame, text = "Surname", style="BW.TLabel")
    self.surname_label.pack(default_padding)    

    self.email_label = Label(self.left_frame, text = "Email", style="BW.TLabel")
    self.email_label.pack(default_padding)

    self.cellphone_label = Label(self.left_frame, text = "Cellphone", style="BW.TLabel")
    self.cellphone_label.pack(default_padding)

    #Right frame for entries
    self.right_frame = Frame(self.master)
    
    self.name_entry = Entry(self.right_frame)
    self.name_entry.pack(default_padding)    

    self.surname_entry = Entry(self.right_frame)
    self.surname_entry.pack(default_padding)

    self.email_entry = Entry(self.right_frame)
    self.email_entry.pack(default_padding)

    self.cellphone_entry = Entry(self.right_frame)
    self.cellphone_entry.pack(default_padding)
    
    #Bottom frame for button
    self.button_frame = Frame(self.master)
    self.create_customer_button = Button(self.button_frame, text = "Create Customer", command = self.save_customer)
    self.create_customer_button.pack(default_padding)

    self.button_frame.pack(side = BOTTOM, fill = "x", expand = True)
    self.left_frame.pack(side = LEFT, expand = True, fill = "y")
    self.right_frame.pack(side = RIGHT, expand = True, fill = "y")

    self.frame.pack()

  def save_customer(self):
    print("saving customer")

    self.customer = Customer(self.name_entry.get(), self.surname_entry.get(),
                             self.email_entry.get(), self.cellphone_entry.get())
    if not self.customer.validate():
      messagebox.showerror(message = "All fields are mandatory, please fill in all the fields")
      return
    
    db = TinyDB('db/db.json')
    self.customer_id = db.insert(self.customer.__dict__)
    
    #TODO redirect to next page
    self.go_to_execute_script()
  
  def go_to_execute_script(self):
    """redirect to next page"""
    
    self.execute_script = Toplevel(self, self.master)
    self.app = ExecuteScript(self.execute_script)
     
class Customer(object):

  def __init__(self, name, surname, email, cellphone):
    self.name = name
    self.surname = surname
    self.email = email
    self.cellphone = cellphone

  def validate(self):
    return self.name and self.surname and self.email and self.cellphone
    
    
class ExecuteScript(Frame):
  """Execute script screen"""
  
  def __init__(self, master):
    Frame.__init__(self,master)
    self.master = master
    self.initUI()
  
  def initUI(self):
    #TODO add components here
    
    #Customer summary / id fields
    
    #Take picture button
    
    #Update button
    
    #Input text to display the script result
    pass

def main():
  
    root = Tk()
    app = CreateCustomer(root)
    root.mainloop()  


if __name__ == '__main__':
    main()  
