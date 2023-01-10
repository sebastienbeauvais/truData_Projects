using System;

namespace ArchitectureProgram
{
    public class Coupon{
        // Maybe use a hashtable with pre-defined coupons??
        public string Name;
        public float Discount;
    }

    public class Item{
        public string Name;
        public float Price;
        public int Quantity;
    }

    public class Cart{
        
    }

    class Program{
        public void Main(string[] args){
            Item item = new Item();
            item.Name = "Milk";
            item.Price = 3.99;
            item.Quantity = 2;

            Coupon coupon = new Coupon();
            coupon.Name = "10% off cart total";
            coupon.Discount = .1;

            //Console.WriteLine("Your cart consists of " + item.Name + " the price is " + item.Price + " and quantity ("+ item.Quantity +")");
            //Console.WriteLine("Your Current Total: " + (item.Price*item.Quantity));
            //Console.WriteLine("We will apply a coupon to your basket: " + coupon.Name);
            //Console.WrtieLine("Your new cart total is: " + (item.Price*item.Quantity)*(1-coupon.Discount));

        }
    }
}