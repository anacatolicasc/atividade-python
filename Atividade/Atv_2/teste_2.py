from main_2 import gerar_lista, intervalo, ordenacao


def test_tamanho():
  lista_aleat = gerar_lista(20000)
  assert len(lista_aleat) == 20000


def test_intervalo():
  lista_aleat = gerar_lista(20000)
  assert intervalo(lista_aleat)


def test_ordenacao():
  lista_aleat = gerar_lista(20000)
  ordenacao(lista_aleat)
  print(lista_aleat)
  assert all(lista_aleat[i] <= lista_aleat[i + 1]
             for i in range(len(lista_aleat) - 1))
