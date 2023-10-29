def hitung_nilai_akhir(uts, uas):
    return (uts + uas) / 2

def hitung_semua_nilai_akhir(data_mahasiswa):
    data_nilai_akhir = {}
    for nama, nilai in data_mahasiswa.items():
        nilai_akhir = hitung_nilai_akhir(nilai['uts'], nilai['uas'])
        data_nilai_akhir[nama] = nilai_akhir
    return data_nilai_akhir

def tampilkan_nilai_akhir(data_nilai_akhir):
    print("Hasil Nilai Akhir Mahasiswa:")
    for nama, nilai_akhir in data_nilai_akhir.items():
        print(f"Nama: {nama}\tNilai Akhir: {nilai_akhir:.2f}")

def main():
    data_mahasiswa = {
        'abib': {'uts': 85, 'uas': 92},
        'abib1': {'uts': 78, 'uas': 89},
        'abib2': {'uts': 92, 'uas': 86},
    }

    data_nilai_akhir = hitung_semua_nilai_akhir(data_mahasiswa)
    tampilkan_nilai_akhir(data_nilai_akhir)

if __name__ == "__main__":
    main()