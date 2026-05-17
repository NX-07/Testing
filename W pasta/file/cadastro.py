from dados import cadastro_filmes
from utils import titulo, linha


def catagol(): #catalogo 1 
    print("\n FILME | GÊNERO | ANO | DISPONÍVEL\n")
    for i, filme in enumerate(cadastro_filmes, start=1): 
        print(f"{i} - {filme['Nome']} | {filme['Genero']} | {filme['Ano']} | {filme['Disponível']}")
    #for filme in cadastro_filmes:
        #print(f"{filme['Nome']} | {filme['Genero']} | {filme['Ano']} | {filme['Disponível']}")

def cadastrar(): #cadastro de filmes 2 
    print("[CADASTRO DE FILMES]\n ")
    nome = str(input("Nome do filme: "))    
    print("\nCadastre o gênero do filme")
    print("1 - Drama | 2 - Ação | 3 - Animação | 4 - Suspense | 5 - Policial | 6 - Comedia | 7 - Ficção")
    
    genero = str(input("\nEscolha o gênero (1 a 7): "))
    if genero == "1":
        genero = "Drama"
    elif genero == "2":
        genero = "Ação"
    elif genero == "3":
        genero = "Animação"
    elif genero == "4":
        genero = "Suspense"
    elif genero == "5":
        genero = "Policial"
    elif genero == "6":
        genero = "Comédia"
    elif genero == "7":
        genero = "Ficção"
    else:
        print("Opção invalida")    
    ano = str(input("\nCadastre o ano do filme (AAAA): "))
    disponivel = str(input("\nO filme está disponível? (Sim/Não): "))
    filmes = {
        "ID": len(cadastro_filmes) + 1,
        "Nome": nome,
        "Genero": genero,
        "Ano": ano,
        "Disponível": disponivel
    }
    cadastro_filmes.append(filmes)
    print("\nFilme cadastrado!!!")
    
def pgenero(): #Procurar pelo gênero 8
    print("\nEscolha por gênero\n")
    linha()
    print('''
        1 - Drama 
        2 - Ação 
        3 - Animação 
        4 - Suspense 
        5 - Policial 
        6 - Comedia 
        7 - Ficção
        ''')
    linha()
    genero = int(input("Escolha o genero (1 a 7 ): "))
    if genero == 1:
        genero = "Drama"
    elif genero == 2:
        genero = "Ação"
    elif genero == 3:
        genero = "Animação"
    elif genero == 4:
        genero = "Suspense"
    elif genero == 5:
        genero = "Policial"
    elif genero == 6:
        genero = "Comédia"
    elif genero == 7:
        genero = "Ficção"
    else:
        print("Opção invalida")
    for filme in cadastro_filmes:
        if filme["Genero"] == genero:
            print(f"{filme['Nome']} | {filme['Genero']} | {filme['Ano']} | {filme['Disponível']}")
