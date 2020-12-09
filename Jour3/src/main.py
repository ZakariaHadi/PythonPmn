from modulebdd import *

new_conn = create_connection("../database/GestionFormaton.db")

if new_conn is None:
    raise Exception("Error! cannot create the database connection.")


ajouterMatiere(new_conn,'Java')
ajouterMatiere(new_conn,'C#')
ajouterMatiere(new_conn,'Algebre')

ajouterCursus(new_conn,'Info')
ajouterCursus(new_conn,'Math')

ajouterEtudiant(new_conn,('nom1','prenom1'))
ajouterEtudiant(new_conn,'Info')
ajouterEtudiant(new_conn,'Info')