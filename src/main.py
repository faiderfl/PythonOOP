from models.account import Account
from models.car import Car
from models.coordinate import Coordinate
from models.person import Person
from models.uberX import UberX
from models.washer import Washer
from models.miles import Miles
from models.vote import Vote

if __name__ == '__main__':
    print('Start')
    faider= Person('Faider', 'Test')
    pedro = Person('Pedro', 'Test')
    print(faider.name)
    print(faider.saluda(pedro))

    driver= Account("1",'Juan')
    car= Car(id=1, license='123', driver=driver)
    uberX= UberX(id=1, license='123', driver=driver, brand='Toyota', model='2021' )
    uberX.set_license('456')
    print(vars(uberX))

    coordinate_1= Coordinate(3,30)
    coordinate_2= Coordinate(4,8)
    print(coordinate_1.distance(coordinate_2))
    print(isinstance(coordinate_1, Coordinate))

    washer = Washer()
    washer.wash()

    try:
        miles= Miles()
        miles.distance=-1
    except Exception as e:
        print(e)
    print(miles.convert_to_kilometers())

    try:
        vote= Vote(123,['Medellin','Bogota'])
        print(vote.region)
        vote.region= 'Medellin2'
        print(vote.region)
    except Exception as e:
        print(e)