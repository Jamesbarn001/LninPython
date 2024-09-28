info={'1stname':'Arthur\n','2ndname':'kijito\n','age':'20\n','city':'Nairobi\n',}
print("This is the personal info of the new student:")
print(info['1stname'])
print(info['2ndname'])
print(info['age'])
print(info['city'])

favnum={'Mary':'22\n','John':'21\n','King':'23\n','prince':'32\n'}
print(favnum['John'])
print(favnum['Mary'])
print(favnum['King'])
print(favnum['prince'])

glossary={'comments':'Words that are used to describe what a section of code is supposed to do\n',
          'Dictionary':'Refers to a collection of key-value pairs\n',
          'Lists':'Refers to a storage space of data \n',
          'indentation':'Refers to number of spaces one jumps from the end of the editor especially when using a for loop\n'
          }
for word,definition in glossary.items():
    print(f"{word.title()}:  {definition.title()}")

favnum={'Mary':'22\n','John':'21\n','King':'23\n','prince':'32\n'}
for name,numbers in favnum.items():
    print(f"{name.title()} : {numbers}")

info={'1stname':'Arthur\n','2ndname':'kijito\n','age':'20\n','city':'Nairobi\n',}
for prov,data in info.items():
    print(f"{prov.title()} : {data.upper()}")

#.keys() method
favLanguages={'Jen':'python','King':'c','Leah':'Java','Clara':'Css','Jade':'html'}

friends=['King','Leah']
for name in favLanguages.keys():
    print(name.title())
    
    if name in friends:
      language=favLanguages[name].title()
      print(f"{name.title()}, I see your fav language is : {language.title()}\n")

if 'erin' not in favLanguages.keys():
    print("Erin,Please fill in the poll\n")

#Looping thru in a certain order
for name in sorted(favLanguages.keys()):
    print(f"{name.title()},Thank you for participating in the poll\n")



#To avoid repetition
favLanguages={'Jen':'python','King':'python','Leah':'java','Clara':'java','Jade':'html\n'}
for language in set(favLanguages.values()):
    print(language)


for language in favLanguages.values():
    print(language)
