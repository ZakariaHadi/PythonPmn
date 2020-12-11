from adresse import Adresse
class Personne :

    def __init__(self,nom,sex):
        self.__nom = nom
        self.__sex = sex
        self.__adresses= []

    @property
    def nom(self):
        return self.__nom
    
    @property
    def sex():
        return self.__sex
    
    @nom.setter
    def nom(self,a):
        self.__nom = a
    
    @sex.setter
    def sex(self,s):
        self.__sex = s

    #Méthodes Gestion de l'attribut tableau adress

    def add_adress(self,adress):
        self.__adresses.append(adress)
        print ("l'adress {} a été bien ajouter".format(adress))

    def getAdress(self):
        return self.__adresses
    
    def removeAdress(self,adress):
        if adress in self.__adresses:
            self.__adresses.remove(adress)
            print ("l'adress {} a été bien supprimer".format(adress))
    
    def __str__(self):

        return ('====> Personne : [nom : {} , sex: {} , adresses: {}]'.format(self.__nom,self.__sex,[str(addr) for addr in self.__adresses] ))