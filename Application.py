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
    self.initUI()
  
  def self.initUI(self):
    #TODO add components here
    #Labels and inputtexts
    
    #Create Customer Button
    #Saving to DB and generating an ID
    #Redirecting to the next screen
    pass

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
    app = Application(root)
    root.mainloop()  


if __name__ == '__main__':
    main()      
