#1 - Listar catálogo") #com status de disponibilidade"

cadastro_filmes = [
     {"ID": 1,  "Nome": "Um Sonho de Liberdade",          "Genero": "Drama",       "Ano": "1994", "Disponível": "Sim"},
    {"ID": 2,  "Nome": "O Poderoso Chefão",              "Genero": "Policial",    "Ano": "1972", "Disponível": "Sim"},
    {"ID": 3,  "Nome": "Batman: O Cavaleiro das Trevas", "Genero": "Ação",        "Ano": "2008", "Disponível": "Sim"},
    {"ID": 4,  "Nome": "A Lista de Schindler",           "Genero": "Drama",       "Ano": "1993", "Disponível": "Sim"},
    {"ID": 5,  "Nome": "Avatar",                         "Genero": "Ficção",      "Ano": "2009", "Disponível": "Sim"},
    {"ID": 6,  "Nome": "Vingadores: Ultimato",           "Genero": "Ação",        "Ano": "2019", "Disponível": "Sim"},
    {"ID": 7,  "Nome": "Titanic",                        "Genero": "Drama",       "Ano": "1997", "Disponível": "Sim"},
    {"ID": 8,  "Nome": "Deus e o Diabo na Terra do Sol", "Genero": "Drama",       "Ano": "1964", "Disponível": "Sim"},
    {"ID": 9,  "Nome": "Central do Brasil",              "Genero": "Drama",       "Ano": "1998", "Disponível": "Sim"},
    {"ID": 10, "Nome": "Cidade de Deus",                 "Genero": "Policial",    "Ano": "2002", "Disponível": "Sim"},
    {"ID": 11, "Nome": "Zootopia 2",                     "Genero": "Animação",    "Ano": "2025", "Disponível": "Sim"},
    {"ID": 12, "Nome": "Uma Batalha Após a Outra",       "Genero": "Suspense",    "Ano": "2025", "Disponível": "Sim"},
    {"ID": 13, "Nome": "Parasita",                       "Genero": "Suspense",    "Ano": "2019", "Disponível": "Sim"},
]

fila_reserva = []

pilha_devolucao = [] 

registro_alugel = []

registro_devolucao = []

disponivel = ("Sim", "Não")
