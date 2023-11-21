#bankomat
pin = 1234
limit = 3
proba = 1
while proba <=limit:
  proba += 1
  x = int(input("podaj pin do karty:  "))
  if pin == x:
    print("Poprawny pin. Ile chcesz gotówki? ")
    break
else:
  print("Karta została zablokowana")
  