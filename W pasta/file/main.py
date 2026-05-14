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

def option():
    start()
    while True:
        op = int(input("Num: "))
        ind = 'W pro max'
        if op == 1: 
            print(ind)

        elif op == 2: 
            print(ind)

        elif op == 3: 
            print(ind)

        elif op == 4:
            print(ind)

        elif op == 5:
            print(ind)

        elif op == 6:
            print(ind)
            
        elif op == 7:
            break
        else:
            print("Opção invalida!!")
print("Cabou")