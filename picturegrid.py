#Updated version in the end.

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

for i in grid:
    print(i[0], end='')
print() 

for j in grid:
    print(j[1], end='')
print()

for k in grid:
    print(k[2], end='')
print() 

for l in grid:
    print(l[3], end='')
print()

for m in grid:
    print(m[4], end='')
print() 

for n in grid:
    print(n[5], end='')
print()

#updated the previous code to this one.
#Much simpler and clean.

n = 0
while n < 6:
    for i in grid:
        print(i[n], end='')
    print()
    n += 1