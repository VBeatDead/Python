import math

def transformasi_gabungan(func):
    def wrapper(x, y, gradien, tx, ty, sx, sy):
        x, y = x + tx, y + ty
        
        sudut_radian = math.radians(60)
        x, y = x * math.cos(sudut_radian) - y * math.sin(sudut_radian), \
               x * math.sin(sudut_radian) + y * math.cos(sudut_radian)
        
        x, y = x * sx, y * sy
        
        transformed_result = func(x, y, gradien, tx, ty, sx, sy)
        return transformed_result
    return wrapper

@transformasi_gabungan
def line_equation_of(x, y, gradien, tx, ty, sx, sy):
    C = y - gradien * x
    return f"Y = {gradien:.2f}x + {C:.2f}"

x, y, gradien = map(int, input("Masukkan nilai x, y, dan gradien (pisahkan dengan spasi): ").split())
tx, ty = map(float, input("Masukkan nilai tx dan ty untuk translasi (pisahkan dengan spasi): ").split())
sx, sy = map(float, input("Masukkan nilai sx dan sy untuk perbesaran skala (pisahkan dengan spasi): ").split())

persamaan_garis_transformasi = line_equation_of(x, y, gradien, tx, ty, sx, sy)

print(f"\nPersamaan garis melalui titik ({x},{y}) dan bergradien {gradien}:")
print(f"Y = {gradien:.2f}x + {-gradien * x + y:.2f}")
print("\nPersamaan garis baru setelah transformasi:")
print(persamaan_garis_transformasi)
