import platform
import subprocess

from Inventory import Inventory
from Coupon import Coupon
from Basket import Basket


def clear_screen():
    '''clears terminal screen before starting'''

    # Clear command as function of OS
    command = 'cls' if platform.system().lower() == 'windows' else 'clear'

    # Action
    return subprocess.call(command) == 0

def main():
    clear_screen()

    # defining dictionary to pass to method
    inventory = {
        'Milk': 3.99,
        'Bread': 2.50,
        'Eggs': 4.00,
        'Coffee': 2.00,
        'Creamer': 0.50,
        'Pie': 10.99
    }

    coupons = {
        '10': 0.10,
        '25': 0.25,
        'BOGO': 0.50
    }

    shopping_cart1 = {
        'Milk': 2,
        'Bread': 1,
        'Eggs': 4,
        'Pie': 1
    }

    # creating instances
    inventory1 = Inventory(inventory)

    coupon1 = Coupon(coupons)

    basket1 = Basket(shopping_cart1)
    
    print('What would you like to add to your basket?\n')
    # shows store inventory
    Inventory.view_inventory(inventory1)

    usr_in = input('Would you like to see your current basket (y/n)?: ')
    if usr_in == 'y':
        # pre-defined basket
        print('item_name\tprice\t\tqty')
        for key1 in basket1.dictionary:
            for key2 in inventory1.dictionary:
                if key1 == key2:
                    print(f'{key1}\t\t{inventory1.dictionary[key1]}\t\t{basket1.dictionary[key1]}')
    elif usr_in == 'n':
        print('item_name\tprice\t\tqty')
        for key1 in basket1.dictionary:
            for key2 in inventory1.dictionary:
                if key1 == key2:
                    print(f'{key1}\t\t{inventory1.dictionary[key1]}\t\t{basket1.dictionary[key1]}')
        #print(f'Your current total is: {curr_total}')
    else:
        print('Sorry, we did not recognize that command.')        


if __name__ == '__main__':
    main() 
    
            