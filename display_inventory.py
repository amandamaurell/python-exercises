def displayInventory(inventory):
  print("Inventory:".center(20,'-'))
  item_total = 0
  for k, v in inventory.items():
    print( str(k.ljust(12,'.')) + ':' + str(v).rjust(7))
    item_total = item_total + v
  print( 'The total of items is : ' + str(item_total))


def addToInventory(inventory, addedItems):
  for i in addedItems:
    if i not in inventory.keys():
      inventory[i] = 1
    else:
      inventory[i] += 1
  return inventory


inv1 = {'gold coin' : 42, 'rope' : 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

inv1 = addToInventory(inv1, dragonLoot)

displayInventory(inv1)
