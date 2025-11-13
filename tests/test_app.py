import sys
from pathlib import Path

# Asegurar que la carpeta raíz del proyecto esté en sys.path
ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from app import sum_numbers


def test_sum_numbers_positive():
    assert sum_numbers(2, 3) == 5


def test_sum_numbers_negative():
    assert sum_numbers(-1, -4) == -5
