import copy

# função que jogará cara ou coroa 100 vezes e guardará em uma lista
def cointoss(coin):
  import random
  while len(coin) < 101:
    c = random.randint(0,1)
    if c == 0:
      coin.append('H')
    else:
      coin.append('T')    
  return coin


def numOfStreaks(cointoss2):
  tosses = []
  cointoss(tosses)
  # parte do programa que conta quantas vezes repetiu H e T.
  countH = 0
  countT = 0
  for i in tosses:
    if i == 'H':
      countT=0
      countH += 1
      if countH == 6:
        cointoss2 += 1
        countH=0
    elif i == 'T':
      countH=0
      countT +=1
      if countT == 6:
        cointoss2 += 1
        countT=0
  return cointoss2

streaks = 0
n = 1000

for i in range(n):

  streaks += numOfStreaks(streaks)

# ainda não tenho ctz se este é o caminho para conseguir a %
streaks2 = streaks/n

# % de vezes que saiu 6 caras ou 6 coroas
print('Chance of streak: %s%%' % (streaks2 / 100))
