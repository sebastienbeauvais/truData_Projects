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

    # creating instances

    coupon1 = Coupon('10OFF', .1)

    # creating inventory items
    item1 = Inventory(1, 'Milk', 3.99, 1)
    item2 = Inventory(2, 'Bread', 2.75, 1)
    item3 = Inventory(3, 'Eggs', 5.49, 1)

    # creating a shopping cart
    cart = Basket()

    # adding items to cart
    cart.update(item1)
    cart.update(item2)
    cart.update(item3)

    # viewing items in cart
    cart.view_basket()

    # removing item in cart
    cart.remove_item(2)

    # checking updated cart
    cart.view_basket()

    # viewing total
    print(f'You have {cart.get_num_items()} items in your cart for a total of ${cart.get_total()}\n')


    # applying coupon to cart
    print(f'Your coupon {coupon1.coupon_name} has been applied to your cart')
    print(f'Your new total is ${coupon1.apply_coupon(cart.get_total())}')
    


if __name__ == '__main__':
    main() 