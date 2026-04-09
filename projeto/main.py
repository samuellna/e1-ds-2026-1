def somar(a, b):
	return a + b


def subtrair(a, b):
	return a - b


def multiplicar(a, b):
	return a * b


def dividir(a, b):
	if b == 0:
		raise ZeroDivisionError("Não é possível dividir por zero.")
	return a / b

def bhaskara(a, b, c):
	import math

	delta = b**2 - 4*a*c

	if delta < 0:
		return "Não existem raízes reais."
	elif delta == 0:
		x = -b / (2*a)
		return f"Existe uma raiz real: x = {x}"
	else:
		x1 = (-b + math.sqrt(delta)) / (2*a)
		x2 = (-b - math.sqrt(delta)) / (2*a)
		return f"Existem duas raízes reais: x1 = {x1}, x2 = {x2}"

def calcular():
	print("Calculadora Básica")
	print("Operações: +, -, *, /, b (Bhaskara)")

	while True:
		try:
			opcao = input("1 - Operações básicas\n2 - Calcular raízes\nDigite uma opção: ").strip().lower()
			a = float(input("Digite o primeiro número: "))
			b = float(input("Digite o segundo número: "))
			if opcao == "1":
				operacao = input("Digite a operação (+, -, *, /): ").strip().lower()
				if operacao == "+":
					resultado = somar(a, b)
				elif operacao == "-":
					resultado = subtrair(a, b)
				elif operacao == "*":
					resultado = multiplicar(a, b)
				elif operacao == "/":
					resultado = dividir(a, b)
			elif opcao == "2":
				c = float(input("Digite o terceiro número: "))
				resultado = bhaskara(a, b, c)
			else:
				print("Operação inválida.")
				continue

			print(f"Resultado: {resultado}")
   
		except ValueError:
			print("Entrada inválida. Digite números válidos.")
		except ZeroDivisionError as e:
			print(e)

		continuar = input("Deseja fazer outra operação? (s/n): ").strip().lower()
		if continuar != "s":
			print("Encerrando calculadora.")
			break


if __name__ == "__main__":
	calcular()
