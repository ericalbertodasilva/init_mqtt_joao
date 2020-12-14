import time


def read_topics():
    print("Abrir conexão a broker")
    print("Ler topicos e salvar em uma variavel")
    print("Fechar conexão com broker")
    print("Retornar um list ou dic com valores dos topicos")
    return None

def white_values(values):
    print("Abrir conexão com banco de dados")
    print("Gravar valores")
    print("Fechar conexao com banco de dados")

def status_machine(status_row):
    if status_row == 0:
        print("Iniciado o sistema")
        print("Mudando o estado")
        if status_row == 0:
            print("Estado igual 1")
            return 1
    
    if status_row == 1:
        values = read_topics()
        white_values(values)
        print("Mudando o estado")
        if status_row == 1:
            print("Estado igual 2")
            return 1

if __name__ == "__main__":
    status_row = 0
    while True:
        status_row = status_machine(status_row)
        time.sleep(30)