inventory = {
  'gold' : 500,
  'pouch' : ['flint', 'twine', 'gemstone'],
  'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}
# 1 thêm vs list
inventory['pocket'] = ['seashell', 'strange berry','lint']
print(inventory['pocket'])
# 2
inventory['backpack'].remove('dagger') # ngoặc tròn là vì
print(inventory['backpack'])
# 3  chinh gold len 50
inventory['gold'] += 50
print(inventory['gold'])
