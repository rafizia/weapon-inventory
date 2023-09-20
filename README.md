Link App: [Weapentory](https://weapentory.adaptable.app/main/)<br>

Nama: Muhammad Rafi Zia Ulhaq<br>
NPM: 2206814551<br>
Kelas: PBP B
<hr>

1. Apa perbedaan antara form `POST` dan form `GET` dalam Django?

**Jawab:**

* **Post** <br>
*Method* `POST` biasanya digunakan untuk memproses data yang akan dimasukkan ke dalam database. Data dalam form `POST` dikirimkan dalam *request body* HTTP. Hal ini berarti data tidak akan terlihat dalam URL, sehingga lebih aman untuk mengirim data sensitif seperti kata sandi. Kelebihan dari method `POST` adalah data yang dikirim dapat berupa sebuah data yang besar dan kompleks, seperti pengiriman file.

* **Get** <br>
*Method* `GET` biasanya digunakan untuk mengambil data dari server tanpa memodifikasinya. Berbeda dengan `POST`, data yang dikirim melalui method `GET` disisipkan ke dalam URL sebagai parameter `query string`. Hal ini membuat data dapat terlihat dalam URL, sehingga kurang aman untuk mengirim data sensitif. Selain itu, URL juga memiliki batasan panjang tertentu yang dapat membatasi jumlah data yang dapat dikirim.
<br><br>

2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?

**Jawab:**

* **XML** <br>
XML adalah format data markup yang menggunakan tag untuk mewakili data. Tag tersebut dapat digunakan untuk mendefinisikan struktur data dan data itu sendiri. XML adalah format yang sangat fleksibel dan dapat digunakan untuk mewakili berbagai jenis data. XML umumnya digunakan untuk pertukaran data kompleks dan memiliki struktur yang lebih rumit, terutama dalam konteks layanan web, konfigurasi, dan penyimpanan data semi-struktural.
```
<product>
    <id>1234</id>
    <name>T-Shirt</name>
    <price>20.00</price>
</product>
```

* **JSON** <br>
JSON adalah format data teks yang menggunakan pasangan *key-value* untuk mewakili data sehingga lebih mudah dibaca oleh manusia. JSON adalah format yang didukung oleh banyak bahasa pemrograman. JSON mendukung tipe data dasar seperti string, integer, object, boolean, dan null. JSON digunakan untuk pertukaran data yang lebih sederhana, terutama dalam pengembangan aplikasi web.
```
{
    "id": 1234,
    "name": "T-Shirt",
    "price": 20.00
}
```

* **HTML** <br>
HTML adalah format data markup yang digunakan untuk membuat halaman web dan mengatur cara konten ditampilkan kepada pengguna melalui browser web. HTML adalah format yang sangat umum digunakan untuk mengirimkan data dari server ke browser. HTML menggunakan tag untuk mewakili elemen-elemen halaman web, seperti teks, gambar, dan video. HTML tidak digunakan untuk pertukaran data seperti XML dan JSON. Sebaliknya, HTML fokus pada presentasi dan tampilan halaman web.
```
<product id="1234">
    <name>T-Shirt</name>
    <price>20.00</price>
</product>
```
<br>


3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?

**Jawab:**

Beberapa alasan mengapa JSON sering digunakan:
* **Mudah dibaca dan ditulis**: JSON menggunakan sintaks yang sederhana dan mudah dibaca oleh manusia. Strukturnya menggunakan *key-value* yang mirip dengan format data dalam bahasa pemrograman seperti JavaScript. Hal ini membuat JSON lebih mudah untuk dipahami dan digunakan oleh pengembang.
* **Dukungan bahasa pemrograman yang luas**: JSON didukung oleh banyak bahasa pemrograman, termasuk JavaScript, Python, Java, dan C++. Hal ini membuat JSON lebih mudah untuk digunakan dalam berbagai aplikasi.
* **Efisien dalam Penggunaan Bandwidth**: JSON cenderung lebih efisien dalam penggunaan bandwidth dibandingkan dengan format lain seperti XML. Karena strukturnya ringkas dan tidak memiliki markup yang berlebihan.
* **Fleksibilitas**: JSON dapat digunakan untuk mewakili berbagai jenis data, termasuk data sederhana dan data kompleks. Hal ini membuat JSON lebih cocok untuk berbagai aplikasi.
* **Dukungan Browser Bawaan**: Sebagian besar browser web modern memiliki dukungan bawaan untuk *parsing* dan menghasilkan objek JavaScript dari JSON, membuatnya sangat berguna dalam pengembangan aplikasi web.
<br><br>


4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

**Jawab:**

a. Membuat input `form` untuk menambahkan objek model pada app sebelumnya.
* Membuat berkas `forms.py` di direktori `main` yang berisi
```
from django.forms import ModelForm
from main.models import Item

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "type", "atk", "rarity", "description", "amount"]
```
* Menambah beberapa import pada berkas `views.py` pada direktori main
```
from django.http import HttpResponseRedirect
from main.forms import ItemForm
from django.urls import reverse
```
* Mengubah fungsi `show_main` pada `views.py` menjadi
```
def show_main(request):
    items = Item.objects.all()

    context = {
        'app_name' : 'Weapentory',
        'name': 'Muhammad Rafi Zia Ulhaq',
        'class': 'PBP B',
        'items': items
    }

    return render(request, "main.html", context)
```
* Menambah import fungsi `create_item` pada `urls.py`
```
from main.views import show_main, create_item
```
* Menambah path `create_item` pada `urlpatterns` pada `urls.py`
```
path('create-item', create_item, name='create_item'),
```
* Membuat berkas create_item.html dengan isi
```
{% extends 'base.html' %} 

{% block content %}
<h1>Add New Item</h1>

<form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td>
                <input type="submit" value="Add Item"/>
            </td>
        </tr>
    </table>
</form>

{% endblock %}
```
* Mengganti isi berkas `main.html` agar dapat menampilkan daftar item yang telah ditambahkan sebelumnya.

b. Tambahkan 5 fungsi `views` untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.
* Membuat fungsi `create_item` pada berkas `views.py`.
```
def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_item.html", context)
```
* Membuat fungsi `show_xml` pada berkas `views.py`.
```
def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```
* Membuat fungsi `show_json` pada berkas `views.py`.
```
def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
* Membuat fungsi `show_xml_by_id` pada berkas `views.py`.
```
def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```
* Membuat fungsi `show_json_by_id` pada berkas `views.py`.
```
def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

c. Membuat routing URL untuk masing-masing `views` yang telah ditambahkan pada poin 2
* Mengimpor fungsi-fungsi yang telah dibuat sebelumnya ke berkas `urls.py`
```
from main.views import show_main, create_item, show_xml, show_json, show_xml_by_id, show_json_by_id 
```
* Menambah masing-masing path url ke berkas `urls.py`
```
    path('create-item', create_item, name='create_item'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
```
<br>


5. Mengakses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam `README.md`.

**Jawab:**

* **HTML**
![HTML](https://github.com/rafizia/weapon-inventory/blob/master/image/Postman_HTML.png?raw=true)
* **XML**
![XML](https://github.com/rafizia/weapon-inventory/blob/master/image/Postman_XML.png?raw=true)
* **JSON**
![JSON](https://github.com/rafizia/weapon-inventory/blob/master/image/Postman_JSON.png?raw=true)
* **XML by id**
![XML by id](https://github.com/rafizia/weapon-inventory/blob/master/image/Postman_XML_by_id.png?raw=true)
* **JSON by id**
![JSON by id](https://github.com/rafizia/weapon-inventory/blob/master/image/Postman_JSON_by_id.png?raw=true)