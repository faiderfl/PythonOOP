from models.account import Account

class Car:
    id          = int
    license     = str
    driver      = Account(name="",document="")
    passegenger = int

    def __init__(self, id, license, driver):
        self._id = id
        self._license= license
        self.driver = driver
        self.passager = str

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id=value

    def get_license(self):
        return self._license

    def set_license(self, value):
        self._license= value
