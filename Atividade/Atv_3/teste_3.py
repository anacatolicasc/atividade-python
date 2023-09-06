from main_3 import massa_lunar, dist_marte
import pytest


def teste_convert_massa():
  assert massa_lunar(6) == 1
  assert massa_lunar(12) == 2
  assert massa_lunar(0) == 0


def teste_convert_dist():
  assert dist_marte(10) == pytest.approx(26.48, rel=1e-2)
  assert dist_marte(20) == pytest.approx(52.96, rel=1e-2)
  assert dist_marte(0) == 0
