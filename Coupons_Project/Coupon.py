class Coupon:
    
    def __init__(self, couponList):
        self.couponList = dict(couponList)

    def view_coupons(self):
        for k, v in self.couponList.items():
            print(k, v)



