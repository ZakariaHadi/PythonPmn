from modulebdd import *

new_conn = create_connection("../database/GestionFormaton.db")

if new_conn is None:
    raise Exception("Error! cannot create the database connection.")

vider_Bdd(new_conn) # Truncate all the tables before running the main script

# Add 3 matieres and returning there respective ids to be used in the coming db links with cursus
java_id = ajouterMatiere(new_conn,('Java',))
Csharp_id = ajouterMatiere(new_conn,('C#',))
Algebre_id = ajouterMatiere(new_conn,('Algebre',))

# Add 2 cursus and returning there respective ids to be used in the coming db links with etudiant/matieres
info_id = ajouterCursus(new_conn,('Info',))
math_id = ajouterCursus(new_conn,('Math',))
ajouterCursus(new_conn,('not linked cursus',)) # add a new cursus which won't be linked to any matiere to test the function afficherCursus in the end of the program

# Add etudiants
ajouterEtudiant(new_conn,('nom 1','prenom 1',20,info_id,))
ajouterEtudiant(new_conn,('nom 2','prenom 2',21,math_id,))
ajouterEtudiant(new_conn,('nom 3','prenom 3',21,info_id,))
id_toModify = ajouterEtudiant(new_conn,('nom 4','prenom 4',22,math_id,))

# link the matieres with the cursus ( Java => Info , Csharp => Info , Algebre => Math )
lierCursusMatiere(new_conn,[
    (java_id,info_id,),
    (Csharp_id,info_id,),
    (Algebre_id,math_id,)
    ])

# List db data
listerMatieres(new_conn)
listerCursus(new_conn)
listerEtudiant(new_conn)

# Modify the fourth etudiant
modifierEtudiant(new_conn, {'id' : (id_toModify,),
                            'row': ('modified nom4','modified prenom4',10,math_id,)
                            } )
listerEtudiant(new_conn)


print("afficherEtudiantDeCursus")
afficherEtudiantDeCursus(new_conn,('Info',))

print("afficherMatiereCursus")
afficherMatiereCursus(new_conn,('Java',))

print("afficherCursus")
afficherCursus(new_conn)
