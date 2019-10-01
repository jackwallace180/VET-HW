#disease date pet, vet price

class appointment():
    def __init__(self, injury, date, price, pet = ' ', vet = ' '):
        self.injury = injury
        self.date = date
        self.pet = pet
        self.vet = vet
        self.price = price

    def assign_pet(self, pet):
        self.pet = pet

    def assign_vet(self, vet):
        self.vet = vet