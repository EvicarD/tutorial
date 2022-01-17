class Employee:
  pass

class EmployeeTest:

  raise_amount = 1.05
  number_of_employee = 0

  def __init__(self, name, occupation, email, salary):
      self.name = name
      self.occupation = occupation
      self.email = email
      self.salary = salary

      EmployeeTest.number_of_employee += 1

  # def salary_raise(self):
  #   self.salary *= 1.05 # this is magic number
  def salary_raise(self):
    self.salary *= self.raise_amount # this is magic number

  def __str__(self):
    return f"His name is {self.name}, position : {self.occupation}, salary: ${self.salary}, email: {self.email}"


class Employer(EmployeeTest):
  def __init__(self, name, occupation, email, salary, car):
      self.car = car
      super().__init__(name, occupation, email, salary)