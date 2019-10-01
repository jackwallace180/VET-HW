# payment

from Humans import *

class owner(Human):
    def __init__(self, name, phone, email, pay):
        super().__init__(name, phone, email)
        self.pay = pay

    def owner_details(self):
        owner_details = {
            'name': self.name,
            'phone': self.phone,
            'email': self.email,
            'payment': self.pay,

            }
        return owner_details