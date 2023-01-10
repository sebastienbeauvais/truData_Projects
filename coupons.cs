using System;

# class to apply discount 
class Coupon{
  public static void coupon(string[] args) {
    Hashtable hashTable_coupons = new Hashtable();
    hashTable_coupons.add("10% off", .1);
    hashTable_coupons.add("BOGO", 1);

    foreach (DictionaryEntry, dictionaryEntry in hashTable_coupons){
      Console.WriteLine("{0} -> {1}", dictionaryEntry.Key, dictionaryEntry.Value);
    }
  }
}

# a class that stores key value pairs of an item and their price
class Items{
  public static void items(){
    Hashtable hashTable_items = new Hashtable();
    hashTable_items.add("Milk", 4.99);
    hashtable_items.add("Eggs", 1.99);
    hashTable_items.add("Bread", 3.99);
    hashTable_items.add("Butter", 0.99);

    foreach (DictionaryEntry, dictionaryEntry in hashTable_items){
      Console.WriteLine("{0} -> {1}", dictionaryEntry.Key, dictionaryEntry.Value);
    }
  }
}

# class for cart total
class Basket{
  public static void basket(string[] args){
    Console.WriteLine("Please specify which items you would like to purchase: ");
    list cart = Console.ReadLine();
    
    # rough code
    if (hashTable_items.ContainsKey({user input}))
      Console.WriteLine("Item added to basket.");
      # add item to Checkout
      # next item check
    else:
      Console.WriteLine("Sorry that item doesn't exists.");

    Console.WriteLine("Would you like to enter a coupon? (Y/N): ");

    Console.WriteLine("Coupon Name: ");
    string couponCode = Console.ReadLine()
    if (hashTable_coupons.ContainsKet({couponCode}))
      Console.WriteLine("Successfully added coupon.");
      # update price
    else
      Console.WriteLine("Coupon does not exists.");
  }
}

# class for final pricing
class Checkout{
  public static void Main(string[] args){
    basket();

    Console.WriteLine("Your final price after applying coupons is: " + discountPrice);
  }
}