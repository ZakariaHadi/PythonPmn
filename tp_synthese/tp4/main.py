from formulaireGUI import formulaireGUI
from formulaire import * 

new_conn = create_connection("db_tp4.db")


user1_id = AddUser(new_conn,{
	'login' : 'zakaria',
	'mdp': '123456'
})



fenetrePrincipale = formulaireGUI(new_conn)

fenetrePrincipale.lanceGUI()


fenetrePrincipale.root.mainloop()





