def menu():
	cadastros = 0
	dicionario = {}
	executar = "s"
  	
	while executar == "s":
		
		op = int(input("### MENU PRINCIPAL ###\n1 - Criar nova conta.\n2 - Depósito.\n3 - Saque.\n4 - Saldo.\n5 - Apagar conta.\n6 - Apagar todas as contas\n"))

		if (op>0) and (op<7):
			
			if op==1: #criar conta

				print("### NOVA CONTA ### \n")
				i_d = int(input("Digite um ID de até 4 números para sua conta: \n"))
				while (i_d>9999):
					i_d = int(input("Erro, digite um ID de até 4 números para sua conta: \n"))

				nome= input("Digite o seu primeiro nome: \n")
				nome = nome.upper()
				saldo= float(input("Digite o seu saldo: \n"))

				dicionario[cadastros] =[i_d,nome,saldo]

				print("\nCadastro realizado com sucesso!\nID: %d\nNome: %s\nSaldo: %d\n" %(dicionario[cadastros][0],dicionario[cadastros][1],dicionario[cadastros][2]))

				cadastros = cadastros + 1

				executar = str(input("Operação finalizada. Deseja retornar ao menu principal? (s/n) \n"))

			elif op==2: #deposito

				existe = False
				i_d = int(input("Digite o ID da conta na qual deseja depositar: \n"))
				
				for i in range(0,cadastros):
					if (i_d == dicionario[i][0]):
						existe = True
						deposito = float(input("Digite o valor do depósito na conta de %s: \n" %dicionario[i][1]))
						dicionario[i][2] = dicionario[i][2] + deposito
						print("O saldo atual é de %.2f \n" %dicionario[i][2])
					
				if (existe==False):
					print("ID inexistente. \n")

				executar = str(input("Operação finalizada. Deseja retornar ao menu principal? (s/n) \n"))

			elif op==3: #saque
	
				existe = False
				i_d = int(input("Digite o ID da conta na qual deseja sacar: \n"))

				for i in range(0,cadastros):
					if (i_d == dicionario[i][0]):
						existe = True
						saque = float(input("Digite o valor de saque da conta de %s: \n" %dicionario[i][1]))
						dicionario[i][2] = dicionario[i][2] - saque
						print("O saldo atual é de %.2f \n" %dicionario[i][2])
						if (dicionario[i][2]<0):
							print("SALDO NEGATIVO! \n")
				
				if (existe==False):
					print("ID inexistente. \n")

				executar = str(input("Operação finalizada. Deseja retornar ao menu principal? (s/n) \n"))

			elif op==4: #saldo
				
				existe = False
				nome = input("Digite o nome do cliente para obter o saldo: \n")
				nome = nome.upper()
				
				for i in range(0,cadastros):
					if (nome == dicionario[i][1]):
						existe = True
						print("O saldo atual é de %.2f \n" %dicionario[i][2])

				if (existe==False):
					print("Nome inexistente. \n")

				executar = str(input("Operação finalizada. Deseja retornar ao menu principal? (s/n) \n"))

			elif op==5: #apagar conta
		
				existe = False
				i_d = int(input("Digite o ID da conta que deseja apagar: \n"))
				
				for i in range(0,cadastros):
					if (i_d == dicionario[i][0]):
						existe = True
						print("Antes de apagar: ", dicionario)
						dicionario.pop(i)
						print("Depois de apagar: ", dicionario)


				if (existe==False):
					print("ID inexistente. \n")

				executar = str(input("Operação finalizada. Deseja retornar ao menu principal? (s/n) \n"))

			elif op==6: #apagar todas as contas

				apagar = input("Deseja realmente apagar todas as contas? (s/n)\n")
				
				if (apagar == "s"):
					print(dicionario)
					dicionario.clear()
					print(dicionario)

				executar = str(input("Operação finalizada. Deseja retornar ao menu principal? (s/n) \n"))
		#if
		else:
			print("Opção inválida, por favor selecione uma opção válida. \n")
		#else
	#while
	return 0
#menu

def main():
  
	print("Bem-vindo ao Banco do Leandro \n")
	menu()
	return 0
#main

main()