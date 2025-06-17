import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import interes_simple, interes_compuesto, cuota_prestamo, valor_futuro_aportes

def test_interes_simple():
    assert interes_simple(1000, 0.05, 2) == 100.0

def test_interes_compuesto():
    assert round(interes_compuesto(1000, 0.05, 2), 2) == 1102.5

def test_cuota_prestamo():
    cuota = cuota_prestamo(10000, 0.02, 12)
    assert round(cuota, 2) == 945.6  # ✅ Valor correcto según fórmula sistema francés

def test_valor_futuro_aportes():
    valor = valor_futuro_aportes(500, 0.01, 12)
    assert round(valor, 2) == 6341.25  # ✅ Valor correcto según fórmula de anualidades
