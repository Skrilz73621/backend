from random import randint
from decouple import config

def game(attempts, minimal, maximum, capital, rnd):

    while attempts > 0:
        print(f"Кол-во попыток: {attempts}")
        print(f"Ваш капитал: {capital}")
        guess = int(input(f"Угадай число от {minimal} до {maximum}: \n"))
        if guess > rnd:
            print('Загадонное число меньше вашего')
            attempts -= 1
            print(f'У вас осталось попыток: {attempts}')

        elif guess < rnd:
            print('Загаданное число больше вашего')
            attempts -= 1
            print(f'У вас осталось попыток: {attempts}')

        elif attempts == 0:
            print(f'Игра окончена вы все програли')
            break

        elif guess == rnd:
            print(f'Вы угадали число {rnd}!')
            print(f'Ваш капитал повышен до {capital * 2}')
            capital *= 2
            keep_going = int(input('Хотите удвоить свой капитал?\nЕсли-да нажмите-1\nЕсли-нет нажмите-2\n'))
            if keep_going == 1:
                attempts = config('AMOUNT_OF_ATTEMPTS', cast=int)
                rnd = randint(minimal, maximum)
            else:
                print(f'Ваш выйгрыш составляет {capital}')
                break


