from typing import Optional
from computer import Computer # From computer import the Computer class

# Defining the resaleshop class
class ResaleShop:

    # The inventory within the resaleshop
    inventory: list = [] # computer objects would go in here

    # The itemID of the computers
    itemID: int = 0
    
    # Set up the constructer
    def __init__(self, inventory, itemID):
        self.inventory = inventory
        self.itemID = itemID

    # Buy a computer
    def buy(self, computer: object):
        self.itemID += 1 # increment itemID
        self.inventory.insert(self.itemID, computer)
        return self.itemID
    
    # Update the price of a computer
    def update_price(self, item_id: int, new_price: int):
        if self.inventory[item_id-1]:
            self.inventory[item_id-1].price = new_price
        else:
            print("Item", item_id, "not found. Cannot update price.")
    
    # Sell a computer
    def sell(self, item_id: int):
        if self.inventory[item_id-1]:
            del self.inventory[item_id-1]
            print("Item", item_id, "sold!")
        else: 
            print("Item", item_id, "not found. Please select another item to sell.")
    
    # Print the inventory of the resaleshop
    def print_inventory(self):
    # If the inventory is not empty
        if self.inventory:
            # For each item
            for item in self.inventory:
                # Print its details
                print(f'Item ID: {self.itemID} : {item}')
        else:
            print("No inventory to display.")
    
    # Refurbish the computer with new_os
    def refurbish(self, item_id: int, new_os: Optional[str] = None):
        if self.inventory[item_id-1]:
            computer = self.inventory[item_id-1] # locate the computer
            if int(computer.year_made) < 2000:
                computer.price = 0 # too old to sell, donation only
            elif int(computer.year_made) < 2012:
                computer.price = 250 # heavily-discounted price on machines 10+ years old
            elif int(computer.year_made) < 2018:
                computer.price = 550 # discounted price on machines 4-to-10 year old machines
            else:
                computer.price = 1000 # recent stuff

            if new_os is not None:
                computer.operating_system = new_os # update details after installing new OS
        else:
            print("Item", item_id, "not found. Please select another item to refurbish.")

def main():

    # A sample to test the above methods.

    # Define a new resaleshop
    resaleshop = ResaleShop(inventory = [], itemID = 0)
    
    # Print a little banner
    print("-" * 21)
    print("COMPUTER RESALE STORE")
    print("-" * 21)

    # Check the inventory in the shop (nothing is in the shop yet)
    resaleshop.print_inventory()
    print()

    # Define a new computer labelled 1
    computer1 = Computer("2019 MacBook Pro","Intel",256,16,"High Sierra",2019,1000)

    # Add it to the resale store's inventory
    print("Buying", computer1.description)
    print("Adding to inventory...")
    computer_id = resaleshop.buy(computer1)
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    resaleshop.print_inventory()
    print("Done.\n")

    # Now, let's refurbish it
    new_OS = "MacOS Monterey"
    print("Refurbishing Item ID:", computer_id, ", updating OS to", new_OS)
    print("Updating inventory...")
    resaleshop.refurbish(computer_id, new_OS)
    print("Done.\n")

    # Also, change the price of it
    new_price = 1200
    print("Updating Item", str(computer_id) + "'s new price:", new_price)
    print("Updating inventory...")
    resaleshop.update_price(computer_id,new_price)
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    resaleshop.print_inventory()
    print("Done.\n")
    
    # Now, let's sell it!
    print("Selling Item ID:", computer_id)
    resaleshop.sell(computer_id)
    
    # Make sure it worked by checking inventory
    print("Checking inventory...")
    resaleshop.print_inventory()
    print("Done.\n")

main()