import pytest
from src.calculator import divide

# 1. Caso Exitoso
def test_divide_success():
    assert divide(10, 2) == 5.0

# 2. Caso Borde (Edge case): El dividendo es cero
def test_divide_edge_case():
    assert divide(0, 5) == 0.0

# 3. Caso de Error: División por cero
def test_divide_error():
    with pytest.raises(ValueError, match="No se puede dividir por cero"):
        divide(10, 0)
