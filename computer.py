# Defining the computer class
class Computer:

    # Setting the attributes of a computer
    # The description of a computer
    description: str

    # The processor_typr of a computer
    processor_type: str

    # The hard_drive_capacity of a computer
    hard_drive_capacity: int

    # The memory of a computer
    memory: int

    # The operating_system of a computer
    operating_system: str

    # The year_made of a computer
    year_made: int

    # The price of a computer
    price: int

    # Set up the constructer
    def __init__(self, description, processor_type, hard_drive_capacity, memory, operating_system, year_made, price):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price
    
    # What methods will you need?

'''
# Set up different computers
def main():
    computer1 = Computer("Mac Pro (Late 2013)","3.5 GHc 6-Core Intel Xeon E5",1024,64,"macOS Big Sur",2013,1500)
    print(computer1.price)

if __name__ == "__main__":
    main()
'''