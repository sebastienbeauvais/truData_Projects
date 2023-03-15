class Inventory:
                                                                                                                             
    def __init__(self, inventory_list):
        self.inventory_list = inventory_list

    def print_inventory(self):
        print('Here is what we have in stock:')
        print('ITEM NAME, PRICE')
        for sublist in self.inventory_list:
            print(*sublist, sep=', ')
        print('\n')

    def add_inventory_item(self, item_name, item_price):
        if item_name not in self.inventory_list:
            self.inventory_list.append([item_name, item_price])
            print(f'The item {item_name} has been successfully added to inventory.\n')
        else:
            print('That item is already in inventory.')

    def remove_inventory_item(self, item_name):
        for index, sublist in enumerate(self.inventory_list):
            if item_name in sublist:
                self.inventory_list.pop(index)
        print(f'Item {item_name} successfully removed from inventory.\n')
            
