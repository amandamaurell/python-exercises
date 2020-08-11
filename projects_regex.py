import re

numCommasRegex = re.compile(r'''(
	^(\d{1,3})
	((,\d{3})*)?$
	)''', re.VERBOSE)
numCommas = numCommasRegex.findall('333,333')
print(numCommas)


fullNameRegex = re.compile(r'''
	([A-Z]{1}
	\w+
	\s{1}
	Watanabe)
	''', re.VERBOSE)

fullName = fullNameRegex.findall('Haruto Watanabe')

if fullName != []:
	print('The names are the following :')
	print(fullName)
else:
	print('No matches were found')

caseInsensitiveRegex = re.compile(r'''
	((Alice|Bob|Carol)
	\s
	(eats|pets|throws)
	\s
	(apples|cats|baseballs)
	\.)''', re.I | re.VERBOSE)

caseInsensitive = caseInsensitiveRegex.findall('BOB EATS CATS.')
print(caseInsensitive)


#Strong Password Detection

'''Needs to have minimum of 8 characters,
uppercase and lower case letters
and at least one digit'''

passwordLengh = re.compile(r'^[a-zA-Z0-9]{8,}$') # Findsout the lengh of the password.
lowcase = re.compile(r'[a-z]') #finds out if the password has a lowercase letter.
uppercase = re.compile(r'[A-Z]') #finds out if the password has an uppercase letter.
digitPassword = re.compile(r'\d+') #finds out if the password has a digit.

def strongPassword():
	while True:
		password = input()

		if lowcase.findall(password) == None:
			print('You have to enter at least one lower case letter.')
			continue
		if uppercase.findall(password) == None:
			print('You have to enter at least one upper case letter.')
			continue
		if digitPassword.findall(password) == None:
			print('You have to enter at least one digit.')
			continue
		if passwordLengh.findall(password) == None:
			print('You need to type at least 8 characters.')
			continue
		else:
			print('Your Password has been accepted and saved.')
			break


import re, sys

dayRegex = re.compile(r'''(
	(^0[1-9]$)| # from 01 to 09 day
	(^[1-2][0-9]$)| # from 10 to 29
	([3][0-1]) # 30 or 31
	)''', re.VERBOSE)
monthRegex = re.compile(r'''
	(^0[1-9]$)| # from 01 to 09 month
	(^1[0-2]$) # 10, 11 or 12
	''', re.VERBOSE)
yearRegex = re.compile(r'''
	(^[1-2][0-9]{3}$) # from year 1000 to 2999 
	''', re.VERBOSE)
dateFormat = re.compile(r'''
    ((\d\d) #day
    (\/) #separator
    (\d\d) #month
    (\/) #separator
    (\d\d\d\d)) #year
	''', re.VERBOSE)


print(dayRegex.search('31')) 
print(monthRegex.search('04'))
print(yearRegex.search('2999'))
print(dateFormat.findall('25/08/1989'))




def dateCheck():
	while True:
		dateEntry = '25/08/1989'
		if dateFormat.search(dateEntry) == None:
			print('Enter a valid date format. (DD/MM/YYYY)')
			continue
		else:
			for groups in dateFormat.findall(dateEntry):
				day = groups[1]
				month = groups[3]
				year = groups[5]
				if dayRegex.search(day) == None:
					print('Enter a valid day. From 01 to 31.')
					continue
				if monthRegex.search(month) == None:
					print('Enter a valid month. From 01 to 12.')
					continue
				if yearRegex.search(year) == None:
					print('Enter a valid year. From 1000 to 2999.')
					continue
				else:
					print('You have entered a corrert date format :')
					print(dateEntry)
					sys.exit()


dateCheck()



