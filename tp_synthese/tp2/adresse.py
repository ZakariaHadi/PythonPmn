
class Adresse:

    def __init__(self,codePostal,rue,ville):
        self.__codePostal = codePostal
        self.__ville = ville
        self.__rue = rue
    
    #Getters
    @property
    def codePostal(self):
        return self.__codePostal

    @property
    def ville(self):
        return self.__ville

    @property  
    def rue(self):
        return self.__rue
    
    #Setters
    @codePostal.setter
    def codePostal(self,v):
        self.__codePostal = v
    
    @ville.setter
    def ville(self,v):
        self.__ville = v
    
    @rue.setter
    def rue(self,r):
        self.__rue = r

    def __str__(self):
        return ("Adress [rue : {} , Ville: {} , codePostal: {}] ".format(self.__rue,self.__ville,self.__codePostal))