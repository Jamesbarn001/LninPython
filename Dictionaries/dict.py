#creating one
animal={'mammal':'lion','Reptile':'Lizard','Amphibian':'Newt','Birds':'Eagle'}
print(animal['mammal'])
print(animal['Reptile'])
print(animal['Amphibian'])

newanimal=animal['Amphibian']
print(f"We just discovered an {newanimal} on the farm")

cars={'Toyota':'Auris','BMW':'X5','Mazda':'Demio','Isuzu':'Hilux'}
print(cars['Mazda'])
print(cars['Isuzu'])
newcar=cars['Isuzu']
print(f"Mem just bought a {newcar} truck"  )

Location={'Meru':'Kiirua',
          'Nairobi':'Kawangware',
          'Uganda':'Kampala',
          'Laikipia':'Nanyuki'
          }
print(Location)
print(Location['Meru'])
newlocation=Location['Nairobi']
print(newlocation)

#Adding key-value pairs
Location['tharaka']='Chuka'
Location['Muranga']='Kabati'
print(Location)

#Starting from an empty list
Country={}
Country['Rwanda']='Kigali'
Country['SouthAfrica']='Johannesberg'
Country['Nigeria']='Abuja'
print(Country)
capcn=Country['Nigeria']
#Modifying values
print(f"The capital city of Nigerai is {capcn}\n")
Country['Nigeria']='Lagos'
capcn1=Country['Nigeria']
print(f"Opps sorry the capital city of Nigeria is actually {capcn1}")

#using get()
Locationval=Location.get('Kirinyaga','no subcounty found')
print(Locationval)