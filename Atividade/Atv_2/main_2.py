import random


def gerar_lista(tamanho):
  return [random.randint(-999999, 999999) for _ in range(tamanho)]


def intervalo(array):
  return all(-999999 <= valor <= 999999 for valor in array)


def ordenacao(array):
  n = len(array)
  for i in range(n - 1):
    for j in range(0, n - i - 1):
      if array[j] > array[j + 1]:
        array[j], array[j + 1] = array[j + 1], array[j]
