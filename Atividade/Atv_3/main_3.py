import pytest


def massa_lunar(massa):
  return massa / 6


def dist_marte(metros):
  grav_terra = 9.81
  grav_marte = 3.71
  return (grav_terra / grav_marte) * metros
