from dados import cadastro_filmes, fila_reserva, pilha_devolucao, registro_devolucao
from utils import titulo, linha
from cadastro import catagol, cadastrar

def start():
    titulo("SISTEMA DE LOCAÇÃO")
    print('''
    1 - Listar catálogo                                  #com status de disponibilidade
    2 - Cadastrar filme (título, gênero, ano)            #disponível: sim/não
    3 - Fila de reservas                                 # FIFO: primeiro a reservar aluga primeiro
    4 - Pilha de devoluções                              #LIFO: última devolução aparece primeiro
    5 - Registrar aluguel                                #(marca filme como indisponível)
    6 - Registrar devolução                              #marca filme como disponível
    7 - Procurar por gênero                              #filtra catálogo por gênero\Bonus
    8 - Sair                                             #Encerrar programa
    ''')
    linha()
    print()
def option(): #opção do menu
    while True:
        opcao = int(input("Digite a opção desejada: "))
        if opcao == 1: 
            catagol()
        elif opcao == 2: 
            cadastrar()
        elif opcao == 3: 
            fila()
        elif opcao == 4:
            pilha()

        elif opcao == 5:
            registro_aluguel()

        elif opcao == 6:
            registro_dev()
            
        elif opcao == 7:
            pgenero()
        elif opcao == 8:
            print("Cabou")
            break
        else:
            print("Opção invalida!!")

def fila(): #FILA DE RESERVA 3
    mostrar = int(input("Ver fila: 1 - reservar filme: 2: "))
    if mostrar == 2:
        print("Cadastrar reserva!!!")
        nomafilme = input("Nome do cliente: ")
        reserva = input("Filme a ser reservado: ")
        Id_filme = str(input("ID do filme a ser reservado: "))
        fila = {
            "Nomefilme": nomafilme, 
            "Reserva": reserva,
            "Id_filme": Id_filme
        }
        fila_reserva.append(fila)
        print("fila de reserva cadastrado na fila!!!")
    else:
        print("Fila de reserva:")
        for fila in fila_reserva:
            print(f"{fila['Nomefilme']} | {fila['Reserva']} | {fila['Id_filme']}")
def pilha(): #Não finalizajicdsvfsdfbdfbdfb 4
    print("Pilhas de devolução")
    if len(pilha_devolucao) == 0: #lê a pilha de devolução, se tiver vazia, ele dispara o print
        print("Sem registros de devolução")
    else:
        for pilha_devolu in reversed(pilha_devolucao): #le a pilha de devolução, e mostra de trás para frente, ou seja, a última devolução aparece primeiro
            print(f"{pilha_devolu['Nome']} | {pilha_devolu['Genero']} | {pilha_devolu['Ano']} | {pilha_devolu['Disponível']}") #Pega da pilha de devolução, o nome, genero, ano e disponibilidade do filme devolvido e mostra para o usuário

def registro_aluguel(): # Aluguel 5
    print("Registrar aluguel")
    catagol() # mostra o catalogo cadastrado
    if len(cadastro_filmes) == 0: #Não tendo nada cadastrado, ele dispara o print
        print("Não há filmes cadastrados para alugar.")
        return
    try:
        id_filme = int(input("Digite o número do filme que deseja alugar: ")) #Cria uma nova variavel
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.")
        return
    for filmes in cadastro_filmes: #filme é variavel local, filme procura dentro do cadastro
        if filmes['ID'] == id_filme: # Se id for igual ao id que o filme achou ele entra na condição
            print("\n [Deseja alugar o filme?] \n")
            print("1 = Sim")
            print("2 = Não")
            opcao = str(input("Digite a opção desejada: ")) #define o que acontece
            if opcao == "1":
                filmes['Disponível'] = "Não" #Atuaiza o catalogo para não disponível
                print("Filme alugado com sucesso!")
                print("Voltando ao menu...")
            elif opcao == "2":
                print("Voltando para o Menu...")
            else:
                print("Opção invalida")
def registro_dev(): #devolução 6    
    print("Registrar devolução")
    catagol() # Catalogo cadastrado
    if len(cadastro_filmes) == 0: #procura dentro do cadastro, se tem algum dentro
        print("Não há filmes cadastrados para devolver.")
        return
    try:
        id_filme = int(input("Digite o número do filme que deseja devolver: ")) #Id do filme que não é mostrado, mas é sinalizado como 'i' no codigo
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.")
        return
    for filmes in cadastro_filmes: # filme é variavel local, filme procura dentro do cadastro
        if filmes['ID'] == id_filme: # Se id for igual ao id que o filme achou ele entra na condição
            print("\n [Deseja devolver o filme?] \n")
            print("1 = Sim")
            print("2 = Não")
            opcao = str(input("Digite a opção desejada: "))
            if opcao == "1":
                filmes['Disponível'] = "Sim" #atualizar o catalogo para disponível
                print("Filme devolvido com sucesso!")
                print("Voltando ao menu...")
                pilha_devolucao.append(filmes) #adiciona a pilha de devolução
            elif opcao == "2":
                print("Voltando para o Menu...")
            else:
                print("Opção invalida")
        
start()
option()
