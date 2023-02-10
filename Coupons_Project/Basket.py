class Basket:
    
    def __init__(self, dictionary):
        self.dictionary = dict(dictionary)

    def view_basket(self):
        for k, v in self.dictionary.items():
            print(k, v)


    
        