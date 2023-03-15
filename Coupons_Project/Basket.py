from Inventory import Inventory
class Basket:
    
    def __init__(self, shopping_list):
        self.shopping_list = shopping_list

    def view_basket(self):
        if len(self.shopping_list)==0:
            print('Your basket is currently empty.')
        else:
            print('Current items in your cart:')
            print('ITEM NAME, QUANTITY')
            for sublist in self.shopping_list:
                print(*sublist, sep=', ')
            print('\n')

    def add_item_to_cart(self, item_name, item_quantity):
        if item_name not in self.shopping_list:
            self.shopping_list.append([item_name, item_quantity])
            print(f'The item {item_name} has been successfully added to the basket.\n')

    def remove_item_from_cart(self, item_name):
        for index, sublist in enumerate(self.shopping_list):
            if item_name in sublist:
                self.shopping_list.pop(index)
        print(f'Item {item_name} successfully removed from the basket.\n')