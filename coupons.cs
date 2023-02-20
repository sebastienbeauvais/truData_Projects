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


            /*
            // creating a coupon object
            Coupon coupon = new Coupon();
            coupon.Name = "10% off";
            coupon.Discount = 0.1f;

            // creating the store inventory
            Inventory inventory = new Inventory();
            inventory.Item = "Milk";
            inventory.Price = 3.99f;

            inventory.Item = "Bread";
            inventory.Price = 2.50f;

            inventory.Item = "Eggs";
            inventory.Price = 4.00f;

            inventory.Item = "Coffee";
            inventory.Price = 2.00f;

            inventory.Item = "Creamer";
            inventory.Price = 0.50f;

            inventory.Item = "Pie";
            inventory.Price = 10.00f;


            // creating the shopping cart
            ShoppingCart cart = new ShoppingCart();
            cart.ItemName = "Milk";
            cart.Quantity = 2;
            
            cart.ItemName = "Bread";
            cart.Quantity = 1;

            cart.ItemName = "Eggs";
            cart.Quantity = 3;

            cart.ItemName = "Pie";
            cart.Quantity = 1;
            */

            // creating inventory objects off dictionary
            Inventory testInv = new Inventory();
            foreach(string key in inventoryDict.Keys){
                testInv.Item = key;
                testInv.Price = inventoryDict[key];
            }

            // Printing hashtable of items
            Console.WriteLine("Item Name\tPrice");
            foreach(string key in inventoryDict.Keys){
                Console.WriteLine(String.Format("{0}\t\t${1}", key, inventoryDict[key]));
            }      
        }
    }
}