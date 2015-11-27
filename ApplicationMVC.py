class CreateCustomerView(Frame):
  def __init__(self):
    self.master = Tk()
    self.master.title("3d Printer - Create customer")
    self.controller = None
  
  def register(self, controller):
    self.controller = controller
  
  def initialize_ui(self):
    pass

class CreateCustomerModel(object):
  pass

class CreateCustomerController(object):
  def __init__(self, model, view):
    self.model = model
    self.view = view
  
  

    create_customer_view = CreateCustomerView()
    create_customer_model = CreateCustomerModel()
    create_customer_controller = CreateCustomerController(create_customer_model, create_customer_view)

    create_customer_view.main_loop()
