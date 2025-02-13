from random import randint

print('-Русская рулетка-')
a = int(input("Введите число от 1 до 6: "))
b = randint(1, 6) 

print(f"Случайное число: {b}") 

if a < 1 or a > 6:
    print("Ошибка: введите число от 1 до 6.")
else:
    if a == b:
        print('В вас попали, вы проиграли...')
    else:
        print('Выстрел не задел вас')
