import random, sys

print('ROCK, PAPER, SCISSORS')

wins = 0
losses = 0
ties = 0


while True:
  print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
  while True:
    print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
    move = input()
    if move == 'q':
      sys.exit()
    if move == 'r' or move == 'p' or move == 's':
      break
    print('Type one of r, p, s, or q.')


  if move == 'r':
    print('ROCK versus...')
  elif move == 'p':
    print('PAPER versus...')
  elif move == 's':
    print('SCISSORS versus...')


  randomNumber = random.randint(1,3)

  if randomNumber == 1:
    pcmove = 'r'
    print('ROCK')
  elif randomNumber == 2:
    pcmove = 'p'
    print('PAPER')
  elif randomNumber == 3:
    pcmove = 's'
    print('SCISSORS')
  
  if pcmove == move :
    print('It´s a tie!')
    ties = ties + 1
  elif move == 'r' and pcmove == 's':
    print('You win!')
    wins = wins + 1
  elif move == 's' and pcmove == 'p':
    print('You win!')
    wins = wins + 1
  elif move == 'p' and pcmove == 'r':
    print('You win!')
    wins = wins + 1
  elif pcmove == 'r' and move == 's':
    print('You Lose!')
    losses = losses + 1
  elif pcmove == 's' and move == 'p':
    print('You Lose!')
    losses = losses + 1
  elif pcmove == 'p' and move == 'r':
    print('You Lose!')
    losses = losses + 1
