def display_inventory(inventory):
    print('inventory:')
    item_count=0
    for k ,v in inventory.items():
        print(v ,k)
        item_count+=v
    print('Total number of items:',item_count)

inventory={'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} 
# display_inventory(inventory)
def add_to_inventory(inventory, added_items):
    for v in added_items:
        inventory.setdefault(v,0)
        inventory[v]+=1
    return inventory 
inv = {'gold coin': 42, 'rope': 1}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(inv, dragon_loot)
display_inventory(inv)
