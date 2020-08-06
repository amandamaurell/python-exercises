listOfNames = [['apples','oranges','cherries','banana'],['Alice','Bob','Carol','David'],['dogs', 'cats','moose', 'goose']]

def printTable(tableData):
  colWidth = [0]*len(tableData)
  for i in range(len(tableData)):
    for j in range(len(tableData[i])):
      if len(tableData[i][j]) > colWidth[i]:
        colWidth[i] = len(tableData[i][j])


  for x in range(len(tableData[0])):
    for i in range(len(tableData)):
      print(tableData[i][x].ljust(colWidth[i]), end=' ')
    print()

printTable(listOfNames)