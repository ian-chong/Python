class Employee():
    list_employee = []
    def __init__(self, employee_name, employee_id, employee_role, pay, username=None, password=None):
        self.employee_name = employee_name
        self.employee_id = employee_id
        self.employee_role = employee_role
        self.pay = pay
        self.email = employee_name + '@hospital.com'
        self.username = username
        self.password = password
        self.list_employee.append(self)
    
TomTheJanitor= Employee("Tom", 1, "Janitor",500, "Tom", "test")

print (TomTheJanitor.employee_name)
print (TomTheJanitor.employee_role)
print (TomTheJanitor.username)
print (TomTheJanitor.password)
print (TomTheJanitor.email)
