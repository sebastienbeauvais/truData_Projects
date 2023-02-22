class Coupon:
    
    def __init__(self, coupon_name, discount):
        self.coupon_name = coupon_name
        self.discount = discount

    def apply_coupon(self, total):
        return round(total*(1-self.discount), 2)
