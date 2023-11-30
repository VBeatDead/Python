# Line Equation Transformation

This Python script performs a linear transformation on a given line equation. It includes translation and scaling operations based on user input.

## Usage

1. Run the script.
2. Enter the values when prompted for:
   - `x`, `y`, and `gradien` for the original line equation.
   - `tx` and `ty` for translation in the x and y directions.
   - `sx` and `sy` for scaling in the x and y directions.

## Transformation Function

The script defines a transformation function `transformasi_gabungan` that takes the original line equation function as an argument. The transformation includes translation, rotation, and scaling. The transformed result is then displayed.

```python
@transformasi_gabungan
def line_equation_of(x, y, gradien, tx, ty, sx, sy):
    C = y - gradien * x
    return f"Y = {gradien:.2f}x + {C:.2f}"
```

## Example

```python
x, y, gradien = map(int, input("Masukkan nilai x, y, dan gradien (pisahkan dengan spasi): ").split())
tx, ty = map(float, input("Masukkan nilai tx dan ty untuk translasi (pisahkan dengan spasi): ").split())
sx, sy = map(float, input("Masukkan nilai sx dan sy untuk perbesaran skala (pisahkan dengan spasi): ").split())

persamaan_garis_transformasi = line_equation_of(x, y, gradien, tx, ty, sx, sy)

print(f"\nPersamaan garis melalui titik ({x},{y}) dan bergradien {gradien}:")
print(f"Y = {gradien:.2f}x + {-gradien * x + y:.2f}")
print("\nPersamaan garis baru setelah transformasi:")
print(persamaan_garis_transformasi)
```

## Dependencies

- Python 3
- `math` module