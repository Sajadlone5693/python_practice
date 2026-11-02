import random



cat_names=[]
while True:
	print('enter the name of cat'+ str(len(cat_names)+1)  +'(or enter nothing to stop the code):')
	name =input()

	if name =='':
		break
	cat_names= cat_names+[name]
print('the cats names are:')
for name in cat_names:
	print('  '+name)

random.shuffle(cat_names)

print(cat_names)
print(random.choice(cat_names))




# for index,item in enumerate(cat_names):
# 	print('index ' + str(index) + ' in cat_names is: ' + item)
# # print('enter a pets name:')
# # name=input()
# # if name not in cat_names:
# 	print('i dont have pet named ', name)
# else:
# 	print(name+' is my pet')
