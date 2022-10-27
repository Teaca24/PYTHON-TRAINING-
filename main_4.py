cognomi = ["BOMMO", "FORMICOLA", "TEACA"]
for x in cognomi:
  print(x) 
#il comando print(x) ci permette di stampare in collona tutte le variabili all'interno delle parentesi 

for x in "MOLDAVIA":
  print(x) 
#in questo caso dato che non è presente una lista il comando print(x) stampera in collona le lettere della parola tra virgolette 

cognomi = ["BOMMO", "FORMI", "TEACA"]
for x in cognomi:
  print(x) 
  if x == "FORMI":
    break
#il comando break permette di fermare la stampa della lista ad una determinata variabile in modo da non stampare tutta la lista 

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x) 
#il comando "continue" permette di saltare una variabile e di stampare le altre 

for x in range(122):
  print(x) 
#ci stampa tutti i numeri compresi, in collona, tra 0 e 122 con il numero che consideriamo non incluso 

for x in range(2, 6):
  print(x)
  #stampa tutti i numeri compresi tra il primo e l'ultimo, escluso l'ultimo 

  for x in range(2, 30, 3):
  print(x) 
#stamapa i numeri tra 2 e 30, escluso 30, incrementando di 3 

for x in range(6):
  print(x)
else:
  print("Finally finished!")
  #