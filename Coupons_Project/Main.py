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
    for key1 in basket1.cartList:
        for key2 in inventory1.inventoryList:
            if key1 == key2:
                total += inventory1.inventoryList[key1]
    
    # showing basket and total
    while True:
        usr_in = input('Would you like to see your current basket (y/n)?: ')
        if usr_in == 'y':
            # pre-defined basket
            print('ITEM NAME\tPRICE\t\tQTY')
            for key1 in basket1.cartList:
                for key2 in inventory1.inventoryList:
                    if key1 == key2:
                        print(f'{key1}\t\t{inventory1.inventoryList[key1]}\t\t{basket1.cartList[key1]}')
            print(f'Your current total is: ${total}')
            break

        elif usr_in == 'n':
            print(f'Your current total is: ${total}')
            break

        else:
            print('Sorry, we did not recognize that command.')
            continue

    while True:
        usr_in = input('Would you like to add or remove an item (a/r/n)?: ')
        # 'a' is for adding item
        if usr_in == 'a':
            usr_in1 = input('Please type the item you\'d like to add: ')
            usr_in2 = input(f'How many {usr_in1}\'s would you like?: ')
            if usr_in not in inventory1.inventoryList:
                print('Sorry, we dont carry that item')
            else:
                basket1 = basket1.add_item(usr_in1, usr_in2)
        # 'r' is for removing an item
        elif usr_in == 'r':
            pass
        # 'n' is a happy customer
        elif usr_in == 'n':
            pass
        # no command found
        else:
            print('Sorry, we did not recognize that command.')


    # applyin coupon
    while True:
        usr_in = input('Would you like to use a coupon (y/n)?: ')
        if usr_in == 'y':
            print('COUPON NAME\t\tDISCOUNT')
            Coupon.view_coupons(coupon1)
            cpn_in = input('Enter the coupon you would like to use: ')
            for key1 in coupon1.couponList:
                if cpn_in == key1:
                    disc = coupon1.couponList[key1]
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