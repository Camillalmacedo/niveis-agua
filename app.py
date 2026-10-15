import colorama #Importar bibliotecas
import random

situacao = ["Muito baixo (crítico)", "Baixo", "Médio", "Alto", "Muito alto (alerta)"] #Criar lista com possíveis situações

def escolha(): #Função que faz a escolha aleatória acessando a biblioteca random
    return random.randint(1, 5)

def resultado(nivel): #Função que personaliza as cores no terminal acessando a biblioteca colorama
    if nivel == 1:
        resultado = colorama.Fore.RED + situacao[0] 
    elif nivel == 2:
        resultado = colorama.Fore.YELLOW + situacao[1] 
    elif nivel == 3:
        resultado = colorama.Fore.GREEN + situacao[2]
    elif nivel == 4:
        resultado = colorama.Fore.CYAN + situacao[3]  
    elif nivel == 5:
        resultado = colorama.Fore.BLUE + situacao[4] 
    else:
        resultado = "Nível inválido"
    

    return resultado #A resposta é armazenada para ser utilizada depois

print (f'''Seja bem-vindo(a) ao sistema de controle de níveis de água!
A atual situação do nível de água é:''') #Mensagem ao usuário
print (resultado(escolha())) #Mostra na cor correspondente
print(colorama.Style.RESET_ALL) #Retorna a cor padrão do terminal

print (f'''Volte em outro momento para mais verificações!''') #Evidência de que a cor voltou ao padrão.
