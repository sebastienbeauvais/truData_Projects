import sys

import pandas as pd
import numpy as np

def main():

    # declaring variables
    shopping_list = []
    shopping_total = []
    usr_in = ''

    # availble items
    items = {
        'item_name':['Milk', 'Bread', 'Eggs', 'Butter', 'Coffee', 'Creamer', 'Chicken', 'Pie'], 
        'price':[3.99, 2.99, 5.99, 1.99, 1.50, 0.65, 12.00, 10.00, ]
    }
    
    # loading into dataframe
    items_df = pd.DataFrame(data=items)

    # available coupons
    coupons = {
        'coupon_name':['10%', '25%', 'BOGO'],
        'discount':[0.1, 0.25, 0.50]
    }

    # loading into dataframe
    coupons_df = pd.DataFrame(data=coupons)

    # showing customer list of items available
    print(items_df.to_string(index=False))

    # getting users list of items
    while usr_in != "done":
        usr_in = input('Please enter an item: ')

        # check if any strings match user input
        if items_df.item_name.str.contains(usr_in).any():
            print(f'{usr_in} was added to the basket.')
            shopping_list.append(usr_in)

        # if the user is done we will add the total
        elif usr_in == "done":
            print('Items added to the basket.') 
            for i in range(len(shopping_list)):
                item_lookup = shopping_list[i]
                
                # getting price of each item
                shopping_total.append(items_df[items_df['item_name']==item_lookup]['price'].values[0])
            
            print(f'Your current total is {sum(shopping_total)}')
            shopping_total = sum(shopping_total)

        # if the item does not exist
        else:
            print('Sorry, we do not carry that item.')

    # prompt user if they want to use a coupon
    coupon_yn = input('Would you like to use a coupon (Y/N):')

    if coupon_yn == 'Y':
        # showing customer list of coupons available
        print(coupons_df.to_string(index=False))
        coupon_in = input('Please select a coupon: ')

        # Reformat for overall discounts
        if coupons_df.coupon_name.str.contains(coupon_in).any():
            print(f'Applying {coupon_in} discount to your cart.')
            discount = coupons_df[coupons_df['coupon_name']==coupon_in]['discount'].values[0]
            disc_total = shopping_total*(1-discount)
            print(f'Your new total is: {disc_total}')

        # create elif for BOGO

        else:
            print('Sorry, that does not match any of the available coupons.')

    elif coupon_yn == 'N':
        print(f'Your total is: {shopping_total}')

    else:
        print('Response not found.')
        print(f'Your total is {shopping_total}')
    
    # create case to loop back for correct input if user inputs wrong answer
if __name__ == "__main__":
    sys.exit(main())


