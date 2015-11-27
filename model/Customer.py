class Customer(object):
  """Customer data"""
  def __init__(self, name, surname, email, cellphone):
    self.name = name
    self.surname = surname
    self.email = email
    self.cellphone = cellphone

  def validate(self):
    return self.name and self.surname and self.email and self.cellphone

  def to_json(self)
    return self.__dict__
