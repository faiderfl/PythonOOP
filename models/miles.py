class Miles:
    def __init__(self):
        self._distance = 0

    def convert_to_kilometers(self):
        return (self._distance*1.609344)

    @property
    def distance(self):
        return self._distance

    @distance.setter
    def distance(self,distance):
        if distance <= 0:
            raise ValueError("distance must be greater than zero")
        else:
            self._distance = distance