limit = 3
attempt = 1
while attempt <= limit:
  auto_user = input("Podaj swoje ulutione auto: ").lower()
  print(auto_user)
  if auto_user == "bmw":
    message="good driver"
  elif auto_user == "tesla":
    message = "giga s...."
  elif auto_user == "mercedes":
    message="bęc"
  else:
    message="słaby z Ciebie driver"
  print(message,"próba:", attempt, "*"*attempt)
  attempt += 1