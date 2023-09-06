from main_1 import gerar_lista, intervalo


def test_tamanho_do_array():
  array_aleatorio = gerar_lista(20000)
  print(array_aleatorio)
  assert len(array_aleatorio) == 20000


def test_valores_no_intervalo():
  array_aleatorio = gerar_lista(20000)
  assert intervalo(array_aleatorio)


test_tamanho_do_array()
