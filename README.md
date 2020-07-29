# Logistic Routing Problem

<img src="https://picjumbo.com/wp-content/uploads/white-tir-truck-in-motion-driving-on-highway_free_stock_photos_picjumbo_DSC04205-1080x720.jpg" class="img-responsive" width="50%" height="50%"><img src="https://upload.wikimedia.org/wikipedia/commons/1/1a/Luftaufnahmen_Nordseekueste_2013_05_by-RaBoe_tele_46.jpg" class="img-responsive" width="50%" height="50%">

Oleh :
* Felicia Gillian Tekad Tuerah
* 13518070

## Deskripsi Masalah
Welcome to **Oldenburg** ! Kota kecil cantik ini merupakan sebuah kota kecil di barat lau kota Bremen , Jerman , dengan penduduk kurang lebih 168 ribu jiwa [2018]. Kota kecil ini cocok menjadi lahan uji coba untuk melakukan pemodelan sederhana pembuatan rute pengantaran logistik.<br>
Setiap beberapa jam sekali, sebuah perusahaan logistik akan mengirimkan beberapa kurirnya untuk mengantar barang dari kantor pusat mereka ke beberapa titik tujuan yang tersebar di penjuru kota Oldenburg. Anda diminta untuk mencari rute untuk seluruh kurir sehingga jarak yang ditempuh oleh semua kurir paling kecil, sehingga perusahaan logistik dapat menghemat biaya bensin.

## Multiple-Agent TSP
Masalah pengantaran barang untuk satu kendaraan dengan fungsi objektif jarak minimal dapat dimodelkan oleh Travelling Salesman Problem. Akan tetapi, perusahaan logistik biasanya memiliki lebih dari satu kendaraan yang berangkat bersamaan, sehingga TSP kurang cocok digunakan. Generalisasi TSP untuk beberapa agen adalah **multiple-agent TSP (mTSP)**, dan model masalah ini akan kita gunakan. Pada mTSP, akan terdapat *m* tur yang akan dibangun. Syarat dari semua tur mirip dengan TSP, yaitu bahwa seluruh tur akan kembali ke simpul awal (mewakili kantor pusat) dan setiap tujuan hanya akan dilewati oleh satu tur.

## Tugas
Kita akan menggunakan dataset jalanan pada kota Oldenburg yang dapat diakses pada <a href="https://www.cs.utah.edu/~lifeifei/SpatialDataset.htm">tautan ini.</a> Lakukan pengunduhan untuk kedua data jalanan di kota Oldenburg. Data pertama merupakan koordinat simpul, data kedua merupakan data sisi antar simpul. Asumsikan seluruh jalan dua arah.<br> 
Seperti yang disebutkan sebelumnya, kita akan menggunakan pendekatan mTSP dalam permasalahan ini. Untuk mempermudah anda dan mempermudah penilaian, tugas akan dibagi dalam beberapa tahap.

## Library
Dalam menyelesaikan tugas ini, saya menggunakan beberapa library yakni:
1. **networkx** (untuk menggambar simpul dan sisi dari upagraf)
2. **matplotlib** (untuk menampilkan gambar graf )

Sebelum menjalankan program, yang perlu disiapkan adalah :
1. [Python 3.0 or above](https://www.python.org/)
2. Networkx
```
pip install networkx
```
3. Matplotlib
```
pip install matplotlib
```

Cara menjalankan program cukup mudah yakni :
1. Buka folder tempat kode disimpan
2. Menjalankan kode main dari kode sumber di terminal
```
py main.py
```
3. Kemudian, ikuti instruksi dari program

## Pendekatan Algoritma
Algoritma dibuat dengan menggunakan prinsip backtracking dan rekursif untuk memperoleh jarak terpendek dari simpul satu ke simpul lainnya. Algoritma ini digunakan untuk memperoleh upagraf dan matriks jarak dari beberapa kota tujuan dan kantor pusat terlebih dahulu. Syarat dari algoritma ini adalah tidak boleh ada kota yang terlewati dua kali. Kemudian, untuk penyelesaian mTSP memanfaatkan matriks jarak upagraf yang diperoleh sebelumnya serta memanfaatkan algoritma **Branch and Bound** dengan mengambil jarak terkecil di setiap langkahnya.

## Referensi
Silahkan gunakan referensi berikut sebagai awal pengerjaan tugas:<br>
[1] Dataset : https://www.cs.utah.edu/~lifeifei/SpatialDataset.htm<br>
[2] Pengenalan dan formulasi mTSP : https://neos-guide.org/content/multiple-traveling-salesman-problem-mtsp<br>
[3] MIP , pustaka Python untuk optimisasi : https://python-mip.readthedocs.io/en/latest/intro.html<br>
[4] OpenGL untuk Python : https://stackabuse.com/brief-introduction-to-opengl-in-python-with-pyopengl/<br>
[5]  Li, Feifei, Dihan Cheng, Marios Hadjieleftheriou, George Kollios, and Shang-Hua Teng. "On trip planning queries in spatial databases." In International symposium on spatial and temporal databases, pp. 273-290. Springer, Berlin, Heidelberg, 2005.

## Credits
Thank you for Li Fei Fei et. al. for providing the data.

