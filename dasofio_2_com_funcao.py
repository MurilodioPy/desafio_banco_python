menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
=> """

LIMITE = 500
LIMITE_SAQUES = 3
users = []
banco_users = {}

def banco():
  operacao = ""
  while (operacao != "q"):
    name = input("Digite seu nome: ")
    if name not in users:
      new_user(name)
      banco_users[name] = {}
      banco_users[name]["saldo"] = 0
      banco_users[name]["numero_saques"] = 0
      banco_users[name]["extrato"] = ""
      caixa(name)
    else:
      caixa(name)
    operacao = input("Digite 'q' para sair ou enter pra continuar! ")
    # reiniciando o dia do usuário
    if operacao == "q":
      banco_users[name]["numero_saques"] = 0
        
# Lista de usuários
def new_user(user_name):
  users.append(user_name)
    
# operação de saque
def sacar(user_name):
  valor_saque = int(input("Digite o valor de saque: "))
  if valor_saque > LIMITE:
    print("Valor inválido! Limite excedido.")
  elif valor_saque > banco_users[user_name]["saldo"]:
    print("Saldo insuficiente.")
  elif banco_users[user_name]["numero_saques"] >= LIMITE_SAQUES:
    print("Você excedeu o número de saques diários.")
  elif valor_saque <= 0:
    print("Valor inválido! Tente outro valor")
  else:
    banco_users[user_name]["saldo"] -= valor_saque
    banco_users[user_name]["numero_saques"] += 1
    add_extrato(user_name, f"Saq: -R$ {valor_saque:,.2f} \n")
      
# operação de depósito
def depositar(user_name):
  deposito = int(input("Digite o valor de depósito: "))
  if deposito <= 0:
    print("Valor inválido! Tente outro valor")
  else:
    banco_users[user_name]["saldo"] += deposito
    add_extrato(user_name, f"Dep: +R$ {deposito:,.2f} \n")
      
# add ao extrato
def add_extrato(user_name, texto):
  banco_users[user_name]["extrato"] += texto

# visualização do extrato
def view_extrato(user_name):
  print(f"Extrato da Conta: {user_name}\n")
  print(banco_users[user_name]["extrato"])
    
# operacao no caixa
def caixa(name_user):
  sair = False
  while not sair:
    opcao = input(menu)
    if opcao == "d":
      depositar(name_user)
    elif opcao == "s":
      sacar(name_user)
    elif opcao == "e":
      view_extrato(name_user)
    elif opcao == "q":
      sair = True
    else:
      print("Operação inválida, favor selecione novamente.")

# inicio das operações
banco()
