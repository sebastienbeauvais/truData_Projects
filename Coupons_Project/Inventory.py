class Inventory:
                                                                                                                             
    def __init__(self, dictionary):
        self.dictionary = dict(dictionary)

    def view_inventory(self):
        for k, v in self.dictionary.items():
            print(f'{k}\t{v}')