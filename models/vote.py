class Vote:
    def __init__(self,id,allow_regions):
        self._id= id
        self._allow_regions= allow_regions
        self._region= None

    @property
    def region(self):
        return self._region
    @region.setter
    def region(self,region):
        if region in self._allow_regions:
            self._region= region
        else:
            raise ValueError(f'Region {region} is not allowed')

    @property
    def id(self):
        return self._id