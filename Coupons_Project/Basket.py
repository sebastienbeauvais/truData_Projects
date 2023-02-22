class Basket:
    
    def __init__(self):
        self.content = dict()

    def __dict__(self):
        return self.content

    def update(self, item):
        if item.id not in self.content:
            self.content.update({item.id: item})
            return
        for k, v in self.content.get(item.id).iteritems():
            if k == 'id':
                continue
            elif k == 'quantity':
                total_qty = v.quantity + item.quantity
                if total_qty:
                    v.quantity = total_qty
                    continue
                self.remove_item(k)
            else:
                v[k] = item[k]

    def get_total(self):
        return sum([v.price * v.quantity for _, v in self.content.items()])
    
    def get_num_items(self):
        return sum([v.quantity for _, v in self.content.items()])
    
    def remove_item(self, key):
        self.content.pop(key)

    def view_basket(self):
        print('ITEMS:', [v.name for _, v in self.content.items()])
        print('PRICES:', [v.price for _, v in self.content.items()])
        print('QUANTITES:', [v.quantity for _, v in self.content.items()])
        print('\n')