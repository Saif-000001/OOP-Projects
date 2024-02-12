from menu import Pizza, Burger, Drinks, Manu
from restaurent import Restaurent
from users import Chef, Server, Manager, Customer
from order import Order
def main():
    manu = Manu()

    # add pizza to the menu
    pizza_1 = Pizza('Shutki Pizza', 1200, 'large', ['shutki', 'oil', 'egg'])
    manu.add_manu_item('pizza', pizza_1)
    pizza_2 = Pizza('Alu Pizza', 1100, 'large', ['alu', 'oil', 'egg'])
    manu.add_manu_item('pizza', pizza_2)
    pizza_3 = Pizza('Dal pizza', 900, 'large', ['dal', 'oil', 'egg'])
    manu.add_manu_item('pizza', pizza_3)

    # add burger to the menu
    burger_1 = Burger('vagitable bureger', 250, 'vagitable', ['potatu', 'oil', 'onion'])
    manu.add_manu_item('burger', burger_1)
    burger_2 = Burger('cheken bureger', 500, 'cheken', ['cheken', 'oil', 'onion'])
    manu.add_manu_item('burger', burger_2)

    # add Drink to the menu
    coke = Drinks('Cook', 100, True)
    manu.add_manu_item('drink', coke)

    coffie = Drinks('mocha', 50, False)
    manu.add_manu_item('drink', coffie)

    # show Manu
    manu.show_manu()

    restaurent = Restaurent('Sai baba restaurent', manu)

    # add employees
    manager = Manager('kala chan manager', 241, 'kala@chan.com', 'uttora', 1500, 'Feb 12 2024', 'core')
    restaurent.add_employee('manager', manager)

    chef = Chef('Rustom Baburchi', 4512, 'rustom@baburchi.com', 'barisal', 3500, 'Feb 12, 2024', 'chef', 'everything')
    restaurent.add_employee('chef', chef)

    server = Server('chotu server', 451, 'chotu@server.com', 'feni', 1525, 'Feb 12, 2024', 'everythin')
    restaurent.add_employee('server', server)

    # show restaurent
    restaurent.show_employees()

    # Customer
    customer = Customer('shakib', 4512, 'king@khan.com', 'bonani', 100000)
    order = Order(customer, [pizza_3, coffie])
    customer.pay_for_order(order)
    restaurent.add_order(order)

    # Customer one paying for order
    restaurent.receive_payment(order, 2000, customer)

    print(restaurent.revenue, restaurent.balance)

    # pay rent
    # restaurent.pay_expense(restaurent.rent, 'Rent')
    print('After rent', restaurent.revenue, restaurent.balance, restaurent.expanse)


if __name__ == "__main__":
    main()
