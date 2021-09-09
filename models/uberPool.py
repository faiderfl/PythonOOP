from models.car import Car

class UberPool(Car):
    brand = str
    model = str

    def __init__(self, id, license,driver,brand, model):
        super().__init__(id=id,license=license,driver=driver)
        self.brand=brand
        self.model=model
