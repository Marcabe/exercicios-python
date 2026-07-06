import math

num1 = float(input('Digite um angulo qualquer: '))

sin = math.sin(math.radians(num1))
cos = math.cos(math.radians(num1))
tan = math.tan(math.radians(num1))

print('O número digitado foi {}, o seu seno é {:.2f}, cosseno {:.2f} e a sua tangente {:.2f}'.format(num1, sin, cos, tan))
