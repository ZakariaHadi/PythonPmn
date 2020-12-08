#coding:utf-8

fr_ang = {
  "langage": "language",
  "fille": "girl",
  "voiture": "car",
  "ciel": "sky",
  "fenetre": "window"
}

fr_ang['mot'] = "word"

print("my dictionnary (fr:ang) : \n", fr_ang.values())

to_del = [key for key in fr_ang if key.startswith('c')] 
for key in to_del: del fr_ang[key]

print("my dictionnary after supression (fr:ang) : \n", fr_ang.values())
