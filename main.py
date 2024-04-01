import datetime
import random

import functions

# Инициализационный файл

# #Вариант 1
# import module

# # Вариант 2
# import module as m

# # Вариант 3
# from module import func

# Вариант вызова встроенного модуля
# import random

# numbers = [1, 2, 3, 4, 5]
# random.shuffle(numbers)
# print(numbers)

# Вариант 1
my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

def start_project():
  functions.three_songs_time(my_favorite_songs)
  
  print (functions.three_songs_time(my_favorite_songs))

if __name__ == '__main__':
    start_project()