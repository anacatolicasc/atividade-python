import random


def gerar_lista(tamanho):
  return [random.randint(-999999, 999999) for _ in range(tamanho)]


def intervalo(array):
  return all(-999999 <= valor <= 999999 for valor in array)
