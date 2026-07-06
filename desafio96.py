def area(largura, comprimento):
    resultado = largura * comprimento
    print(f'A área do terreno é {resultado:.2f} m²')


largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))

area(largura, comprimento)

