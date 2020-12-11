from connection import create_connection,create_table


new_conn = create_connection("db_tp4.db")


if new_conn is None:
    raise Exception("Error! cannot create the database connection.")

sql_create_tables = """ CREATE TABLE "Personne" (
                                "id"	INTEGER NOT NULL,
                                "login"	TEXT NOT NULL,
                                "password"	TEXT NOT NULL,
                                PRIMARY KEY("id" AUTOINCREMENT)
                            );""" 


create_table(new_conn,sql_create_tables)
def AddUser(conn,user):

    sql = ''' INSERT INTO Personne(login,password)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, (user['login'],user['mdp'],))
    conn.commit()
    return cur.lastrowid


def login(conn,login,mdp):
  
    cur = conn.cursor()
    cur.execute("SELECT * FROM Personne where login = ? and password = ?",(login.get(),mdp.get(),))
    if len(cur.fetchall()) > 0:
        return True
    else:
        return False
    
 



