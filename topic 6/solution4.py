"""Суммы диагоналей квадратной матрицы из файла."""
from pathlib import Path
import sys

def read_matrix(path):
    return [list(map(int, line.split()))
            for line in path.read_text(encoding="utf-8").splitlines()]


path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_name("matrix.txt")
matrix = read_matrix(path)
n = len(matrix)
main_sum = sum(matrix[i][i] for i in range(n))
secondary_sum = sum(matrix[i][n - i - 1] for i in range(n))
print(f"Сумма главной диагонали: {main_sum}")
print(f"Сумма второстепенной диагонали: {secondary_sum}")
