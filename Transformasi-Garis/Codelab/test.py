# Curry function
def perkalian(a):
    def dengan(b):
        return a * b
    return dengan

total = perkalian(5)
print("Hasil perkalian menggunakan HOF:", total(3))

hasil_currying = perkalian(5)(3)
print("Hasil Currying:", hasil_currying)
