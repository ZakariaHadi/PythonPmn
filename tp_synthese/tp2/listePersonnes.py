from personne import Personne

class ListPersonnes:

    def __init__(self):
        self.__personnes = []
    
    #Methods of profil gestion
    def addPersonne(self,p):
        self.__personnes.append(p)
    
    def getPersonnes(self):
        return self.__personnes
    
    def removePersonne(self,p):
        if p in self.__personnes :
            self.__personnes.remove(p)
        else:
            print("The given person is not existed")
    
    #Searching in the person list by the name 
    def find_by_nom(self,s):
        for personne in self.__personnes :
            if personne.nom == str(s) :
                return str(personne)
        return None

    # Searching if a postal code is exists
    def exists_code_postal(self,PC):
        for personne in self.__personnes :
            for adresse in personne.getAdress():
                if adresse.codePostal == PC :
                    return True
                else :
                    return False

    #get the number of persons linked to this city
    def count_personne_ville(self,ville):
        count = 0
        for personne in self.__personnes :
            for adresse in personne.getAdress():
                if adresse.ville == ville :
                    count = count + 1
        return count

    #Modify a name of a person
    def edit_personne_nom(self,oldNom,newNom) :
        for personne in self.__personnes :
            if personne.nom == oldNom:
                personne.nom = newNom
    
    #Modify city of a person
    def edit_personne_ville(self,nom,newCity):
        for personne in self.__personnes :
            if personne.nom == nom:
                for adresse in personne.getAdress():
                    adresse.ville = newCity

    def __str__(self):
        return ("Liste Personnes : \n {} ".format('\n'.join([str(per) for per in self.__personnes])))

    def write_in_file(self):
        try:
            with open("personnes.data","w") as fic:
                for pers in self.__personnes:
                    fic.write('%s\n' % pers)
            print("The list of the persons has been written in the file")
            fic.close()
            return True
        except:
            fic.close()
            print("there was a error in the writting process !!")
            return False
            

    
    def read_from_file(self):
        try:
            personnes = []
            with open("personnes.data","r") as fic:
                for row in fic:
                    personnes.append(row)
            fic.close()
            return personnes
        except:
            fic.close()
            print("there was a error in the reading process !!")
            return None
    