#dzielniki
liczba = int(input("Podaj liczbę\n"))
# for i in range(1, liczba + 1):
#   if liczba % i == 0:
#     print(i, end=" ")

# i = 1
# while i <= liczba:
#   if liczba % i == 0:
#     print(i, end=" ")
#   i += 1
  



# def znajdz_dzielniki(liczba):
#   dzielniki = []
#   for i in range(1, liczba + 1):
#       if liczba % i == 0:
#           dzielniki.append(i)
#   return dzielniki

# # Przykładowe użycie
# liczba = int(input("Podaj liczbę: "))
# wynik = znajdz_dzielniki(liczba)
# print(f"Dzielniki liczby {liczba}: {wynik}")

#czy pierwsza
# for i in range(2, liczba // 2 + 1):
#   if liczba % i == 0:
#     print("złożona")
#     break
# else:
#   print("pierwsza")

# def czy_liczba_pierwsza(liczba):
#   if liczba < 2:
#       return False
#   for i in range(2, int(liczba**0.5) + 1):
#       if liczba % i == 0:
#           return False
#   return True

# # Przykładowe użycie
# liczba = int(input("Podaj liczbę: "))
# if czy_liczba_pierwsza(liczba):
#   print(f"{liczba} jest liczbą pierwszą.")
# else:
#   print(f"{liczba} nie jest liczbą pierwszą.")

#nwd - największy wspólny dzielnik 
#optymalny
a = 10
b = 4
while b != 0:
  a, b = b, a % b
print(a)


a = 10
b = 4
while a != b:
  if a > b:
    a = a - b
  else:
    b = b - a

# print(a)


# def nwd(a, b):
#   while b:
#       a, b = b, a % b
#   return a

# # Przykładowe użycie
# liczba1 = int(input("Podaj pierwszą liczbę: "))
# liczba2 = int(input("Podaj drugą liczbę: "))

# wynik = nwd(liczba1, liczba2)
# print(f"Największy Wspólny Dzielnik ({liczba1}, {liczba2}): {wynik}")
