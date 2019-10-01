# name breed owner
class pet():
    def __init__(self, name, breed, owner = ' '):
        self.name = name
        self.breed = breed
        self.owner = owner


    def pet_details(self):
        pet_details = {
            'name' : self.name,
            'breed' : self.breed,
            'owner' : self.owner.name
        }
        return pet_details