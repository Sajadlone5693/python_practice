print('Enter the English message to translate into pig latin:')
message = input()

VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')

pig_latin = []

for word in message.split():
    non_alpha = ''
    while len(word) > 0 and not word[0].isalpha():
        non_alpha=non_alpha+word[0]
        word=word[1:]
    # print(non_alpha)
    if len(word)==0:
        pig_latin.append(non_alpha)
        continue
    # print(pig_latin)
    word_endings=''
    while not word[-1].isalpha():
        word_endings=word[-1]+word_endings
        word=word[:-1]
    # print(word_endings)
    was_upper=word.isupper()
    was_title=word.istitle()
    word= word.lower()
    pre_cons=''
    while len(word) > 0 and word[0] not in VOWELS:
        pre_cons+=word[0]
        word=word[1:]
    if len(pre_cons)==0:
        word+='yay'
    else:
        word=word+pre_cons+'ay'
    if was_upper is True:
        word=word.upper()
    if was_title is True:
        word=word.title()

    pig_latin.append(non_alpha+word+word_endings)
print(' '.join(pig_latin))