from models.car import Car

class UberVan(Car):
    type_card_accepted = []
    seats_material = []

    def __init__(self, id, license,driver,type_card_accepted, seats_material):
        super().__init__(id=id,license=license,driver=driver)
        self.type_card_accepted=type_card_accepted
        self.seats_material=seats_material
