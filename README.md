Link App: [Weapentory](https://weapentory.adaptable.app/main/)<br>

Nama: Muhammad Rafi Zia Ulhaq<br>
NPM: 2206814551<br>
Kelas: PBP B
<hr>

1. Apa itu Django `UserCreationForm`, dan jelaskan apa kelebihan dan kekurangannya?

**Jawab:**

Django `UserCreationForm` adalah sebuah form yang digunakan untuk membuat akun pengguna (user account) dalam sebuah aplikasi web. Form ini mengandung berbagai data yang umumnya diperlukan untuk membuat akun pengguna, seperti nama pengguna (username), kata sandi (password), dan konfirmasi kata sandi.

* **Kelebihan**
    * **Mudah digunakan**: Form ini sudah dikonfigurasi secara default, sehingga pengguna dapat langsung menggunakannya tanpa perlu melakukan konfigurasi tambahan.
    * **Aman**: Django memiliki sistem keamanan yang kuat yang mencakup proteksi terhadap serangan seperti SQL injection.
    * **Fleksibel**: Form ini dapat dikonfigurasi ulang sesuai dengan kebutuhan pengguna.

* **Kekurangan**
    * **Tidak dapat disesuaikan secara penuh**: Form ini sudah dikonfigurasi secara default, sehingga pengguna tidak dapat menyesuaikannya secara penuh.
    * **Tampilan standar**: UserCreationForm memiliki tampilan standar yang mungkin perlu disesuaikan agar sesuai dengan desain tampilan yang diinginkan.
<br><br>


2. Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?

**Jawab:**

* **Autentikasi**
Autentikasi adalah proses verifikasi identitas pengguna. Tujuan autentikasi adalah untuk memastikan bahwa pengguna memiliki identitas yang valid dan sah sebelum memberikan akses ke bagian tertentu dari aplikasi. Contoh: pengguna memasukkan nama pengguna dan kata sandi untuk masuk ke aplikasi.

* **Otorisasi**
Otorisasi adalah proses yang menentukan hak akses apa yang dimiliki oleh pengguna yang telah terotentikasi. Otorisasi memastikan bahwa meskipun seorang pengguna telah terotentikasi, ia hanya memiliki akses ke bagian aplikasi yang sesuai dengan peran atau izinnya. Contoh: hanya administrator yang dapat mengedit atau menghapus data, sementara pengguna biasa hanya dapat melihatnya.
<br><br>


3. Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?

**Jawab:**

Cookies adalah mekanisme yang digunakan dalam aplikasi web untuk menyimpan data pada sisi klien (pada perangkat pengguna) untuk berbagai tujuan seperti pengelolaan informasi sesi pengguna, pelacakan pengguna, preferensi pengguna, dan iklan. Django menggunakan cookies untuk mengelola data sesi pengguna dengan cara berikut:
* Saat pengguna masuk ke aplikasi, Django membuat objek `Session` baru. Objek ini menyimpan informasi tentang pengguna, seperti nama pengguna, terakhir login, dan pengaturan lainnya.
* Django menyimpan objek `Session` dalam cookie yang dikirim ke browser pengguna.
* Ketika pengguna mengunjungi halaman lain di aplikasi, browser akan mengirimkan cookie tersebut ke server.
* Server menggunakan data sesi untuk menentukan apakah pengguna telah masuk dan untuk menyimpan informasi tentang pengguna.
<br><br>


4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?

**Jawab**

Penggunaan cookies secara default dalam pengembangan web tidak sepenuhnya aman. Terdapat beberapa risiko yang harus diwaspadai, antara lain:
* **Kebocoran data**: Cookies dapat diretas untuk dicuri datanya. Data yang dicuri dapat berupa informasi pribadi, seperti nama pengguna, alamat email, dan kata sandi.
* **Pelacakan**: Cookies dapat digunakan untuk melacak aktivitas pengguna di web. Data pelacakan ini dapat digunakan untuk menargetkan iklan atau untuk mengumpulkan informasi tentang perilaku pengguna.
* **Penggunaan cookie oleh pihak ketiga**: Cookies dapat digunakan oleh pihak ketiga, seperti penyedia layanan iklan. Pihak ketiga dapat menggunakan cookie untuk melacak aktivitas pengguna di berbagai situs web.
* **Pembajakan session**: Jika cookie sesi pengguna tidak dienkripsi atau diatur dengan baik, penyerang dapat mencuri cookie tersebut dan mengakses sesi pengguna yang sudah ada.
<br><br>


4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

**Jawab:**

a. Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.
* Buka berkas `views.py` dan impor fungsi-fungsi yang diperlukan 
```
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
```
* Membuat fungsi dengan nama `register`, `login_user`, `logout_user` yang masing-masing menerima parameter request
```
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```
* Menambahkan kode berikut di atas fungsi `show_main`
```
@login_required(login_url='/login')
```
* Membuat berkas `register.html`, `login.html` di folder `templates`
* Menambahkan button logout di berkas `main.html`
* Impor fungsi-fungsi yang telah dibuat ke berkas `urls.py` lalu menambahkan path url yang sesuai ke `urlpatterns`
```
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
```

b. Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.
* Register dua akun pengguna baru kemudian menambahkan masing-masing akun dengan tiga dummy data dengan `Add New Item`

c. Menghubungkan model `Item` dengan `User`.
* Menambahkan kode berikut untuk mengimpor model di berkas `models.py`
```
from django.contrib.auth.models import User
```
* Menambahkan kode berikut ke `class Item`
```
user = models.ForeignKey(User, on_delete=models.CASCADE)
```
* Mengganti fungsi `create_item` di berkas `views.py` menjadi
```
form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)
        item.user = request.user
        item.save()
        return HttpResponseRedirect(reverse('main:show_main'))
    ...
```
* Mengubah fungsi `show_main` menjadi
```
def show_main(request):
    items = Item.objects.filter(user=request.user)

    context = {
        'app_name' : 'Weapentory',
        'name': request.user.username,
        'class': 'PBP B',
        'items': items,
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)
```
* Melakukan migrasi model

d. Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan `cookies` seperti `last login` pada halaman utama aplikasi.
* Buka berkas `views.py` dan impor fungsi-fungsi berikut
```
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
```
* Pada fungsi `login_user` ubah isi kode `if user is not None` menjadi
```
if user is not None:
    login(request, user)
    response = HttpResponseRedirect(reverse("main:show_main")) 
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response
```
* Menambahkan kode berikut pada variabel `context`
```
'last_login': request.COOKIES['last_login'],
```
* Buka berkas `main.html` dan menambahkan kode berikut
```
<h5>Sesi terakhir login: {{ last_login }}</h5>
```

e. Bonus
* Membuat fungsi `delete_item`, `increment_amount`, dan `decrement_amount` yang menerima parameter `request` dan `item_id` di berkas `views.py`
```
def delete_item(request, item_id):
    item = Item.objects.get(pk=item_id)
    item.delete()
    return redirect('main:show_main')

def increment_amount(request, item_id):
    item = Item.objects.get(pk=item_id)
    item.amount += 1
    item.save()
    return redirect('main:show_main')

def decrement_amount(request, item_id):
    item = Item.objects.get(pk=item_id)
    if item.amount > 1:
        item.amount -= 1
        item.save()
    else:
        delete_item(request, item_id)
    return redirect('main:show_main')
```
* Mengimpor fungsi-fungsi tersebut ke `urls.py` dan menambahkan path yang sesuai
```
    path('delete/<item_id>/', delete_item, name='delete_item'),
    path('increment_amount/<item_id>/', increment_amount, name='increment_amount'),
    path('decrement_amount/<item_id>/', decrement_amount, name='decrement_amount'),
```
* Mengedit berkas `main.html` agar dapat menampilkan tombol yang sesuai



