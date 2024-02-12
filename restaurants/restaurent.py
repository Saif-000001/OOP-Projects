class Restaurent:
    def __init__(self, name, rent, manu = []) -> None:
        self.name = name
        self.orders = []
        self.chef = None
        self.server = None
        self.manager = None
        self.rent = rent
        self.manu = manu
        self.revenue = 0
        self.expanse = 0
        self.balance = 0
        self.profit = 0
    
    def add_employee(self, employ_type, employee):
        if employ_type == 'chef':
            self.chef = employee
        elif employ_type == 'server':
            self.server = employee
        elif employ_type == 'manager':
            self.manager = employee
    
    def add_order(self, order):
        self.orders.append(order)
    
    def receive_payment(self, order, amount, customer):
        if amount >= order.bill:
            self.revenue += order.bill
            self.balance += order.bill
            customer.due_amount = 0
            return amount - order.bill
        else:
            print("Not Enough money, pay more.")
    
    def pay_expense(self, amount, description):
        if amount > self.balance:
            self.expanse += amount
            self.balance -= amount
            print(f'Expense {amount} for {description}')
        
        else :
            print(f'Not enough money to pay {amount}')
    
    def pay_salary(self, employee):
        print(f'Paying salary for {employee.name} salary: {employee.salary}')
        if employee.salary < self.balance:
            self.balance -= employee.salary
            self.expanse += employee.salary
            employee.receive_salary()
    def show_employees(self):
        print('--------------Showing Employees')

        if self.chef is not None:
            print(f'Chef: {self.chef.name} with salary: {self.chef.salary}')
        
        if self.server is not None:
            print(f'Server: {self.server.name} with salary: {self.server.salary}')
        
        if self.manager is not None:
            print(f'Manager: {self.manager.name} with salary: {self.manager.salary}')