def display_inventory(inventory):
	print('inventory:')
	item_count=0
	for k ,v in inventory.items():
		print(v ,k)
		item_count+=v
	print('Total number of items:',item_count)

inventory={'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} 
display_inventory(inventory)