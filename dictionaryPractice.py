import pprint

all_guests = {'Alice': {'apples': 5, 'pretzels': 12},
              'Bob': {'ham sandwiches': 3, 'apples': 2},
              'Carol': {'cups': 3, 'apple pies': 1}}

def total_brought(guests, item):
    num_brought = 0
    for k, v in guests.items():
    	num_brought = num_brought + v.get(item, 0)
    return num_brought

print('Number of things being brought:')
print(' - Apples         ' + str(total_brought(all_guests, 'apples')))
print(' - Cups           ' + str(total_brought(all_guests, 'cups')))
print(' - Cakes          ' + str(total_brought(all_guests, 'cakes')))
print(' - Ham Sandwiches ' + str(total_brought(all_guests, 'ham sandwiches')))
print(' - Apple Pies     ' + str(total_brought(all_guests, 'apple pies')))

for k, v in all_guests.items():
	print(k ,':', v )

pprint.pprint(all_guests)






# message='a quick brown fox jumped over the lazy dog'
# count={}

# for character in message:
# 	count.setdefault(character,0)
# 	count[character]=count[character]+1
# for character in sorted(count):
# 	print(character +':'+str(count[character]), end=' ')





# # birthdays={'sajad':'29 Dec','mariya':'12 Sep',}
# # print('enter a name:(Blank to quit)')
# # name =input().lower()

# # print(name+'s birthday is '+ str(birthdays.get(name,'unknown')))





# # while True:
# # 	print('enter a name:(Blank to quit)')
# # 	name =input().lower()
# # 	if name =='':
# # 		break
# # 	if name in birthdays:
# # 		print(birthdays[name]+ ' is the birthday of '+ name.capitalize())
# # 	else:
# # 		print('i dont have the birthday for '+ name.capitalize())
# # 		print('what is their birthday?')
# # 		bday=input()
# # 		birthdays[name]=bday
# # 		print('Birthday database updated.')
# # # print(birthdays)
# # # for k in birthdays.items():
# # # 	print(k)