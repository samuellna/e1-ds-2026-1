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


def calcular():
	print("Calculadora Básica")
	print("Operações: +, -, *, /")

	while True:
		try:
			a = float(input("Digite o primeiro número: "))
			operacao = input("Digite a operação (+, -, *, /): ").strip()
			b = float(input("Digite o segundo número: "))

			if operacao == "+":
				resultado = somar(a, b)
			elif operacao == "-":
				resultado = subtrair(a, b)
			elif operacao == "*":
				resultado = multiplicar(a, b)
			elif operacao == "/":
				resultado = dividir(a, b)
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
