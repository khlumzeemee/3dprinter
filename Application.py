from Tkinter import Tk, RAISED, BOTH
from Ttk import Frame, Button, Style, Label

class Application(Frame):
  
  def __init__(self,master):
    Frame.__init__(self,master)
    self.master = master
    self.initUI()
  
  def initUI(self):
    self.master.title("3D Printer")
    self.style = Style()
    
    frame = Frame(self, relief = RAISED, borderwidth = 1)
    frame.pack(fill = BOTH, expand = 1)
    
    self.pack(fill = BOTH, expand = 1)
    
    closeButton = Button(self, text="Close")
    closeButton.pack(side=RIGHT, padx=5, pady=5)
    okButton = Button(self, text="OK")
    okButton.pack(side=RIGHT)

def main():
  
    root = Tk()
    root.geometry("300x200+300+300")
    app = Application(root)
    root.mainloop()  


if __name__ == '__main__':
    main()      
