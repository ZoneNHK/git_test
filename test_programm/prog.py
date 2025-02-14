from colorama import Fore, Style
class Vechicle:
    """Класс по транспорту"""
    transport = []
    def __init__(self, brand, weight, speed):
        self.br = brand
        self.wh = weight
        self.sd = speed 
        Vechicle.transport.append(self)
    
    @classmethod
    def set_transport(cls):
        n = int(input('Какое кол-во транспорта вы хотите внести? : '))
        tr = []
        for _ in range(n):
            brand = input('-Бренд: ')
            weight = float(input('-Вес в кг:'))
            speed= float(input('Скорость в км/ч: '))
            transport = Vechicle(brand, weight, speed)
            print(Fore.BLUE + '-' * 25 + Style.RESET_ALL)
        return cls.transport

    def get_transport(self):
        print('-' * 25)
        for tr in Vechicle.transport:
            print(Fore.GREEN+
                f'-Бренд: {tr.br}',
                f'\n-Вес: {tr.wh}',
                f'\nСкорость: {tr.sd}' 
                + Style.RESET_ALL)
            print('-' * 25)
            
class Car(Vechicle):
    """Дочерный класс Car, наследующий поля с класса Vechicle"""
    cars = []
    def __init__(self, brand, weight, speed, num_doors):
        super().__init__(brand, weight, speed)
        self.nd = num_doors
        Car.cars.append(self)
    
    @classmethod
    def set_car(cls):
        n = int(input('Какое кол-ов машин вы хотите занести? : '))
        print(Fore.BLUE + '-' * 25 + Style.RESET_ALL)
        for _ in range(n):
            brand = input('-Бренд: ')
            weight = float(input('-Вес в кг: '))
            speed = float(input('-Скорость в км/ч: '))
            num_doors = int(input('-Количество дверей в машине: '))
            cars = Car(brand, weight, speed, num_doors)
            print(Fore.BLUE + '-' * 25 + Style.RESET_ALL)

    def get_car(self):
        print('-' * 25)
        for car in Car.cars:
            print(
            Fore.GREEN+
            f'-Бренд: {car.br}',
            f'\n-Вес: {car.wh}',
            f'\nСкорость: {car.sd}',
            f'\nКол-во дверей: {car.nd}' 
             + Style.RESET_ALL
            )
            print('-' * 25)

        
transports = Vechicle("Mercedes-Benz", 1520, 352)
print(Fore.BLUE + f'Документация: {transports.__doc__}' + Style.RESET_ALL)
# transports.set_transport()
transports.get_transport()

car = Car("LADA Granta", 1560, 179, 4)
print(Fore.BLUE + f'Документация: {car.__doc__}')
car.set_car()
car.get_car()