print ('Enter TB or GB for the advertisement unit: ')
unit = input('>')

#calculate the amount that the advertised capacity lies:

if unit == 'TB' or unit == 'tb':
	discrepancy = 1000000000000 / 1099511627776
elif unit == 'GB' or unit == 'gb':
	discrepancy = 1000000000 / 1073741824

print ('enter the advertised capacity:')
advertised_capacity = float(input('>'))
advertised_capacity = float(advertised_capacity)

#Calculate the real capacity, round to the nearest hundredths,,
#and convert it to the str so it can be concatented:

real_capacity = str(round(advertised_capacity*discrepancy,2))

print ('The actual value or capacty is '+ real_capacity+ ''+unit)