class Automobile:
    def __init__(self, model, brand, color):
        self.model = model
        self.brand = brand
        self.color = color
        self._status= 'iddle'
        self._motor= None

    def accelarate(self, type='slow'):
        if type == 'fast':
            self._motor.injects_gas(10)
        else:
            self._motor.injects_gas(3)
        self._status='move'



class Engine:
    def __init__(self,cilinders, type='gas'):
        self.cilinders =cilinders
        self.tipo = type
        self._temperature= 0

    def  injects_gas(self,quantity):
        #TODO
        pass