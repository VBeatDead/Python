def point(x, y):
    return x, y

def line_equation_of(p1, p2):
    def calculate_slope(point1, point2):
        return (point2[1] - point1[1]) / (point2[0] - point1[0])

    M = calculate_slope(p1, p2)
    C = p1[1] - M * p1[0]

    return f"y = {M:.2f}x + {C:.2f}"

titik_A = point(1, 3)
titik_B = point(3, 1)

persamaan_garis = line_equation_of(titik_A, titik_B)

print("Persamaan garis yang melalui titik A dan B:")
print(persamaan_garis)