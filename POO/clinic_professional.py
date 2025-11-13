from i_clinic import Clinic
class ProfessionalClinic(Clinic):
    """This class represents the behavior of an emergency clinic,"""

    def __init__ (self, nurse, medical ):
        self.nurse = nurse
        self.medical = medical

    def recovery(self, pokemon_type:str) -> int:
        recovery_value = 10
        if (pokemon_type == "plant"):
            recovery_value = 15
        return recovery_value
    
    def vaccunate(self, pokemon_age:int) -> bool:
        return True