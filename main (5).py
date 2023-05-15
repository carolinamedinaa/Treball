opcion = 0
while opcion != 3:
  print('1: Animarme')
  print('2: Calcular')
  print('3: Sortir')
  opcion = int(input('Tria una opció: '))

  if opcion == 1:
    nom = input('Escriu un nom: ')
    guions = ''

    for i in nom:
      print(f"Dame una {i}")

    for lletra in nom:
      guions = guions + lletra + '-'
    print(guions)

  if opcion == 2:
    operacio = input('Escriu una operacio: ')

    if " + " in operacio:
      operandos = operacio.split(" + ")
      operador = "+"
    elif " - " in operacio:
      operandos = operacio.split(" - ")
      operador = "-"
    elif " * " in operacio:
      operandos = operacio.split(" * ")
      operador = "*"
    elif " / " in operacio:
      operandos = operacio.split(" / ")
      operador = "/"

  #El duplicarem per si la operació no te espais

    if "+" in operacio:
      operandos = operacio.split("+")
      operador = "+"
    if "-" in operacio:
      operandos = operacio.split("-")
      operador = "-"
    if "*" in operacio:
      operandos = operacio.split("*")
      operador = "+"
    if "/" in operacio:
      operandos = operacio.split("/")
      operador = "/"

    if operador == "+":
      resultat = int(operandos[0]) + int(operandos[1])
    elif operador == "-":
      resultat = int(operandos[0]) - int(operandos[1])
    elif operador == "*":
      resultat = int(operandos[0]) * int(operandos[1])
    elif operador == "/":
      resultat = int(operandos[0]) / int(operandos[1])

    print(f"{operandos[0]} {operador} {operandos[1]} = {resultat}")
    operacio = 0

  if opcion == 3:
    print('Has sortit')
    break
