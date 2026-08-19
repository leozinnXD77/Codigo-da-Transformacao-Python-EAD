import faker
import utilidades
import time
import datetime

num1 = 10
num2 = 5
num3 = 12
num4 = 8
num5 = 6
num6 = 14
num7 = 20
num8 = 21
num9 = 17
num10 = 16

print("\n","=" * 40)
print("\n📐Teste de Utilidades📐")
time.sleep(2)
print(f"\nNúmeros Utilizados: {num1} e {num2}\n")
time.sleep(3)
print(f"\nUsando Adição ({num1} + {num2}):",utilidades.soma(num1, num2))
time.sleep(3)
print(f"\nUsando Subtração ({num1} - {num2}):",utilidades.subtracao(num1, num2))
time.sleep(2)
print(f"\nUsando Multiplicação ({num1} * {num2}):",utilidades.multiplicacao(num1, num2))
time.sleep(2)
print(f"\nUsando Divisão ({num1} / {num2}):",utilidades.divisao(num1, num2))
time.sleep(2)
print(f"\nUsando Potência ({num1} ** {num2}):",utilidades.potencia(num1, num2))
time.sleep(2)
print(f"\nUsando o Resto da Divisão ({num1} % {num2}):",utilidades.resto_divisao(num1, num2))
time.sleep(2)
print(f"\nUsando a Divisão Completa ({num1} // {num2}):",utilidades.divisao_inteira(num1, num2))
time.sleep(2)
print("\n","=" * 40)
