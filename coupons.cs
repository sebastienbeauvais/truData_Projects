using System.Collections;

namespace ArchitectureProgram
{
    public class Coupon{
        // Maybe use a hashtable with pre-defined coupons??
        public string? Name;
        public float Discount;
    }

    public class Item{

    }

    class Program{
        public static void Main(string[] args){

            Hashtable itemTable = new Hashtable();
            itemTable.Add("Milk", 3.99f);
            itemTable.Add("Eggs", 5.99f);
            itemTable.Add("Bread", 2.99f);
            itemTable.Add("Butter", 1.99f);

            Hashtable couponTable = new Hashtable();
            couponTable.Add("10%", 0.1f);
            couponTable.Add("25%", 0.25f);
            couponTable.Add("BOGO", 0.5f);
            

            Coupon coupon = new Coupon();
            coupon.Name = "10% off cart total";
            coupon.Discount = 0.1f;

            // Printing hashtable of items
            foreach(string key in itemTable.Keys){
                Console.WriteLine(String.Format("{0}: {1}", key, itemTable[key]));
            }
            
            // Getting customer shopping list
            List<string> shoppingList = new List<string>();

            Console.WriteLine("Enter your shopping list: ");
            string input = Console.ReadLine();
            shoppingList.Add(input);
            
            
            while (input != ""){
                Console.WriteLine("Please enter another item: ");
                input = Console.ReadLine();
                shoppingList.Add(input);
            }
            if (input == ""){
                foreach(string key in shoppingList){
                    Console.WriteLine(key + " was added to the shopping list.");
                }
            }            
        }
    }
}