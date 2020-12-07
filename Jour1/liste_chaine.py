#coding:utf-8

myList = ("toto", "tata", "tititi")
iterator = iter(myList)

for item in myList:
  print(item,"--> ",len(item))