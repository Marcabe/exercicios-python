L = float(input('Qual a largura da parede?'))
A = float(input('Qual a altura da parede?'))
print('Sua parede tem a dimensão de {}m x {}m e a sua  área é de {}m2 '.format(L,A,L*A))
print('Para pintar essa parede, você precisará de {}l de tinta '.format((L*A)/2))