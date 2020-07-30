import sys
def collatz(number):
  if number % 2 == 0:
    return number//2
  else:
    return 3*number+1

try:
  number = int(input())
  while True:
   collatz(number)
   if collatz(number) > 1:
     print(collatz(number))
     number = collatz(number)
     if collatz(number) == 1 :
       print(collatz(number))
       break

except:
  print("Please, enter an integer number!")
  