inputs = str(input("Veuillez entrer le devise à convertir ?\n"))
montant = int(inputs[:-1])
devise = inputs[-1]
if devise=="€": print("Montant apres convertion => ",montant * 1.21,"$")
else: print("Montant apres convertion => ",montant * 0.86,"€")
