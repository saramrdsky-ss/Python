input_string = input()

list_operators = []
list_numbers = []

list_conerted = list(input_string.split(""))

for x in range(0, len(list_conerted)):
  if list_conerted[x] == "*" or list_conerted[x] == "+" or list_conerted[x] == "-" or list_conerted[x] == "/":
    list_operators.append(list_conerted[x])
  else:
    list_numbers.append(int(list_conerted[x]))

for y in range(len(list_operators)+1):
# if "*" or "/" or "-" or "+" in list_operators:
    if "/" in list_operators:
      i = list_operators.index("/")
      list_numbers[i] = list_numbers[i] / list_numbers[i + 1]
      del list_numbers[i+1]
      del list_operators[i]
    if "*" in list_operators:
      i = list_operators.index("*")
      list_numbers[i] = list_numbers[i] * list_numbers[i+1]
      del list_numbers[i+1]
      del list_operators[i]
    
    elif "+" in list_operators:
      i = list_operators.index("+")
      list_numbers[i] = list_numbers[i] + list_numbers[i + 1]
      del list_numbers[i+1]
      del list_operators[i]
    elif "-" in list_operators:
      i = list_operators.index("-")
      list_numbers[i] = list_numbers[i] - list_numbers[i + 1]
      del list_numbers[i+1]
      del list_operators[i]

res = list_numbers
print(res)
print(list_operators)
