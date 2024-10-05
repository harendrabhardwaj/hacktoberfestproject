#estaurant Management System Project

class MenuItem:  
    def __init__(self, name, price):  
        self.name = name  
        self.price = price  

    def __str__(self):  
        return f"{self.name}: ${self.price:.2f}"  


class Order:  
    def __init__(self):  
        self.items = []  

    def add_item(self, item):  
        self.items.append(item)  

    def total(self):  
        return sum(item.price for item in self.items)  

    def print_bill(self):  
        print("Order Bill:")  
        for item in self.items:  
            print(item)  
        print(f"Total: ${self.total():.2f}")  


class Table:  
    def __init__(self, table_number):  
        self.table_number = table_number  
        self.order = None  

    def take_order(self):  
        self.order = Order()  

    def add_to_order(self, item):  
        if self.order is not None:  
            self.order.add_item(item)  
        else:  
            print("No order taken for this table.")  

    def print_bill(self):  
        if self.order is not None:  
            print(f"Bill for Table {self.table_number}:")  
            self.order.print_bill()  
        else:  
            print("No orders have been taken for this table.")  


class Restaurant:  
    def __init__(self):  
        self.menu = []  
        self.tables = {}  

    def add_menu_item(self, item):  
        self.menu.append(item)  

    def show_menu(self):  
        print("Menu:")  
        for item in self.menu:  
            print(item)  

    def add_table(self, table_number):  
        if table_number not in self.tables:  
            self.tables[table_number] = Table(table_number)  
            print(f"Table {table_number} added.")  
        else:  
            print(f"Table {table_number} already exists.")  

    def get_table(self, table_number):  
        return self.tables.get(table_number, None)  

# Example Usage  
if __name__ == "__main__":  
    restaurant = Restaurant()  

    # Adding items to the menu  
    restaurant.add_menu_item(MenuItem("Burger", 8.99))  
    restaurant.add_menu_item(MenuItem("Fries", 3.49))  
    restaurant.add_menu_item(MenuItem("Soda", 1.99))  

    restaurant.show_menu()  

    # Adding tables  
    restaurant.add_table(1)  
    restaurant.add_table(2)  

    # Taking orders  
    table1 = restaurant.get_table(1)  
    table1.take_order()  
    table1.add_to_order(restaurant.menu[0])  # Burger  
    table1.add_to_order(restaurant.menu[1])  # Fries  

    # Printing bill for table 1  
    table1.print_bill()  

    # Trying for a table with no orders  
    table2 = restaurant.get_table(2)  
    table2.print_bill()  # No orders
