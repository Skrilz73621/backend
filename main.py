from decouple import config
from random import randint
from logic import game

attempts = config('AMOUNT_OF_ATTEMPTS', cast=int)
capital = config('FIRST_CAPITAL', cast=int)
minimal = config('MINIMAL_NUMBER', cast=int)
maximum = config('MAXIMUM_NUMBER', cast=int)
rnd = randint(minimal, maximum)

game(attempts, minimal, maximum, capital, rnd)