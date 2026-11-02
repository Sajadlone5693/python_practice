import re, pyperclip
text=str(pyperclip.paste())

phone_reg= re.compile(r'''
	(?:[+]\d{1,3}\s)? # optional country code
	\d{3}	#digits
	[-.] 	#seperator
	\d{3}	
	[-.]
	\d{4}
	''',re.VERBOSE)

email_reg= re.compile(r'''
	[\w.]+		#username 
 	@ 			#@ symbol
 	\w+[.]\w+	#domain
 	'''
 	,re.VERBOSE)

emails=email_reg.findall(text)
print(emails)
phone_no=phone_reg.findall(text)
matches=emails+phone_no
copy_matches='\n'.join(matches)
pyperclip.copy(copy_matches)

total_email=len(emails)
total_phone_no= len(phone_no)
print(f"TOTAL EMAILS: {total_email }\nTOTAL PHONE NUMBERS: {total_phone_no}")