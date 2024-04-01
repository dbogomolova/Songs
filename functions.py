import datetime
import random

def three_songs_time(songs):
  three_songs = datetime.timedelta()
  for spisok in random.choices(songs, k=3):
    r = str(spisok[1]).split('.')
    dataobject = datetime.timedelta(minutes=int(r[0]), seconds=int(r[1]))
    three_songs+=dataobject
  return three_songs