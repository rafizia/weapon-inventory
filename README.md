Link App: [Weapentory](https://weapentory.adaptable.app/main/)<br>

Nama: Muhammad Rafi Zia Ulhaq<br>
NPM: 2206814551<br>
Kelas: PBP B
<hr>

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

**Jawab:**

a. Membuat sebuah proyek Django baru<br>
* Inisiasi repository baru dengan perintah `git init` serta konfigurasi nama pengguna dan email
* Inisiasi repository `weapon-inventory`
* Menghubungkan repository lokal dengan repository Github dengan perintah `git branch -M main` dan `git remote add origin ...`
* Instalasi Django dan inisiasi proyek Django
* Mengunggah konfigurasi proyek ke Github

b. Membuat aplikasi dengan nama `main` pada proyek<br>
* Membuat aplikasi `main` dengan perintah `python manage.py startapp main`
* Membuat template `main.html`

c. Melakukan routing pada proyek agar dapat menjalankan aplikasi `main`<br>
* Menambahkan `main` ke `INSTALLED_APPS` di berkas `settings.py`

d. Membuat model pada aplikasi `main` dengan nama `Item`
* Mengisi berkas `models.py` dalam aplikasi `main` dengan kode:
```from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    atk = models.IntegerField()
    rarity = models.CharField(max_length=255)
    description = models.TextField()
    amount = models.IntegerField()
```
* Melakukan migrasi model sesuai tutorial 1

e. Membuat sebuah fungsi pada `views.py` untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas
* Mengisi berkas `views.py` dalam aplikasi `main`dengan kode:
```def show_main(request):
    context = {
        'app_name' : 'Weapentory',
        'name': 'Muhammad Rafi Zia Ulhaq',
        'class': 'PBP B',
    }

    return render(request, "main.html", context)
```
* Mengubah template `main.html` agar dapat menampilkan data yang telah diambil dari model

f. Membuat sebuah routing pada `urls.py` aplikasi `main` untuk memetakan fungsi yang telah dibuat pada `views.py`
* Konfigurasi `urls.py` di dalam direktori `main` sesuai tutorial 1
* Menambahkan rute URL di `urls.py` dalam direktori proyek `weapon_inventory` sesuai tutorial 1

g. Melakukan deployment ke Adaptable sesuai tutorial 0, tidak lupa mengganti start command menjadi `python manage.py migrate && gunicorn weapon_inventory.wsgi`
<br><br>


2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara `urls.py`, `views.py`, `models.py`, dan `berkas html`.

**Jawab:**

![Bagan request client](https://github.com/rafizia/weapon-inventory/blob/master/image.png?raw=true)

* Client Request: Sebuah request pertama kali diterima oleh Django dari client, seperti web browser. Request ini berisi informasi seperti URL yang dituju ataupun berupa sebuah data.

* `urls.py`: File ini berperan sebagai peta rute untuk mengarahkan request ke view yang sesuai. Saat request masuk, Django akan mencocokkan URL dengan pola yang didefinisikan dalam `urls.py`.

* `views.py`: Setelah URL yang cocok ditemukan, request akan dikirimkan ke fungsi view yang sesuai dalam `views.py`. View berfungsi untuk memproses data, memanggil model, dan mempersiapkan data untuk ditampilkan di halaman web.

* `models.py`: Models adalah representasi struktur data dalam basis data. Ketika view memerlukan akses ke data, view akan berinteraksi dengan model melalui ORM (Object-Relational Mapping) Django. Models juga digunakan untuk membuat dan mengubah data dalam basis data.

* Berkas HTML: Setelah view memproses data yang dibutuhkan, view akan menggunakan template HTML untuk menghasilkan tampilan yang akan dikirimkan kembali ke client.

* Client Response: Setelah view menghasilkan tampilan HTML, respons yang berisi halaman HTML tersebut dikirimkan kembali ke client, yang akan menampilkan konten yang dihasilkan kepada pengguna.
<br><br>


3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

**Jawab:**

Kita perlu menggunakan virtual environment saat membuat aplikasi web berbasis Django karena beberapa alasan, yaitu:
* **Isolasi Dependensi Aplikasi**<br>
Setiap aplikasi web Django memiliki dependensinya sendiri. Jika tidak menggunakan virtual environment, maka semua dependensi dari semua aplikasi akan diinstal di sistem operasi. Hal ini dapat menyebabkan konflik dependensi dan membuat aplikasi menjadi tidak stabil.

* **Memudahkan Manajemen Dependensi**<br>
Virtual environment memungkinkan kita untuk menginstal dependensi aplikasi secara terpisah dari sistem operasi. Hal ini memudahkan kita untuk memperbarui atau menghapus dependensi tanpa mempengaruhi aplikasi lain.

* **Portabilitas**<br> 
Aplikasi yang dikembangkan dalam virtual environment dapat dengan mudah dipindahkan ke sistem operasi lain.

Kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment. Namun, hal ini tidak disarankan karena dapat menyebabkan beberapa masalah seperti konflik dependensi.
<br><br>


4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.

**Jawab:**

* **MVC (Model-View-Controller)**<br>
    - **Model**: Representasi data aplikasi.<br>
    - **View**: Bertanggung jawab untuk menampilkan data dari Model dan menanggapi interaksi pengguna.<br>
    - **Controller**: Menerima masukan dari pengguna, memprosesnya, dan memutuskan bagaimana Model dan View harus berinteraksi.<br>
    - **Perbedaan utama**: Dalam pola MVC, Model dan View tidak berinteraksi secara langsung. Interaksi antara keduanya dikendalikan oleh Controller.

* **MVT (Model-View-Template)**<br>
    - **Model**: Representasi data aplikasi.<br>
    - **View**: Menangani tampilan data. Dalam Django, Template dan View bersama-sama bertanggung jawab untuk menghasilkan tampilan.<br>
    - **Template**: Berisi tampilan HTML yang memungkinkan penggunaan sintaks template khusus Django untuk menggabungkan data dari Model ke dalam tampilan.<br>
    - **Perbedaan utama**: MVT adalah adaptasi dari MVC, tetapi dalam MVT, Template memainkan peran yang lebih kuat dalam menghasilkan tampilan, sedangkan View mengelola logika aplikasi.

* **MVVM (Model-View-ViewModel)**<br>
    - **Model**: Representasi data aplikasi.<br>
    - **View**: Merupakan representasi tampilan yang dikendalikan oleh ViewModel. View dalam MVVM biasanya lebih pasif dan hanya menampilkan data yang disediakan oleh ViewModel.<br>
    - **ViewModel**: Bertanggung jawab untuk mengelola tampilan dan menyediakan data yang diperlukan oleh View.<br>
    - **Perbedaan utama**: MVVM memperkenalkan ViewModel yang berperan penting dalam menghubungkan Model dengan View. ViewModel menyediakan data dan perilaku yang diperlukan oleh View.