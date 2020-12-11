class Alphabet:
	def __init__(self, nom): 
		self.lettre_nom = nom 
	def info (self): 
		print("je suis une lettre de l'Alphabet")
	def test1(self): 
		print ("Fonction test1() de la classe Alphabet")
	def test2 (self): 
		print("Fonction test2() de la classe Alphabet")
class Mot: 
	def info(self): 
		print("je suis un mot")
	def test1(self): 
		print ("Fonction test1() de la classe Mot")
	def test3 (self): 
		print ("Fonction test3() de la classe Alphabet")
class Accent: 
	def info(self): 
		print("je suis une lettre avec accent")
	def test1(self): 
		print ("Fonction test1() de la classe Accent")
	def test3 (self): 
		print ("Fonction test3() de la classe Accent")
class A(Alphabet): 
	def info(self): 
		print("je suis A")
	def test1 (self): 
		print("Fonction test1() de la classe A")
class Abracadabra(Mot): 
	def test1(self): 
		print ("Fonction test1() de la classe Abracadabra")
class AGrave(Accent,A,Abracadabra): 
	def test4(self): 
		print("Fonction test4() de la classe AGrave")