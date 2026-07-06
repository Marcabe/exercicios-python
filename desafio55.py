todos_os_pesos = []

for c in range(1, 6):
    peso = int(input(f'Digite o peso da {c}ª pessoa: '))
    todos_os_pesos.append(peso)

print('Todos os pesos:', todos_os_pesos)
print('O maior peso foi:', max(todos_os_pesos))
print('O menor peso foi:', min(todos_os_pesos))