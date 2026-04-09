import json
import os
from datetime import datetime
ARQUIVO_HISTORICO = "historico.json"

def salvar_operacao(tipo, valores, resultado):
    with open(ARQUIVO_HISTORICO, "r") as f:
        historico = json.load(f)

    historico.append({
        "tipo": tipo,
        "valores": valores,
        "resultado": resultado,
        "data": datetime.now().isoformat()
    })

    with open(ARQUIVO_HISTORICO, "w") as f:
        json.dump(historico, f, indent=2)

def listar_historico():
    with open(ARQUIVO_HISTORICO, "r") as f:
        historico = json.load(f)

    if not historico:
        print("Nenhuma operação registrada.")
        return

    print("\nHistórico de operações:")
    for i, op in enumerate(historico, 1):
        print(f"{i}. {op['tipo']} {op['valores']} = {op['resultado']} ({op['data']})")

# garante que o arquivo existe
def inicializar_historico():
    if not os.path.exists(ARQUIVO_HISTORICO):
        with open(ARQUIVO_HISTORICO, "w") as f:
            json.dump([], f)

def somar(a, b):
    resultado = a + b
    return resultado


def subtrair(a, b):
    resultado = a - b
    return resultado


def multiplicar(a, b):
    resultado = a * b
    return resultado


def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("Não é possível dividir por zero.")
    resultado = a / b
    return resultado


def bhaskara(a, b, c):
    import math

    delta = b**2 - 4*a*c

    if delta < 0:
        resultado = "Não existem raízes reais."
    elif delta == 0:
        x = -b / (2*a)
        resultado = f"Existe uma raiz real: x = {x}"
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        resultado = f"x1 = {x1}, x2 = {x2}"

    return resultado


def calcular():
    inicializar_historico()

    print("Calculadora Básica")
    print("Operações: +, -, *, /, b (Bhaskara)")

    while True:
        try:
            opcao = input("\n1 - Operações básicas\n2 - Bhaskara\n3 - Ver histórico\nEscolha: ").strip()

            if opcao == "3":
				# todo: implementar função para ler e exibir histórico
                continue

            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))

            if opcao == "1":
                operacao = input("Digite a operação (+, -, *, /): ").strip()

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

            elif opcao == "2":
                c = float(input("Digite o terceiro número: "))
                resultado = bhaskara(a, b, c)

            else:
                print("Opção inválida.")
                continue

            print(f"Resultado: {resultado}")

        except ValueError:
            print("Entrada inválida.")
        except ZeroDivisionError as e:
            print(e)

        continuar = input("Deseja continuar? (s/n): ").strip().lower()
        if continuar != "s":
            print("Encerrando calculadora.")
            break


if __name__ == "__main__":
    calcular()