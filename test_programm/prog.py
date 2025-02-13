from functools import wraps
import random

def func(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        lst = func(*args, **kwargs)
        print(f'Элементы списка: {lst}')
        print(f'Длина списка: {len(lst)}')
        print(f'Наибольший элемент: {max(lst)}')
        print(f'Наименьший элемент: {min(lst)}')
        average = round(sum(lst) / len(lst),2)
        print(f'Среднее арифметическое по списку: {average}')
        return lst 
    return wrapper

@func        
def take_date():
    n = int(input('Введите кол-во элементов в списке: \n- '))
    a = float(input('Введите начало диапазона: \n- '))
    b = float(input('Введите конец диапазона: \n- '))
    lst = [round(random.uniform(a, b),2) for _ in range(n)]
    return lst

# take_date()


class College:
    def __init__(self, id, name, surname, subject, aver_ball):
        self.id = id
        self.name = name
        self.sur = surname
        self.sub = subject
        self.ab = aver_ball
    
    def set_stud(self):
        n = int(input("Какое кол-во студентов вы хотите ввести? \n- "))
        studs = []
        for i in range(n):
            id = i + 1
            surname = input("-фамилия: ")
            name = input("-имя: ")
            subject = input("-предмет: ")
            aver_ball = float(input("-средний балл: "))
            print("-"*25)
            stud = College(id, name, surname, subject, aver_ball)
            studs.append(stud)
        return studs
    
    def get_stud(self, studs):
        print('Информация о студентах:\n')
        print("-"*25)
        for stud in studs:
            print(
                f'\n-номер: {stud.id}',
                f'\n-фамилия: {stud.sur}',
                f'\n-имя: {stud.name}',
                f'\n-предмет: {stud.sub}',
                f'\n-средний балл: {stud.ab}'
            )
            print("-"*25)

stud = College(0, "", "", "", 0.0)
lst = stud.set_stud()
stud.get_stud(lst)


class College:
    all_students = []  # Статический атрибут для хранения всех студентов

    def __init__(self, id, name, surname, subject, aver_ball):
        self.id = id
        self.name = name
        self.sur = surname
        self.sub = subject
        self.ab = aver_ball
        College.all_students.append(self)  # Добавляем студента в общий список

    @classmethod
    def get_stud(cls):
        print('Информация о студентах:\n')
        print("-" * 25)
        for stud in cls.all_students:  # Используем cls для обращения к статическому атрибуту
            print(
                f'\n-номер: {stud.id}',
                f'\n-фамилия: {stud.sur}',
                f'\n-имя: {stud.name}',
                f'\n-предмет: {stud.sub}',
                f'\n-средний балл: {stud.ab}'
            )
            print("-" * 25)

class Graduate(College):  # Graduate наследует от College
    def __init__(self, id, name, surname, subject, aver_ball, thesis_title):
        super().__init__(id, name, surname, subject, aver_ball)  # Вызов конструктора родительского класса
        self.thesis_title = thesis_title  # Новая функция для аспирантов
        print(f'Аспирант {name} добавлен.')

    @classmethod
    def get_graduates(cls):
        print('Информация об аспирантах:\n')
        print("-" * 25)
        for stud in cls.all_students:  # Используем cls для обращения к статическому атрибуту
            if isinstance(stud, Graduate):  # Проверяем, является ли студент аспирантом
                print(
                    f'\n-номер: {stud.id}',
                    f'\n-фамилия: {stud.sur}',
                    f'\n-имя: {stud.name}',
                    f'\n-предмет: {stud.sub}',
                    f'\n-средний балл: {stud.ab}',
                    f'\n-тема диссертации: {stud.thesis_title}'  # Проверка на тему диссертации
                )
                print("-" * 25)

# Создаем студентов
stud1 = College(1, "Alice", "Smith", "Mathematics", 4.5)
stud2 = College(2, "Bob", "Jones", "Physics", 4.0)

# Создаем аспирантов
grad1 = Graduate(3, "Charlie", "Brown", "Biology", 4.8, "Genetic Engineering")
grad2 = Graduate(4, "Diana", "Prince", "Chemistry", 4.7, "Quantum Chemistry")

# Получаем информацию о всех студентах
College.get_stud()

# Получаем информацию только об аспирантах
Graduate.get_graduates()