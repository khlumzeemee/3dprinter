from Tkinter import Tk, RAISED, BOTH
from Ttk import Frame, Button, Style, Label

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
  
  def self.initUI(self):
    self.master.title("3D Printer - Add Customer")
    self.style = Style()
    #TODO add components here
    #Labels and inputtexts
    
    #Create Customer Button
    #Saving to DB and generating an ID
    #Redirecting to the next screen
    
    self.frame.pack()
  
  def go_to_execute_script(self):
    """redirect to next page"""
    self.execute_script = Toplevel(self, self.master)
    self.app = ExecuteScript(self.execute_script)

class ExecuteScript(Frame):
  """Execute script screen"""
  
  def __init__(self, master):
    Frame.__init__(self,master)
    self.master = master
    self.initUI()
  
  def self.initUI(self):
    #TODO add components here
    
    #Customer summary / id fields
    
    #Take picture button
    
    #Update button
    
    #Input text to display the script result
    pass

def main():
  
    root = Tk()
    root.geometry("300x200+300+300")
    app = CreateCustomer(root)
    root.mainloop()  


if __name__ == '__main__':
    main()      
