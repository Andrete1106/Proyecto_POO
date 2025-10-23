"""Author: Andres David Hincapie Alvarez <<anhincapiea@unal.edu.co>> """
Blessd = "Daniel"
print(Blessd)
class Computer:
    """Represent a Laptop"""
    def __init__(self,brand,processor,ram,hd_space,operative_system,graphic_card,power_supply,mother_board,coling_system,case):
        """Constructor of the class"""
        self.brand = brand
        self.processor = processor
        self.ram = ram
        self.hd_space = hd_space
        self.operative_system = operative_system
        self.graphic_card = graphic_card
        self.power_supply = power_supply
        self.mother_board = mother_board
        self.coling_system = coling_system
        self.case = case

    def specs(self):
        print( f"I am a computer of brand {self.brand} \ 
                I have a processor {self.processor}, {self.ram} GB of RAM, \ 
                {self.hd_space} HDD capacity, and a {self.operative_system} OS")