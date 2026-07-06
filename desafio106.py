from time import sleep


def titulo(msg, cor=0):
    tamanho = len(msg) + 4
    print(f'\033[{cor}m', end='')
    print('~' * tamanho)
    print(f'  {msg}')
    print('~' * tamanho)
    print('\033[m', end='')


def ajuda(comando):
    titulo(f'Acessando o manual do comando "{comando}"', 44)
    sleep(1)
    print('\033[7;40m', end='')
    help(comando)
    print('\033[m', end='')


while True:
    titulo('SISTEMA DE AJUDA PyHELP', 42)

    comando = input('Função ou biblioteca > ').strip()

    if comando.upper() == 'FIM':
        titulo('ATÉ LOGO!', 41)
        break

    ajuda(comando)