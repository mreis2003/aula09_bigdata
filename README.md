def dobro(x):
  r = x * 2
  return r
num = float(input('informe o numero: '))

resultado = dobro(num)

print(f'o dobro do numero é: {resultado}')


def calcular_operacoes(numero: float) -> tuple[float, float, float]:
  dobro = numero * 2
  triplo = numero * 3
  quadrado = numero * 4

  return dobro, triplo, quadrado


# Exemplo de uso:
valor = float(input("Digite um número: "))
dobro, triplo, quadrado = calcular_operacoes(valor)

print(f"Dobro: {dobro}")
print(f"Triplo: {triplo}")
print(f"Quadrado: {quadrado}")


      
