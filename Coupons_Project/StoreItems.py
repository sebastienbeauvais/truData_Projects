class StoreItems:

    def __init__(self, item_name, item_price):
        self.item_name = item_name
        self.item_price = item_price

    

    def display_inventory(dict):
        print("Current Items in Stock:")
        for k, v in dict.items():
            print(k, v)

item_dict = {
        'Milk': 3.99,
        'Bread': 2.50,
        'Eggs': 4.00,
        'Coffee': 2.00,
        'Creamer': 0.50,
        'Pie': 10.99
    } 
    
def main():
    display_inventory(item_dict)