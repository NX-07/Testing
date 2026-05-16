from dedos import cadastro_filmes, fila_reserva, pilha_devolucao

cadastro_filmes =[]
filmes = []
fila_reserva = []
pilha_devolucao = []

def logo():
    print("-=-" * 20)
def start():
    logo()
    print("     OPÇÕES     ")
    logo()
    print('''1 - Listar catálogo        #com status de disponibilidade
    2 - Cadastrar filme (título, gênero, ano)            #disponível: sim/não
    3 - Fila de reservas                                 # FIFO: primeiro a reservar aluga primeiro
    4 - Pilha de devoluções                              #LIFO: última devolução aparece primeiro
    5 - Registrar aluguel                                #(marca filme como indisponível)
    6 - Registrar devolução                              #marca filme como disponível
    7 - Sair                                             #Encerrar programa''')
    logo()
def option(): #opção do menu
    while True:
        op = int(input("Num: "))
        
        if op == 1: 
            catagolo()

        elif op == 2: 
            cadastrar()

        elif op == 3: 
            fila()
        elif op == 4:
            print()

        elif op == 5:
            print()

        elif op == 6:
            print()
            
        elif op == 7:
            print("Cabou")
            break
        else:
            print("Opção invalida!!")

def catagolo(): #catalogo
    print("FILME | GÊNERO | ANO | DISPONÍVEL")
    for filme in cadastro_filmes:
        print(f"{filme['Nome']} | {filme['Genero']} | {filme['Ano']} | {filme['Disponível']}")
def cadastrar(): #cadastro de filmes
    nome = input("Cadastrar nome do filme: ")
    genero = input("Cadastrar gênero do filme: ")
    ano = input("Cadastre o ano do filme (AAAA): ")
    disponivel = input("O filme está disponível? (Sim/Não): ")
    filmes = {
        "Nome": nome,
        "Genero": genero,
        "Ano": ano,
        "Disponível": disponivel
    }
    cadastro_filmes.append(filmes)
    print("Filme cadastrado!!!")
def fila(): #FILA DE RESERVA
    mostrar = int(input("Ver fila: 1 - reservar filme: 2: "))
    if mostrar == 2:
        print("Cadastrar reserva!!!")
        nomafilme = input("Nome do cliente: ")
        reserva = input("Filme a ser reservado: ")
        fila = {
            "Nomefilme": nomafilme, 
            "Reserva": reserva
        }
        fila_reserva.append(fila)
        print("fila de reserva cadastrado na fila!!!")
    else:
        print("Fila de reserva:")
        for fila in fila_reserva:
            print(f"{fila['Nomefilme']} | {fila['Reserva']}")
def pilha():
    print("Devoluções")
start()
option()
