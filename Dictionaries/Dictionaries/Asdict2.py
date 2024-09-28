Glossary={'comments':'Words that are used to describe what a section of code is supposed to do\n',
          'Dictionary':'Refers to a collection of key-value pairs\n',
          'Lists':'Refers to a storage space of data \n',
          'indentation':'Refers to number of spaces one jumps from the end of the editor especially when using a for loop\n',
           'github':'A open-version space used to store coding projects\n',
          'visual studio code':'An editor used to edit pieces of code\n',
          'git bash':'A commandline used to run git commands locally on the pc\n',
          'repository':' A storage space for written codes both locally on the pc and on the cloud.\n'}
for word,definition in Glossary.items():
   print(f"{word.title()}: {definition.title()}")

#Question 2
Rivers={'Nile':'Egypt','Niger':'Niger','Tana':'Kenya'}
for river,country in Rivers.items():
   print(f" The river {river.title()} is found in {country.title()}")

for river in Rivers.keys():
   print(river)

for country in Rivers.values():
   print(country)

#Question 3
favLanguages={'Jen':'python',
             'King':'python',
             'Leah':'java',
             'Clara':'java',
             'Jaden':'html\n'}

people=['Ken','Willis','Bruce','clara','jen','king']
people1=[name.lower() for name in favLanguages.keys()]
print(people1)
for name in people:
 
   if  name  in favLanguages.keys() and people1:
    print(f"Hello {name.title()},thank you for taking the poll.")
   else:
    print(f"Hello {name.title()}, please take the poll.")
   