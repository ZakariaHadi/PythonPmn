##################################### tp1 Principal program ##########################################

from db_manipulation import *

new_conn = create_connection("./db_tp1.db")

if new_conn is None:
    raise Exception("Error! cannot create the database connection.")

vider_Bdd(new_conn) # Truncate all the tables before running the main script


#### Question 1 test all CRUD functions

## CREATE FUNCTIONS test
client1_id = ajouterClient(new_conn,"HADI","Zakaria","59 rue lenain de tillemont","Homme")
client2_id = ajouterClient(new_conn,"Nom 2","Prenom 2","59 rue lenain de tillemont","Femme")
client3_id = ajouterClient(new_conn,"Nom 3","Prenom 3","59 rue lenain de tillemont","Femme")

agence1_id = ajouterAgence(new_conn,"BNP")
agence2_id = ajouterAgence(new_conn,"BP")
agence3_id = ajouterAgence(new_conn,"Credit mutuel")

compte1_client1 = ajouterCompte(new_conn,0,100,client1_id,agence1_id)
compte1_client2 = ajouterCompte(new_conn,20,100,client2_id,agence2_id)
compte2_client1 = ajouterCompte(new_conn,500,100,client1_id,agence1_id)
compte1_client3 = ajouterCompte(new_conn,1000,100,client3_id,agence1_id)
compte3_client1 = ajouterCompte(new_conn,300,100,client1_id,agence1_id)

#READ FUNCTIONS test

print ('\n'.join([ str(myelement) for myelement in listerComptes(new_conn) ])) # print all the accounts
print ('\n'.join([ str(myelement) for myelement in listerComptes(new_conn,compte2_client1) ])) # print the seconde account of the first client (id=compte2_client1)

print ('\n'.join([ str(myelement) for myelement in listerAgence(new_conn) ])) # print all the banks

print ('\n'.join([ str(myelement) for myelement in listerClient(new_conn) ])) # print all the clients
print (listerClient(new_conn,'HADI','Zakaria')) # print HADI Zakaria profil

# UPDATE FUNCTIONS test
modifierClient(new_conn,{
    'id': client3_id,
    'nom': 'modified name 3',
    'prenom': 'modified prenom 3',
    'Civilite': 'Homme',
    'adresse': '100 rue la marche rouge'
})
print (listerClient(new_conn,'modified name 3','modified prenom 3')) # print the modified profil

modifierAgence(new_conn,{
    'id': agence3_id,
    'nomAgence': 'modified agence 3'
})
print (listerAgence(new_conn,'modified agence 3') ) # print the modified bank


modifierCompteBancaire(new_conn,{
    'id': compte1_client1,
    'decouvert' : 500, # A VIP client we give him 500 as a decouvert,
    'solde' : 1000
})

print ('\n'.join([ str(myelement) for myelement in listerComptes(new_conn,compte1_client1) ]))


#DELETE functions test

# supprimerClient(new_conn,client2_id )
# supprimerCompte(new_conn,compte1_client1)
# supprimerAgence(new_conn,agence3_id)

####### Question 2 =======>

# Add solde = 1400 to the first client
ajouter(new_conn,listerClient(new_conn,client1_id)[0],listerComptes(new_conn,compte1_client1)[0],1400)
print("==================== After adding 1400 as a solde ======================")
print ('\n'.join([ str(myelement) for myelement in listerComptes(new_conn,compte1_client1) ]))


####### Question 3 =======>

# withdraw 500 from the first client's first account  old solde= 2400 new solde = 1900
retirer(new_conn,listerClient(new_conn,client1_id)[0],listerComptes(new_conn,compte1_client1)[0],500)
print("==================== After withdrawing 500 ======================")
print ('\n'.join([ str(myelement) for myelement in listerComptes(new_conn,compte1_client1) ]))

# trying to withdraw 5000 more than the decouvert
retirer(new_conn,listerClient(new_conn,client1_id)[0],listerComptes(new_conn,compte1_client1)[0],5000)

####### Question 4 =======>

print ('\n'.join([ str(compte) for compte in listerCompteAgence(new_conn,{
    'nomAgence': 'BNP'
}) ]))


####### Question 5 =======>

print ('\n'.join([ str(compte) for compte in listerCompte(new_conn,{
    'idClient': client1_id
}) ]))

