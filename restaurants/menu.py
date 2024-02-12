class Food:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price
        self.cooking_time = 15

class Burger(Food):
    def __init__(self, name, price, meat, ingradients) -> None:
        self.meat = meat
        self.ingradients = ingradients
        super().__init__(name, price)

class Pizza(Food):
    def __init__(self, name, price, size, toppings) -> None:
        self.size = size
        self.toppings = toppings
        super().__init__(name, price)

class Drinks(Food):
    def __init__(self, name, price, isCold = True) -> None:
        self.isCold = isCold
        super().__init__(name, price)

# Composition

class Manu:
    def __init__(self) -> None:
        self.pizzas = []
        self.burgers = []
        self.drinks = []

    def add_manu_item(self,item_types, item):
        if item_types == 'pizza':
            self.pizzas.append(item)
        if item_types == 'burger':
            self.burgers.append(item)
        if item_types == 'drink':
            self.drinks.append(item)
    
    def remove_pizza(self, pizza):
        if pizza in self.pizzas:
            self.pizzas.remove(pizza)
    
    def show_manu(self):
        for pizza in self.pizzas:
            print(f'name : {pizza.name} price : {pizza.price}')
        
        for burger in self.burgers:
            print(f'name : {burger.name} price : {burger.price}')

        for drink in self.drinks:
            print(f'name : {drink.name} price : {drink.price}')