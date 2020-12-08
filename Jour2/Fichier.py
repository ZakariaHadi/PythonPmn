depart_ptr = open("depart.txt", "r")
arrivee_ptr = open("arrivee.txt", "w")
arrivee_ptr.write(depart_ptr.read())

arrivee_ptr.close()
depart_ptr.close()