from functools import reduce

movies = [
    {"title": "Avengers: Endgame", "year": 2019, "rating": 8.4, "genre": "Action"},
    {"title": "Parasite", "year": 2019, "rating": 8.6, "genre": "Drama"},
    {"title": "Nomadland", "year": 2020, "rating": 7.3, "genre": "Drama"},
    {"title": "Dune", "year": 2021, "rating": 7.9, "genre": "Sci-Fi"},
    {"title": "Spider-Man No Way Home", "year": 2021, "rating": 7.6, "genre": "Action"},
    {"title": "The French Dispatch", "year": 2021, "rating": 7.0, "genre": "Comedy"},
    {"title": "A Quiet Place Part II", "year": 2020, "rating": 7.4, "genre": "Horror"},
    {"title": "No Time to Die", "year": 2021, "rating": 6.8, "genre": "Action"},
    {"title": "The Power of the Dog", "year": 2021, "rating": 7.3, "genre": "Drama"},
    {"title": "Eternals", "year": 2021, "rating": 6.4, "genre": "Action"},
    {"title": "The Last Duel", "year": 2021, "rating": 7.0, "genre": "Drama"},
]

def hitung_jumlah_film_berdasarkan_genre(genre):
    filtered_movies = list(filter(lambda movie: movie["genre"] == genre, movies))
    return len(filtered_movies)

def hitung_rata_rata_rating_berdasarkan_tahun(year):
    year_movies = list(filter(lambda movie: movie["year"] == year, movies))
    ratings = list(map(lambda movie: movie["rating"], year_movies))
    total_rating = reduce(lambda x, y: x + y, ratings, 0)
    return total_rating / len(ratings) if ratings else 0

def cari_film_dengan_rating_tertinggi():
    return max(movies, key=lambda movie: movie["rating"])

def tampilkan_info_film(movie):
    print("Informasi Film:", movie["title"])
    print("Rating:", movie["rating"])
    print("Tahun rilis:", movie["year"])
    print("Genre:", movie["genre"])
    print()

def main():
    while True:
        print("Pilih tugas yang ingin dilakukan:")
        print("1. Menghitung jumlah film berdasarkan genre")
        print("2. Menghitung rata-rata rating film berdasarkan tahun rilis")
        print("3. Menemukan film dengan rating tertinggi")
        print("4. Cari judul film untuk menampilkan informasi rating, tahun rilis, dan genre")
        print("5. Selesai")
        task = input("Masukkan nomor tugas: ")

        if task == '1':
            genres = set(movie["genre"] for movie in movies)
            genre_count = {genre: hitung_jumlah_film_berdasarkan_genre(genre) for genre in genres}
            print("Jumlah film berdasarkan genre:")
            print(genre_count)
        elif task == '2':
            years = set(movie["year"] for movie in movies)
            avg_ratings = {year: hitung_rata_rata_rating_berdasarkan_tahun(year) for year in years}
            print("Rata-rata Rating Film berdasarkan Tahun Rilis:")
            print(avg_ratings)
        elif task == '3':
            highest_rated_movie = cari_film_dengan_rating_tertinggi()
            print("Film dengan Rating Tertinggi:")
            tampilkan_info_film(highest_rated_movie)
        elif task == '4':
            title = input("Masukkan judul film yang ingin dicari: ")
            found = False
            for movie in movies:
                if movie["title"] == title:
                    tampilkan_info_film(movie)
                    found = True
                    break
            if not found:
                print("Film dengan judul tersebut tidak ditemukan.")
        elif task == '5':
            break
        else:
            print("Pilihan tugas tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
