import math

def point(x, y):
    return x, y

def line_equation_of(x1, y1, M, C):
    return f"Y = {M:.2f}X + {C:.2f}"

def transformasi_decorator(func):
    def wrapper(x, y, gradien, tx, ty, sx, sy):
        # Translasi
        x_translated = x + tx
        y_translated = y + ty

        # Rotasi
        sudut_radian = math.radians(60)
        x_rotated = x_translated * math.cos(sudut_radian) - y_translated * math.sin(sudut_radian)
        y_rotated = x_translated * math.sin(sudut_radian) + y_translated * math.cos(sudut_radian)

        # Dilatasi
        x_transformed = x_rotated * sx
        y_transformed = y_rotated * sy

        # Menampilkan hasil transformasi
        print("Titik setelah transformasi:")
        print(f"X = {x_transformed:.2f}, Y = {y_transformed:.2f}")

        # Menghitung persamaan garis setelah transformasi
        M_transformed = gradien * sx
        C_transformed = y_transformed - M_transformed * x_transformed

        return func(x_transformed, y_transformed, M_transformed, C_transformed)

    return wrapper

@transformasi_decorator
def line_equation_of_transformed(x, y, M, C):
    return f"Persamaan garis baru setelah transformasi:\nY = {M:.2f}X + {C:.2f}"

# Input dari user
x, y = map(int, input("Masukkan koordinat titik A (contoh: 3 4): ").split())
gradien = float(input("Masukkan gradien: "))
tx, ty = map(float, input("Masukkan translasi tx dan ty (contoh: 2 -3): ").split())
sx, sy = map(float, input("Masukkan faktor skala sx dan sy (contoh: 1.5 2): ").split())

# Menghitung persamaan garis sebelum transformasi
persamaan_garis_sebelum = line_equation_of(x, y, gradien, y - gradien * x)
print(f"\nPersamaan garis sebelum transformasi:\n{persamaan_garis_sebelum}")

# Menghitung persamaan garis setelah transformasi dengan decorator
persamaan_garis_transformed = line_equation_of_transformed(x, y, gradien, tx, ty, sx, sy)
print("\n" + persamaan_garis_transformed)
