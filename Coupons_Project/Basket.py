class Basket:
    
    def __init__(self, cartList):
        self.cartList = dict(cartList)

    def view_basket(self):
        for k, v in self.cartList.items():
            print(k, v)

    def add_item(self, new_item, new_quantity):
        self.cartList[new_item] = new_quantity

    def remove_item(self,remove):
        self.cartList.pop(remove)

    
        