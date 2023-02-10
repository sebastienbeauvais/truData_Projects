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
    '''clear screen() does not work on windows machines'''
    # clear_screen()

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
    
    print('Welcome to our store. Here is what we have in stock:\n')
    # shows store inventory
    Inventory.view_inventory(inventory1)

    # getting total
    total = 0
    for key1 in basket1.dictionary:
        for key2 in inventory1.dictionary:
            if key1 == key2:
                total += inventory1.dictionary[key1]
    
    # showing basket and total
    while True:
        usr_in = input('Would you like to see your current basket (y/n)?: ')
        if usr_in == 'y':
            # pre-defined basket
            print('ITEM NAME\tPRICE\t\tQTY')
            for key1 in basket1.dictionary:
                for key2 in inventory1.dictionary:
                    if key1 == key2:
                        print(f'{key1}\t\t{inventory1.dictionary[key1]}\t\t{basket1.dictionary[key1]}')
            print(f'Your current total is: ${total}')
            break

        elif usr_in == 'n':
            print(f'Your current total is: ${total}')
            break

        else:
            print('Sorry, we did not recognize that command.')
            continue

    # applyin coupon
    while True:
        usr_in = input('Would you like to use a coupon (y/n)?: ')
        if usr_in == 'y':
            print('COUPON NAME\t\tDISCOUNT')
            Coupon.view_coupons(coupon1)
            cpn_in = input('Enter the coupon you would like to use: ')
            for key1 in coupon1.dictionary:
                if cpn_in == key1:
                    disc = coupon1.dictionary[key1]
                    new_total = total*(1-disc)
                    print(f'Your new total: ${new_total}')
                else:
                    continue
            break
        elif usr_in == 'n':
            print(f'Your total is: ${total}')
            break
        else:
            print('Sorry, we did not recognize that command.')
            continue


if __name__ == '__main__':
    main() 