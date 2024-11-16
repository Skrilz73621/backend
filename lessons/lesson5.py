from random import randint as rnd, choice as select_random_element
from utilites.template import Person
from termcolor import cprint
# import emoji
from decouple import config


print(select_random_element([1,2,3]))
print(rnd(1,10))
friend  = Person('Jim', 18)
print(friend)

cprint('Hello world', 'white', 'on_magenta')
# print(emoji.emojize('Python is :thumbs_up:'))

print(config('SECRET_KEY'))
commented = config('COMMENTED', default=0, cast = int)
print(commented * 2)