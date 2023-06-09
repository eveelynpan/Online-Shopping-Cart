class ItemToPurchase:
    def __init__(self, item_name='none', item_price=0, item_quantity=0, item_description='none'):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_cost(self):
        total_price = self.item_price * self.item_quantity
        print(f'{self.item_name} {self.item_quantity} @ ${self.item_price} = ${total_price}')

    def print_item_description(self):
        print(f'{self.item_name}: {self.item_description}')


class ShoppingCart:
    def __init__(self, customer_name='none', current_date='January 1, 2016', cart_items=[]):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items

    def add_item(self, ItemToPurchase):
        self.cart_items.append(ItemToPurchase)

    def remove_item(self, remove_item):
        for i in self.cart_items:
            if i.item_name == remove_item:
                self.cart_items.remove(i)
                return
        print("Item not found in cart. Nothing removed.")

    def modify_item(self, ItemToPurchase):
        for i in self.cart_items:
            if i.item_name == ItemToPurchase.item_name:
                i.item_quantity = ItemToPurchase.item_quantity
                return
        print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        total_quantity = 0
        for i in self.cart_items:
            total_quantity = total_quantity + i.item_quantity
        return total_quantity

    def get_cost_of_cart(self):
        total_price = 0
        for i in self.cart_items:
            total_price = total_price + i.item_price * i.item_quantity
        return total_price

    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        if self.cart_items != []:
            print(f'Number of Items: {self.get_num_items_in_cart()}')
            print()
            for i in self.cart_items:
                i.print_item_cost()
            print()
            print(f"Total: ${self.get_cost_of_cart()}")
        else:
            print(f"Number of Items: 0")
            print("\nSHOPPING CART IS EMPTY")
            print("\nTotal: $0")

    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print()
        print("Item Descriptions")
        for i in self.cart_items:
            i.print_item_description()


def print_menu():
    print("MENU\na - Add item to cart\nr - Remove item from cart\nc - Change item quantity\n"
          "i - Output items' descriptions\no - Output shopping cart\nq - Quit\n")


def execute_menu(option, ShoppingCart):
    if option == 'o':
        print('OUTPUT SHOPPING CART')
        ShoppingCart.print_total()
    elif option == 'i':
        print("OUTPUT ITEMS' DESCRIPTIONS")
        ShoppingCart.print_descriptions()
    elif option == 'a':
        print('ADD ITEM TO CART')
        print('Enter the item name:')
        name = input()
        print('Enter the item description:')
        description = input()
        print('Enter the item price:')
        price = int(input())
        print('Enter the item quantity:')
        quantity = int(input())
        item1 = ItemToPurchase(name, price, quantity, description)
        ShoppingCart.add_item(item1)
    elif option == 'r':
        print('REMOVE ITEM FROM CART')
        print('Enter name of item to remove:')
        remove_item = input()
        ShoppingCart.remove_item(remove_item)
    elif option == 'c':
        print('CHANGE ITEM QUANTITY')
        print('Enter the item name:')
        modify_name = input()
        print('Enter the new quantity:')
        new_quan = int(input())
        item = ItemToPurchase(modify_name, item_quantity=new_quan)
        ShoppingCart.modify_item(item)


if __name__ == "__main__":
    print("Enter customer's name:")
    cust_name = input()
    print("Enter today's date:")
    curr_date = input()
    cart1 = ShoppingCart(cust_name, curr_date)
    print()
    print(f'Customer name: {cart1.customer_name}')
    print(f"Today's date: {cart1.current_date}")
    print()

    option_list = ['r', 'a', 'c', 'i', 'o']
    print_menu()
    option = str(input('Choose an option:\n'))

    while option != 'q':
        if option in option_list:
            execute_menu(option, cart1)
            print()
            print_menu()
            option = input('Choose an option:\n')
        else:
            option = input('Choose an option:\n')

