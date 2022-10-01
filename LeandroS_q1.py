def main():
  
	import random
  	
	palavras = ['teclado', 'computador', 'notebook', 'memoria', 'processador', 'smartphone', 'lulalivre', 'ventilador', 'bateria', 'carregador']
	
	jogar = 's'
	while jogar == 's':

		descoberta = []  
		x = random.randint(0,len(palavras))  
		escolhida = list(palavras[x])

		for i in range(0,len(escolhida)):
			descoberta.append("_")

		impressa = ' '.join(descoberta)[:]
  
		print ("Jogo da Forca!\n")
		print ("A palavra possui %d letras... \n" %len(escolhida))
		print ("%s\n" %impressa)
  
		erros = 0
	
		while erros < 6:

			achou = False
			terminou = True
			letra = str(input("Digite uma letra: \n"))
 	 
			for i in range(0,len(escolhida)):
				if letra.lower() == escolhida[i]:
					descoberta[i] = letra.upper()
					achou = True
 	    	
			if achou == True:
				impressa = ' '.join(descoberta)[:]
				print ("A palavra é: %s\n" %impressa)
			else:
				erros = erros+1
				if erros < 6:
					print("Você errou pela %dª vez. Tente de novo! \n" %erros)
    
			for i in range(0,len(escolhida)):
				if descoberta[i] == "_":
					terminou = False

			if terminou == True:
				print("Parabéns você acertou a palavra! \n")
				jogar = str(input("Deseja jogar novamente? (s/n): \n"))
				if jogar=="s":
					main()			
				else:
					exit(0)

		impressa = ''.join(escolhida)[:]		
		print ("Enforcado!!! A palavra era %s\n" %impressa.upper())

		jogar = str(input("Deseja jogar novamente? (s/n): \n"))
		print("\n")

	return 0

main()

