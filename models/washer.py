class Washer:

    def __init__(self):
        # TODO
        pass

    def wash(self, temperature='hot'):
        """Wash the water tank .

        Args:
            temperature (str, optional): [description]. Defaults to 'hot'.
        """
        self._fill_water_tank(temperature)
        self._add_soap()
        self._wash()
        self._centrifuge()

    def _fill_water_tank(self, temperature):

        print(f'Filling the water tank with {temperature} water')

    def _add_soap(self):
        print('Adding Soap')

    def _wash(self):
        print('Washing')

    def _centrifuge(self):
        print('Centrifuging')
