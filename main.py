quantidade = int(input("Com quantos números você deseja efetuar a equação? "))

numeros = []

for i in range(quantidade):
  num = float(input(f"Digite o {i+1}º número: "))
  numeros.append(num)

print("\n--- Escolha o tipo de operação ---")
print("1 - Adição (+)")
print("2 - Subtração (-)")
print("3 - Multiplicação (*)")
print("4 - Divisão (/)")
print("5 - Exponenciação (**)")

opcao = input("Digite o número correspondente à operação desejada: ")

# 3. Efetua a conta com base na escolha do usuário
if quantidade > 0:
  resultado = numeros[0]
  operacao_valida = True

  if opcao == "1":  # Adição
    for n in numeros[1:]:
      resultado += n
    nome_op = "Adição"

  elif opcao == "2":  # Subtração
    for n in numeros[1:]:
      resultado -= n
    nome_op = "Subtração"

  elif opcao == "3":  # Multiplicação
    for n in numeros[1:]:
      resultado *= n
    nome_op = "Multiplicação"

  elif opcao == "4":  # Divisão
    for n in numeros[1:]:
      if n == 0:
        operacao_valida = False
        break
      resultado /= n
    nome_op = "Divisão"

  elif opcao == "5":  #Exponenciação
    for n in numeros[1:]:
      resultado **= n
    nome_op = "Exponenciação"

  else:
    print("\nOpção inválida! Reinicie o programa.")
    operacao_valida = False

  if operacao_valida and opcao in ["1", "2", "3", "4", "5"]:
    print(f"\nO resultado da operação de {nome_op} é: {resultado}")
  elif not operacao_valida and opcao == "4":
    print("\nErro: Não é possível realizar divisão por zero!")
else:
  print("\nQuantidade de números inválida.")