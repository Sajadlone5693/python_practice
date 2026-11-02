def atm_withdrawl(balance,amount,pin):

	if pin == "1234":
	else:
		return 'invalid pin'
		if amount != 0:
			if  amount%500 ==0:


		
				if amount >balance:
					return 'insufficient balance'
				else:
					remaining_balance= balance - amount
					print(remaining_balance)
					if remaining_balance <5000:
						return 'low balance'
					else:
						return'successful'	
pin= input()
amount= int(input('>>>'))
balance= (10000)
print(atm_withdrawl(balance,amount,pin))


