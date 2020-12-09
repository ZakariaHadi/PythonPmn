from modulebdd import *

new_conn = create_connection("../database/GestionFormaton.db")

if new_conn is None:
    raise Exception("Error! cannot create the database connection.")

vider_Bdd(new_conn)


java_id = ajouterMatiere(new_conn,('Java',))
Csharp_id = ajouterMatiere(new_conn,('C#',))
Algebre_id = ajouterMatiere(new_conn,('Algebre',))

info_id = ajouterCursus(new_conn,('Info',))
math_id = ajouterCursus(new_conn,('Math',))

ajouterEtudiant(new_conn,('nom 1','prenom 1',20,info_id,))
ajouterEtudiant(new_conn,('nom 2','prenom 2',21,math_id,))
ajouterEtudiant(new_conn,('nom 3','prenom 3',21,info_id,))
ajouterEtudiant(new_conn,('nom 4','prenom 4',22,math_id,))

lierCursusMatiere(new_conn,[
    (java_id,info_id,),
    (Csharp_id,info_id,),
    (Algebre_id,math_id,)
    ])

listerMatieres(new_conn)
listerCursus(new_conn)
listerEtudiant(new_conn)
