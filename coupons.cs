using System.Collections;

namespace ArchitectureProgram
{
    public class ShoppingCart{
        public string? ItemName;
        // public float ItemPrice;
        public int Quantity;
    }

    public class Coupon{
        // Maybe use a hashtable with pre-defined coupons??
        public string? Name;
        public float Discount;
    }

    public class Inventory{
        public string? Item;
        public float Price;
    }

    class Program{
        public static void Main(string[] args){

            Console.WriteLine("Welcome to our store. Here is what we have in stock:");

            Dictionary<string, float> inventoryDict = new Dictionary<string, float>();
            inventoryDict.Add("Milk", 3.99f);
            inventoryDict.Add("Bread", 2.50f);
            inventoryDict.Add("Eggs", 4.00f);
            inventoryDict.Add("Coffee", 2.00f);
            inventoryDict.Add("Creamer", 0.50f);
            

            Dictionary<string, float> couponDict = new Dictionary<string, float>();
            couponDict.Add("10%", 0.10f);
            couponDict.Add("25%", 0.25f);

            Dictionary<string, int> shoppingCartDict = new Dictionary<string, int>();
            shoppingCartDict.Add("Milk", 2);
            shoppingCartDict.Add("Bread", 1);
            shoppingCartDict.Add("Eggs", 4);
            shoppingCartDict.Add("Pie", 1);


            // creating inventory objects off dictionary
            Inventory inventory = new Inventory();
            foreach(string key in inventoryDict.Keys){
                inventory.Item = key;
                inventory.Price = inventoryDict[key];
            }

            // creating shoppingcart objects off dictionary
            ShoppingCart cart = new ShoppingCart();
            foreach(string key in shoppingCartDict.Keys){
                cart.ItemName = key;
                cart.Quantity = shoppingCartDict[key];
            }

            // creating coupon objects off dictionary
            Coupon coupon = new Coupon();
            foreach(string key in couponDict.Keys){
                coupon.Name = key;
                coupon.Discount = couponDict[key];
            }

            // Printing hashtable of items
            Console.WriteLine("Item Name\tPrice");
            foreach(string key in inventoryDict.Keys){
                Console.WriteLine(String.Format("{0}\t\t${1}", key, inventoryDict[key]));
            }      
        }
    }
}