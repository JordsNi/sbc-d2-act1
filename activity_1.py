#sir daryll
'''
print('Spam eggs')
print("Beef Loaf")
print('42')
print('don\'cha')
q = 'Manok with\nConditioner'
print(q)
print('"GYATT!!" Aljieo said calmly.')
print(r"/name/some/ni")
w = 5 * 'ni' + 'nja '
print(w)
'''

#index
'''
text = "BUNI Jords"
print(text[2])

words = input("words: ")
print(words[])
print(len(words))
'''

#Slicing
'''
texts = "Wello Horld"
print(texts[2])
print(texts[-4])
print(texts[-8:-6])
print(texts[0:2], texts[6:8])
print(f"{texts[0:2]} {texts[6:8]}")
'''

#string methods
'''
hords = "Jords"
print(hords.upper())
print(hords.lower())
print(hords.capitalize())
print(hords.replace("J", "G"))
print(hords.isalpha())
print(hords.isnumeric())
print(hords.isalnum())
'''


wordings = "summer bootcamp"
           #01234567891011121314
print(wordings.title())
print(wordings[0:6].capitalize(), wordings[7:14]+wordings[-1].upper())
print(wordings[7:11].replace("b", "L"))
print(wordings[11:].replace("p", "E"))
print(wordings[4:6].replace("e", "a").upper())
print(wordings.replace(" ", "").isalpha())
