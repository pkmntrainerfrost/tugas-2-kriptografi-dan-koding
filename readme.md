# Tugas 1 II4031 Kriptografi dan Koding
## Dibuat oleh:
- 18221115 Christopher Febrian Nugraha
- 18221102 Salman Ma'arif Achsien

# Deskripsi Tugas 
Mahasiswa ditugaskan untuk membuat ragam cipher klasik dapat dijalankan melalui program melalui perantara GUI dengan bahasa pemrograman yang dibebaskan. Mahasiswa **DILARANG** untuk menggunakan modul yang sudah terdefinisi unutuk membuat cipher-cipher yang akan diimplementasikan. Adapun cipher yang ditugaskan diantaranya:
1. Vigenere Cipher (26 huruf alfabet)
2. Affine Cipher (26 huruf alfabet)
3. Playfair Cipher (26 huruf alfabet)
4. Autokey Cipher (26 huruf alfabet)
5. Extended Vigenere Cipher (256 karakter ASCII)
6. Product Cipher (26 huruf alfabet)

# Spesifikasi
- Program dapat menerima _message_ (ke depannya disebut _plaintext_) berupa teks yang diketikkan dari _keyboard_ atau file sembarang (file .txt maupun file biner).
- Program dapat mengenkripsi _plaintext_ dari masukan pengguna. Selain dari algoritma _Extended Vigenere Cipher_, program hanya mengenkripsi karakter alfabet saja. Angka, spasi, tanda baca, dan simbol lainnya diabaikan dan dibuang saat _ciphertext_ ditampilkan atau disimpan sebagai file.
- Untuk algoritma _Playfair Cipher_, konsensus yang diambil jika terdapat dua huruf X yang muncul berturut-turut dalam _plaintext_ adalah untuk mengganti huruf X dengan huruf lain (seperti Q ataupun Z) sebagai karakter yang diselipkan jika terdapat dua huruf yang muncul berturut-turut dalam _plaintext_.
- Program dapat mendekripsi _ciphertext_ menjadi _plaintext_ semula sehingga dapat dibuka atau diinterpretasikan seperti semula sebelum enkripsi.
- Untuk _plaintext_ berupa teks masukan pengguna, program akan menampilkan _plaintext_ dan _ciphertext_ di layar. Hal ini tidak terjadi bagi _plaintext_ berupa file dari pengguna.
- Program dapat menyimpan _ciphertext_ yang sudah dihasilkan ke dalam file .dat dalam direktori tertentu.
- Kunci dari masing-masing algoritma dimasukkan oleh pengguna. Panjang kunci bebas. Khusus algoritma _Affine Cipher_ dan _Product Cipher_, terdapat kunci tambahan yang harus dimasukkan, yaitu kunci B untuk _Affine_ dan kunci transposisi untuk _Product_.
- Untuk enkripsi _plaintext_ file sembarang pada algoritma _Extended Vigenere Cipher_, setiap file diperlakukan sebagai file of bytes. Program membaca setiap byte di dalam file (termasuk byte-byte header file) dan mengenkripsinya. Dengan melakukan dekripsi, maka file tersebut dapat dibuka kembali oleh aplikasinya.

# Cara Menjalankan Aplikasi pada Windows OS
## Bagian 1: Persiapan dan Instalasi
1. Clone repositori ini ke perangkat komputer Anda.
2. Buatlah sebuah _virtual environment_ baru dengan menjalankan kode berikut terminal CLI Windows:
    > py -m venv venv
    - Pastikan terlebih dahulu Anda sudah memiliki _Python_ yang terinstal. Jika belum, Anda dapat melihat panduan [berikut ini](https://docs.python.org/3/using/windows.html#using-on-windows).
    - Pastikan juga Anda berada pada _root_ dari folder repositori ini sebelum membuat _virtual environment_.
3. Jalankan _virtual environment_ yang baru saja dibuat dengan menggunakan kode berikut:
    > venv/Scripts/activate
4. Lakukan instalasi modul yang diperlukan untuk aplikasi ini dengan menjalankan kode ini:
    > pip install fastapi uvicorn python-multipart Jinja2
    - Modul **fastapi** digunakan untuk mengatur API antara server dan klien.
    - Modul **uvicorn** digunakan untuk menginisiasi server.
    - Modul **python-multipart** digunakan untuk menangani permintaan POST berbentuk form-data dari klien.
    - Modul **Jinja2** digunakan untuk mempermudah routing antara laman-laman HTML.
## Bagian 2: Eksekusi dan Penggunaan
1. Jalankan file main.py dengan menggunakan kode berikut:
    > py Backend/main.py
2. Modul uvicorn akan menginisiasi server. Jika tertulis "Application startup complete." ini berarti server telah siap digunakan.
3. Akses IP Address yang muncul pada layar terminal (dalam hal ini bagian 0.0.0.0 dapat digantikan dengan localhost menjadi http://localhost:8000).
4. Anda sudah bisa menggunakan algoritma yang tersedia dan selamat mencoba beragam _cipher_ yang ingin digunakan.
