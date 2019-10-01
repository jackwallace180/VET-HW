# specialization

from Humans import *

class vet(Human):
    def __init__(self, name, phone, email, injury):
        super().__init__(name, phone, email)
        self.injury = injury
