from Inventory import Inventory
from Coupon import Coupon
from Basket import Basket

# function to compare inventory and current basket 
# to get a total for checkout
def reciept(inventory, basket):
    total_price=0
    for inv_item in inventory:
        for basket_item in basket:
            if inv_item[0] == basket_item[0]:
                total_price += inv_item[1]*basket_item[1]
    print(f'Your total is: ${total_price}')

def main():
    # creating an inventory list to pass into the inventory class
    store_inv = [
        ['Whole Milk', 3.99],
        ['White Bread', 1.99],
        ['12 Large Brown Eggs', 6.99],
        ['Dark Roast Coffee Beans', 2.50],
        ['Light Roast Coffee Beans', 2.99],
        ['Salted Butter', 1.99],
        ['Unsalted Butter', 1.99],
        ['1lb Chicken Breasts', 6.50],
        ['12oz Steak', 8.99],
        ['Oat Milk', 3.79]
    ]

    # creating an empty list for a shopping cart
    shopping_list = []
    

    # creating instances
    coupon1 = Coupon('10OFF', .1)

    # Creating an inventory
    inventory1 = Inventory(store_inv)

    # creating a shopping list instance
    basket1 = Basket(shopping_list)

    print('Welcome to our store!\n')
    inventory1.print_inventory()

    # adding an item to the store inventory
    #inventory1.add_inventory_item('2% Milk', 3.95)
    #inventory1.remove_inventory_item('Whole Milk')

    basket1.view_basket()
    basket1.add_item_to_cart('Whole Milk', 2)
    basket1.add_item_to_cart('White Bread', 4)
    basket1.view_basket()
    basket1.remove_item_from_cart('Whole Milk')
    basket1.view_basket()

    # getting total price
    reciept(inventory1.inventory_list, basket1.shopping_list)



if __name__ == '__main__':
    main() 