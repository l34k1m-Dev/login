from os import system
from getpass import getpass
import stdiomask
from time import sleep
from colorama import init, Fore, Back, Style
init(autoreset=True)

def exibir_menu():
	print(Fore.GREEN + 36*"=")
	print(Back.GREEN + "** Bem-vindo ao Sistema de Login **")
	print(Fore.GREEN + 36*"=")
	print(Fore.GREEN + "Escolha a opção que deseja realizar: \n")
	print(Fore.GREEN +"[1] Cadastrar novo usuário")
	print(Fore.GREEN +"[2] Fazer login")
	print(Fore.GREEN +"[3] Sair \n")
	print(Fore.GREEN + 36*"=")

	opcao = int(input('Digite a opção: '))
	return(opcao)

def fazer_login():
	login = input('Nome de Usuário: ')
	senha = stdiomask.getpass(prompt = 'Senha: ', mask = '*')
	return(login, senha)

def buscar_usuario(login, senha):
	usuarios = []
	try:
		with open('usuarios.txt', 'r+', encoding='Utf-8', newline='') as arquivo:
			for linha in arquivo:
				linha = linha.strip(",")
				usuarios.append(linha.split())

			for usuario in usuarios:
				nome = usuario[0]
				password = usuario[1]
				if login == nome and senha == password:
					return True
	except FileNotFoundError:
		return False

while True:
	system('cls')
	opcao = exibir_menu()

	if opcao == 1:
		login, senha = fazer_login()
		if login == senha:
			print('Sua senha deve ser diferente do login.')
			senha = getpass('Senha: ')
		user = buscar_usuario(login, senha)
		if user == True:
			print('O usuário já existe!')
			sleep(2)
		else:
			with open('usuarios.txt', 'a+', encoding='Utf-8', newline='') as arquivo:
				arquivo.writelines(f'{login} {senha}\n')
			print('Usuário cadastro com sucesso!\n')
			sleep(2)
	
	elif opcao == 2:
		login, senha = fazer_login()
		user = buscar_usuario(login, senha)
		if user == True:
			print('Login realizado com sucesso!')
			sleep(1)
			exit()
		else:
			print('Nome de usuário ou senha inválido. Por favor verifique!')
			sleep(2)
	else:
		system('cls')
		print('\nVocê encerrou a sessão!')
		break