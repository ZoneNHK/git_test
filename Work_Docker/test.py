print('Работа с программой Docker')
from colorama import Fore, Style
class Test:
    """Тестовый класс для программы Docker"""
    people = []
    def __init__(self, id, surname, name, sex, age):
        self.id = id 
        self.sn = surname
        self.nm = name 
        self.sx = sex
        self.ag = age
        Test.people.append(self)
    
    @classmethod
    def set_people(cls):
        n = int(input("Введите желаемое кол-во людей для добавления: \n- "))
        print('-' * 35)
        for i in range(n):
            id = i + 1
            surname = input('-Фамилия: ')
            name = input('-Имя: ')
            sex = input('-Пол: ')
            age = int(input('-Возраст: '))
            cls(id, surname, name, sex, age)
            print('-' * 35)

    def get_people(self):
        print('\nИнформация о людях:')
        print('-' * 35)
        for p in self.people:
            print(Fore.GREEN +
                f'Номер: {p.id}\n',
                f'Фамилия: {p.sn}\n',
                f'Имя: {p.nm}\n',
                f'Пол: {p.sx}\n',
                f'Возраст: {p.ag}\n'
                + Style.RESET_ALL
            )
            print('-' * 35)

test = Test(1, 'Иванов', 'Иван', 'мужской', 20)
print(Fore.BLUE + f'Документация: {test.__doc__}' + Style.RESET_ALL)
test.set_people()
test.get_people()