import pyinputplus as pyip

'''
Sandwich Maker
Write a program that asks users for their sandwich preferences. The program should use PyInputPlus to ensure that they enter valid input, such as:

Using inputMenu() for a bread type: wheat, white, or sourdough.
Using inputMenu() for a protein type: chicken, turkey, ham, or tofu.
Using inputYesNo() to ask if they want cheese.
If so, using inputMenu() to ask for a cheese type: cheddar, Swiss, or mozzarella.
Using inputYesNo() to ask if they want mayo, mustard, lettuce, or tomato.
Using inputInt() to ask how many sandwiches they want. Make sure this number is 1 or more.
Come up with prices for each of these options, and have your program display a total cost after the user enters their selection.
TODO - ask if the sandwich is different than the one chosen.
'''

wheatPrice = 3.0
whitePrice = 2.0
sourdoughPrice = 4.0
chickenPrice = 5.0
turkeyPrice = 6.0
hamPrice = 4.0
tofuPrice = 7.0
cheddarPrice = 2.0
swissPrice = 2.5
mozzarellaPrice = 1.5
mayoPrice = 0.5
mustardPrice = 0.5
lettucePrice = 1.0
tomatoPrice = 1.5

sandwichPrice = []
sandwichNumber = 0
sandNum = 1

prompt = 'Hello, whould you like a sandwich?\n'
answer = pyip.inputYesNo(prompt)
if answer == 'no':
  print('Thank you for coming!')
elif answer == 'yes':
  numberAnswer = pyip.inputInt('How many sandwiches would you like?\n', min=1)
  if numberAnswer > 1:
    answer = pyip.inputYesNo('Are all the sandwiches the same?\n')
  #Main Loop
  while sandNum <= numberAnswer:
  #Main choice
    print('Ok! Let\'s choose sandwich number %s'%sandNum)
    breadType = 'What type of bread would you like?\n'
    breadChoice = pyip.inputMenu(['wheat','white','sourdough'],breadType)
    # Type of bread choice
    if breadChoice == 'wheat':
      sandwichPrice.append(wheatPrice)
    elif breadChoice == 'white':
      sandwichPrice.append(whitePrice)
    elif breadChoice == 'sourdough':
      sandwichPrice.append(sourdoughPrice)
    proteinType = 'What type of protein would you like?\n'
    proteinChoice = pyip.inputMenu(['ham','chicken','turkey','tofu'], proteinType)
     #Protein Choice
    if proteinChoice == 'ham':
      sandwichPrice.append(hamPrice)
    elif proteinChoice == 'chicken':
      sandwichPrice.append(chickenPrice)
    elif proteinChoice == 'turkey':
      sandwichPrice.append(turkeyPrice)
    elif proteinChoice == 'tofu':
      sandwichPrice.append(tofuPrice)
    # Main cheese choice
    cheeseQ = 'Would you like to add some cheese?\n'
    cheeseA = pyip.inputYesNo(cheeseQ)    
    if cheeseA == 'yes':
      cheeseType = ('What cheese would you like?\n')
      cheeseChoice = pyip.inputMenu(['cheddar','swiss','mozzarella'],cheeseType)
        #Cheese choice
      if cheeseChoice == 'cheddar':
        sandwichPrice.append(cheddarPrice)
      elif cheeseChoice == 'swiss':
        sandwichPrice.append(swissPrice)
      elif cheeseChoice == 'mozzarella':
        sandwichPrice.append(mozzarellaPrice)
      # Main fillings choice
    fillingQ = 'Would you like mayo, mustard, lettuce or tomato?\n'
    fillingA = pyip.inputYesNo(fillingQ)
    if fillingA == 'yes':
      # fillings choices
      mayoQ = 'Would you like mayo?\n'
      mustardQ = 'Would you like mustard?\n'
      lettuceQ = 'Would you like lettuce?\n'
      tomatoQ = 'Would you like tomato?\n' 
      if pyip.inputYesNo(mayoQ) == 'yes':
        sandwichPrice.append(mayoPrice)
      if pyip.inputYesNo(mustardQ) == 'yes':
        sandwichPrice.append(mustardPrice)
      if pyip.inputYesNo(lettuceQ) == 'yes':
        sandwichPrice.append(lettucePrice)     
      if pyip.inputYesNo(tomatoQ) == 'yes':
        sandwichPrice.append(tomatoPrice)
    # number of sandwiches question
    if answer == 'no':
      sandNum += 1
      continue
    elif answer == 'yes':
      break
sandwichNumber += numberAnswer
totalAmount = sandwichNumber * sum(sandwichPrice)
# total amount the client has to pay.
print('The total amount of your order is %s$ .'%(totalAmount))