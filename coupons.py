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
        'item_name':['Milk', 'Bread', 'Eggs', 'Butter', 'Coffee'], 
        'price':[3.99, 2.99, 5.99, 1.99, 1.50]
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
            print(f'{usr_in} is in stock')
            shopping_list.append(usr_in)
            
            

        # if the user is done we will add the total
        elif usr_in == "done":
            print('Items added to the basket.') 
            for i in range(len(shopping_list)):
                item_lookup = shopping_list[i]
                
                # getting price of each item
                shopping_total.append(items_df[items_df['item_name']==item_lookup]['price'].values[0])
            print(sum(shopping_total))

        # if the item does not exist
        else:
            print('Sorry, we do not carry that item.')

    #for x in range(len(shopping_list)):
    #    print(shopping_list[x])

if __name__ == "__main__":
    sys.exit(main())


