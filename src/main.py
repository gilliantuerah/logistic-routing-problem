from graph import graph, kurirRute

# Input kantor pusat dan tujuan untuk ditampilkan upagraf
tujuan = []
pusat = str(input("Masukkan Kantor Pusat : "))
n = int(input("Masukkan banyaknya kota tujuan : "))
print("Masukkan kota tujuan : ")
for i in range(n):
    ele = str(input())
    tujuan.append(ele)

matriks = graph(pusat, tujuan)

# input banyaknya kurir dan tujuan kurir untuk ditampilkan jalur terpendek dari setiap kurir
nKurir = int(input("Masukkan banyaknya kurir : "))
for i in range(nKurir):
    tujuanKurir = []
    nKota = int(input("Masukkan banyaknya kota tujuan : "))
    print("Masukkan kota tujuan : ")
    for i in range(nKota):
        ele = str(input())
        if (ele not in tujuan):
            # pesan kesalahan
            print(
                "Kota "+ele+" tidak ada dalam kota tujuan.")
        elif(ele in tujuanKurir):
            print("Kota "+ele+" sudah pernah dimasukkan sebelumnya.")
        else:
            tujuanKurir.append(ele)
    if(len(tujuanKurir) != 0):
        kurirRute(matriks, pusat, tujuanKurir)
