import time
import sys

def sing(lyrics, delay, pause):
  time.sleep(pause)
  for i in lyrics:
    time.sleep(delay)
    sys.stdout.write(i)
    sys.stdout.flush()
  print()
def lyrics():
  
  lyric = ["I don't think that you even realize",
           "The joy you make me feel when I'm inside ",
           "your universe",
           "You hold me like I'm the one who's precious",
           "I hate to break it to you, but it's just the other way around",
           "You can thank your stars all you want",
           "But I'll always be the lucky one",
           ":)"]
  time = [2.6,3,1,2.2,3.5,2.8,4,0.01]
  pause = [4,0.2,0.9,3.4,0.1,3.,0.01,4.8]

  for i in range(len(lyric)):
    sing(lyric[i], time[i]/len(lyric[i]), pause[i])

choice = input("would you like to run the program?(y/n):")
if choice == "y":
  lyrics()

else:
  exit()
