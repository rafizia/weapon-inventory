Nama: Muhammad Rafi Zia Ulhaq<br>
NPM: 2206814551<br>
Kelas: PBP B
<hr>

1. Jelaskan manfaat dari setiap *element selector* dan kapan waktu yang tepat untuk menggunakannya.

    **Jawab:**

* **Element Selector**<br>
Element selector digunakan untuk memilih semua elemen dengan jenis atau nama tertentu, seperti `<p>`, `<h1>`, `<div>`, dan lain-lain. Element selector digunakan ketika ingin menerapkan gaya yang sama pada semua elemen dengan jenis tertentu. Misalnya, jika ingin mengubah gaya teks pada semua `<h2>` menjadi berwarna biru, kita dapat menggunakan `h2` sebagai element selector.

* **ID Selector**<br>
ID selector digunakan untuk memilih elemen berdasarkan ID unik yang diberikan. ID selector digunakan ketika ingin menerapkan gaya atau interaksi khusus pada satu elemen tertentu yang memiliki ID unik. Selector ini sering digunakan untuk tujuan skriping atau navigasi.

* **Class Selector**<br>
Class selector digunakan untuk memilih elemen berdasarkan nama class yang diberikan. Class selector digunakan ketika ingin menerapkan gaya yang sama pada beberapa elemen yang memiliki class yang sama. Hal ini sangat berguna untuk mengelompokkan elemen dengan gaya yang serupa.
<br><br>


2. Jelaskan HTML5 Tag yang kamu ketahui.

    **Jawab:**

* `<header>`: Digunakan untuk mendefinisikan bagian atas atau kepala dokumen, biasanya berisi judul, logo, dan elemen navigasi situs.
* `<nav>`: Digunakan untuk menentukan bagian navigasi dari halaman web, seperti menu utama atau menu samping.
* `<section>`: Digunakan untuk mengelompokkan konten yang terkait secara tematis dalam dokumen.
* `<footer>`: Digunakan untuk mendefinisikan bagian bawah dokumen atau halaman web, biasanya berisi informasi kontak, hak cipta, atau tautan lainnya.
* `<video>` dan `<audio>`: Digunakan untuk menyisipkan video atau audio di dalam halaman web dengan kontrol pemutaran yang sesuai.
* `<form>`: Digunakan untuk membuat formulir yang memungkinkan pengguna mengirimkan data, seperti teks, pilihan, atau file, ke server web.
* `<input>`: Digunakan dalam formulir untuk membuat berbagai jenis input, seperti teks, kotak centang (checkbox), tombol radio (radio button), dan lain-lain.
* `<button>`: Digunakan untuk membuat tombol interaktif yang dapat memicu tindakan atau fungsi.
* `<a>`: Digunakan untuk membuat tautan atau *hyperlink* ke halaman lain atau sumber daya lain di web.
* `<img>`: Digunakan untuk menampilkan gambar di halaman web.
* `<ul>`, `<ol>`, dan `<li>`: Digunakan untuk membuat daftar tak terurut (unordered list), daftar terurut (ordered list), dan item dalam daftar.
* `<table>`, `<tr>`, `<th>`, dan `<td>`: Digunakan untuk membuat tabel dan baris dalam tabel bersama dengan sel dan judul.
<br><br>


3. Jelaskan perbedaan antara *margin* dan *padding*.

    **Jawab:**

* **Margin**<br>
Margin adalah ruang di luar elemen HTML, yang menentukan jarak antara elemen tersebut dengan elemen-elemen lain di sekitarnya.
Margin tidak memiliki latar belakang dan biasanya digunakan untuk mengendalikan jarak antara elemen dengan elemen-elemen lain di luar elemen tersebut. Margin bersifat transparan, artinya tidak dapat diisi dengan warna atau gambar latar belakang. Margin dapat memiliki nilai positif atau negatif, yang memungkinkan kita untuk menggeser elemen ke dalam atau keluar dari elemen-elemen di sekitarnya.

* **Padding**<br>
Padding adalah ruang di dalam elemen HTML, yang menentukan jarak antara konten elemen tersebut dengan tepi elemen tersebut (batas elemen dan kontennya). Padding mempengaruhi area di sekitar konten elemen, dan digunakan untuk memberikan ruang di sekitar teks atau elemen-elemen lain di dalam elemen tersebut. Padding dapat memiliki latar belakang, sehingga kita dapat mengisi padding dengan warna atau gambar latar belakang, namun Padding tidak dapat memiliki nilai negatif.
<br><br>


4. Jelaskan perbedaan antara *framework* CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?

    **Jawab**

* **Bootstrap** memiliki desain yang lebih "opiniated" atau lebih banyak panduan desain yang telah ditentukan sebelumnya. Hal ini berarti kita akan mendapatkan tampilan yang konsisten dan bagus secara *default*, tetapi lebih sulit untuk mengubah tampilan menjadi sesuatu yang benar-benar unik. Bootstrap menyediakan banyak komponen siap pakai dengan desain yang telah ditentukan sebelumnya, namun Bootstrap memiliki ukuran berkas CSS yang lebih besar karena menyertakan banyak fitur dan komponen yang lebih banyak.
* **Tailwind** memiliki pendekatan yang lebih "utility-first." Hal ini berarti Tailwind memberikan banyak kelas utilitas yang memungkinkan kita untuk merancang tampilan dengan lebih bebas, namun kita perlu lebih banyak bekerja untuk membuat tampilan yang sama dengan Bootstrap. Tailwind memberikan kontrol yang lebih besar atas tampilan elemen-elemen individu. Tailwind memiliki ukuran berkas yang lebih kecil karena hanya memberikan kelas-kelas utilitas yang diperlukan.
* **Kapan menggunakan Bootstrap**
    * Saat ingin membangun proyek dengan cepat.
    * Saat tidak ingin menghabiskan banyak waktu untuk menyesuaikan desain.
    * Saat membutuhkan komponen siap pakai seperti navbar, form, dan lain sebagainya.
* **Kapan menggunakan Tailwind**
    * Saat ingin kontrol desain yang sangat besar dan fleksibilitas dalam merancang tampilan.
    * Saat ingin menghindari overhead kelas CSS yang tidak digunakan dalam proyek.
    * Saat merasa nyaman dengan pendekatan "utility-first" dan ingin merancang dengan cepat.
<br><br>


5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

    **Jawab:**

* Menambah Bootstrap ke aplikasi dengan mengedit berkas `base.html` di folder template
```
<head>
    {% block meta %}
        ...
    {% endblock meta %}
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha384-KyZXEAg3QhqLMpG8r+J4jsl5c9zdLKaUk5Ae5f5b1bw6AUn5f5v8FZJoMxm6f5cH1" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js" integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.min.js" integrity="sha384-BBtl+eGJRgqQAUMxJ7pMwbEyER4l1g+O15P+16Ep7Q9Q+zqX6gSbd85u4mG4QzX+" crossorigin="anonymous"></script>
</head>
```
* Membuat navbar menggunakan Bootstrap dan menambahkan nama pengguna, link membuat item, dan tombol logout
* Menambah fitur edit pada aplikasi dengan membuat fungsi `edit_product` di berkas `views.py`
```
def edit_product(request, id):
    item = Item.objects.get(pk = id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)
```
* Membuat berkas `edit_product.html` kemudian menambah path yang sesuai ke `urls.py`
```
from main.views import edit_product
```
```
path('edit-product/<int:id>', edit_product, name='edit_product'),
```
* Mengedit tampilan pada berkas `main.html`, `login.html`, `register.html`, `create_item.html`, dan `edit_product.html` menggunakan CSS dan Bootstrap seperti mengubah warna tabel, warna teks, dan lain sebagainya.
* Bonus: menambah kode berikut di elemen `<tr>` pada tabel di berkas `main.html` serta menambahkan style CSS baru untuk mengubah warna tulisan pada baris terakhir
```
<tr {% if forloop.last %}class="last-row"{% endif %}>
```
```
.last-row {
        color: #0d5fee;
    }
```


