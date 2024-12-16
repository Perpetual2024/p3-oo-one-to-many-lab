class Pet:
    all = []
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    def __init__(self,name,pet_type,owner=None):
        self.name = name
        if pet_type in Pet.PET_TYPES:
            self.pet_type = pet_type
        else:
            raise Exception
        Pet.all.append(self)
        self.pet_type = pet_type
        self.owner = owner

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [ pet for pet in Pet.all if pet.owner == self ]
    
    def add_pet(self, new_pet):
        if isinstance(new_pet, Pet):
            new_pet.owner = self
        else:
            raise Exception("NO")
    
    def get_sorted_pets(self):
        
        my_pets = self.pets()
        
        sorted_pets = sorted( my_pets, key = lambda each_pet: each_pet.name.lower() )
    
        return sorted_pets


