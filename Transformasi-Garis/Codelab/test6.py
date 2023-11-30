def point(x, y):
    return x, y

def line_equation_of(x1, y1, M):
    C = y1 - M * x1
    return f"y = {M:.2f}x + {C:.2f}"

x1, y1 = 3, 3
gradien = 1

persamaan_garis = line_equation_of(x1, y1, gradien)

print("Persamaan garis yang melalui titik (3,3) dan bergradien 1:")
print(persamaan_garis)