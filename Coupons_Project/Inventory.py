class Inventory:
                                                                                                                             
    def __init__(self, inventoryList):
        self.inventoryList = dict(inventoryList)

    def view_inventory(self):
        for k, v in self.inventoryList.items():
            print(k, v)




