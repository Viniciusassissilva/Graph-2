import Funções


def menu_arquivos():
    print("Informe o arquivo que deseja abrir:\n"
          "Arquivo 1 (teste) = 1\n"
          "Arquivo 2 (a280) = 2\n"
          "Arquivo 3 (ali535) = 3\n"
          "Arquivo 4 (ch130) = 4\n"
          "Arquivo 5 (fl1577) = 5\n"
          "Arquivo 6 (gr666) = 6\n"
          "Sair do programa = 0")


def escolha_arquivo():
    menu_arquivos()
    entrada = int(input("Arquivo: "))

    while entrada != 0:
        if entrada == 1:
            arquivo = open("teste.txt", "r")
            nome = "teste"
            return (arquivo, nome, entrada)
        elif entrada == 2:
            arquivo = open("a280.txt", "r")
            nome = "a280"
            return (arquivo, nome, entrada)
        elif entrada == 3:
            arquivo = open("ali535.txt", "r")
            nome = "ali535"
            return (arquivo, nome, entrada)
        elif entrada == 4:
            arquivo = open("ch130.txt", "r")
            nome = "ch130"
            return (arquivo, nome, entrada)
        elif entrada == 5:
            arquivo = open("fl1577.txt", "r")
            nome = "fl1577"
            return (arquivo, nome, entrada)
        elif entrada == 6:
            arquivo = open("gr666.txt", "r")
            nome = "gr666"
            return (arquivo, nome, entrada)
        else:
            menu_arquivos()
            entrada = int(input("Arquivo: "))
    return (0, 0, 0)


def caixeiro(tempo, lista, matriz, saida):
    percuso = Funções.contrutivo(lista)
    tamanho1 = Funções.tamnhanho_percuso(percuso, matriz)
    refinamento = Funções.refinamento(tempo, percuso, matriz)
    tamanho2 = Funções.tamnhanho_percuso(refinamento, matriz)
    print("\nRota normal: ", tamanho1, "\n"
                                       "Rota refinada : ", tamanho2)
    saida.write("%f" % (tamanho2) + '\n')
    for i in refinamento:
        saida.write("%d " % i)
    saida.write("\n" + "---------------------" + "\n")


def menu_prinicipal():
    arq, nome, entrada = escolha_arquivo()
    saida = open("saida.txt", "w")

    while entrada != 0:

        lista = Funções.lista(arq)
        matriz = Funções.matriz(arq)

        saida.write(">>>>>>>> " + "Nome do Arquivo: " + nome + '\n')
        tempo = int(input("Informe o tempo de duração do refinamento(segundos): "))
        rep = int(input("Informe o numero de testes: "))

        while rep > 0:
            caixeiro(tempo, lista, matriz, saida)
            rep = rep - 1

        arq, nome, entrada = escolha_arquivo()

    saida.close()



