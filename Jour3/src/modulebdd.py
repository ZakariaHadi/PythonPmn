

from connection import create_connection,create_table

new_conn = create_connection("../database/GestionFormaton.db")

if new_conn is None:
    raise Exception("Error! cannot create the database connection.")

sql_create_tables = """ CREATE TABLE "Cursus" (
                                "idCursus"	INTEGER NOT NULL,
                                "nomCursus"	TEXT NOT NULL,
                                PRIMARY KEY("idCursus" AUTOINCREMENT)
                            );
                        CREATE TABLE "Etudiant" (
                                "idEtudiant"	INTEGER NOT NULL,
                                "nomEtudiant"	TEXT NOT NULL,
                                "prenomEtudiant"	TEXT NOT NULL,
                                "age"	INTEGER NOT NULL,
                                "idCursus"	INTEGER,
                                PRIMARY KEY("idEtudiant" AUTOINCREMENT),
                                FOREIGN KEY("idCursus") REFERENCES "Cursus"("idCursus")
                            );
                            CREATE TABLE "Matiere" (
                                "idMatiere"	INTEGER NOT NULL,
                                "nomMatiere"	TEXT NOT NULL,
                                PRIMARY KEY("idMatiere" AUTOINCREMENT)
                            );
                            CREATE TABLE "Matiere_Cursus" (
                                "idMatiere"	INTEGER NOT NULL,
                                "idCursus"	INTEGER NOT NULL,
                                FOREIGN KEY("idMatiere") REFERENCES "Matiere"("idMatiere"),
                                FOREIGN KEY("idCursus") REFERENCES "Cursus"("idCursus"),
                                PRIMARY KEY("idMatiere","idCursus")
                            );"""
#create_table(new_conn,sql_create_tables)


#"#### 1) Add Data ##########################################"""

def ajouterMatiere(conn,nomMatiere):
    sql = ''' INSERT INTO Matiere(nomMatiere)
              VALUES(?) '''
    cur = conn.cursor()
    cur.execute(sql, nomMatiere)
    conn.commit()
    return cur.lastrowid

def ajouterCursus(conn,nomCursus):
    sql = ''' INSERT INTO Cursus(nomCursus)
              VALUES(?) '''
    cur = conn.cursor()
    cur.execute(sql, nomCursus)
    conn.commit()
    return cur.lastrowid

def ajouterEtudiant(conn,etudiant):

    sql = ''' INSERT INTO Etudiant(nomEtudiant,prenomEtudiant,age,idCursus)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, etudiant)
    conn.commit()
    return cur.lastrowid

def lierCursusMatiere(conn,matieres_cursus):

    sql = ''' INSERT INTO matiere_cursus VALUES(?,?) '''
    cur = conn.cursor()
    print(matieres_cursus)
    cur.executemany(sql,matieres_cursus)
    conn.commit()
    return cur.lastrowid



#"#### 2) Select Data ##########################################"""

def listerMatieres(conn):
    
    cur = conn.cursor()
    cur.execute("SELECT * FROM Matiere")

    rows = cur.fetchall()

    for matiere in rows:
        print(matiere)

def listerCursus(conn):
    
    cur = conn.cursor()
    cur.execute("SELECT * FROM Cursus")

    rows = cur.fetchall()

    for cursus in rows:
        print(cursus)


def listerEtudiant(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM Etudiant")
    desc = cur.description
    column_names = [col[0] for col in desc]
    data = [dict(zip(column_names, row))  
        for row in cur.fetchall()]

    print(data)

#"#### 3) Modify Data ##########################################"""

def modifierMatiere(conn,newMatiere):
    if(newMatiere['id'] is not None and newMatiere['nomMatiere'] is not None):
        sql = ''' UPDATE Matiere
                    SET nomMatiere = ?,
                    WHERE id = ?'''
        cur = conn.cursor()
        cur.execute(sql,(newMatiere['nomMatiere'],newMatiere['id']))
        conn.commit()

def modifierCursus(conn,newCursus):
    if(newCursus['id'] is not None and newCursus['nomCursus'] is not None):
        sql = ''' UPDATE Cursus
                    SET nomCursus = ?,
                    WHERE id = ?'''
        cur = conn.cursor()
        cur.execute(sql,(newCursus['nomMatiere'],newCursus['id']))
        conn.commit()

def modifierEtudiant(conn,newEtudiant):
    if(newEtudiant['id'] is not None and newEtudiant['row'] is not None):
        sql = ''' UPDATE Etudiant
                    SET nomEtudiant = ?,
                    prenomEtudiant = ?,
                    age = ?,
                    idCursus = ?
                    WHERE idEtudiant = ?'''
        cur = conn.cursor()
        cur.execute(sql,(newEtudiant['row']+newEtudiant['id']))
        conn.commit()


#"#### 4) Delete Data ##########################################"""

def supprimerMatiere(conn,idMatiere):
    sql = 'DELETE FROM Matiere WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (idMatiere,))
    conn.commit()

def supprimerCursus(conn,idCursus):
    sql = 'DELETE FROM Cursus WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (idCursus,))
    conn.commit()

def supprimerEtudiant(conn,idEtudiant):
    sql = 'DELETE FROM Etudiant WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (idEtudiant,))
    conn.commit()

def vider_Bdd(conn):
    c = conn.cursor()

    c.execute('DELETE FROM matiere;',)
    c.execute('DELETE FROM etudiant;',)
    c.execute('DELETE FROM cursus;',)
    c.execute('DELETE FROM Matiere_Cursus;',)

    print(" all tables are truncated !!")
    conn.commit()


def afficherEtudiantDeCursus(conn,nomCursus):
    cur = conn.cursor()
    cur.execute("SELECT * FROM Etudiant e where e.idCursus = (Select idCursus from Cursus c where c.nomCursus = ?)", nomCursus)

    rows = cur.fetchall()
    for etud in rows:
        print(etud)

 
def afficherMatiereCursus(conn,nomMatiere):
    cur = conn.cursor()
    cur.execute("SELECT c.nomCursus FROM Cursus c join Matiere_Cursus mc on mc.idCursus=c.idCursus join Matiere m on mc.idMatiere = m.idMatiere where m.nomMatiere = ?", nomMatiere)
    rows = cur.fetchall()

    for matiere in rows:
        print(matiere)

def afficherCursus(conn):
    cur = conn.cursor()
    cur.execute("SELECT c.nomCursus FROM Cursus c where c.idCursus not in (select idCursus from matiere_cursus)")
    rows = cur.fetchall()

    for matiere in rows:
        print(matiere)
