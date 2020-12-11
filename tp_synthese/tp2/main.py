from personne import Personne
from adresse import Adresse
from listePersonnes import ListPersonnes


print("######### Adresses creation ################## \n\n")
adr1 = Adresse("93100","lenain de tillemont","Montreuil")
adr2 = Adresse("75000","Champs","Paris")
adr3 = Adresse("93200", "guynemer" , "ST Denis")
adr4 = Adresse("93200", "40 guynemer" , "ST Denis")

print("######### Persons creation ################## \n\n")

personne1 = Personne("Zakaria","M")
personne2 = Personne("Name 2","F")
personne3 = Personne("Name 3","F")
personne4 = Personne("Name 4","M")
personne5 = Personne("Name 5","M")

print("######### Link adress to persons ################## \n\n")


personne1.add_adress(adr1)
personne2.add_adress(adr2)
personne3.add_adress(adr3)
personne4.add_adress(adr4)
personne5.add_adress(adr4)

print("######### Print the list of the person ################## \n\n")

listePersonnes1 = ListPersonnes()
listePersonnes1.addPersonne(personne1)
listePersonnes1.addPersonne(personne2)
listePersonnes1.addPersonne(personne5)

print("######### Modify a city of a selected person ################## \n\n")

listePersonnes1.edit_personne_ville("Zakaria","London")
print(listePersonnes1)


print("######### Modify a person  name of a selected person ################## \n\n")


listePersonnes1.edit_personne_nom("Name 3","Zikos")
print(listePersonnes1)

print("######### number of cities of a selected city ################## \n\n")

number = listePersonnes1.count_personne_ville('Montreuil')
print("Montreuil =>>"+ str(number))

number = listePersonnes1.count_personne_ville('ST Denis')
print("ST Denis =>>"+ str(number))


print("######### Searchig if a zip code exists ################## \n\n")

print("93100 ==> " + str(listePersonnes1.exists_code_postal("93100")))
print("75100 ==> " + str(listePersonnes1.exists_code_postal("75100")))
print("93200 ==> " + str(listePersonnes1.exists_code_postal("93200")))


print("######### Searchig if a specific name exists  ################## \n\n")

print("Zakaria ==> " + str(listePersonnes1.find_by_nom("Zakaria")))
print("Name 4 ==> " + str(listePersonnes1.find_by_nom("Name 4")))
print("Name 401 ==> " + str(listePersonnes1.find_by_nom("Name 401")))

print("######### Save the person list in the file  ################## \n\n")
listePersonnes1.write_in_file()

print("######### Read a person list from the file  ################## \n\n")

print('\n'.join(str(elem) for elem in listePersonnes1.read_from_file()))