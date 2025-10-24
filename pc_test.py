class Computer:
    """Represent a Laptop"""
    def __init__(self, brand, processor, ram, hd_space, operative_system, graphic_card, power_supply, mother_board, cooling_system, case):
        self.brand = brand
        self.processor = processor
        self.ram = ram
        self.hd_space = hd_space
        self.operative_system = operative_system
        self.graphic_card = graphic_card
        self.power_supply = power_supply
        self.mother_board = mother_board
        self.cooling_system = cooling_system
        self.case = case

    def specs(self):
        print(
            f"I am a computer of brand {self.brand}.\n"
            f"I have a processor {self.processor}, {self.ram} GB of RAM, {self.hd_space} HDD capacity, and a {self.operative_system} OS.\n"
            f"A {self.graphic_card} Graphic card, {self.power_supply} Power Supply, {self.mother_board} mother board, {self.cooling_system} cooling system and a {self.case} case."
        )