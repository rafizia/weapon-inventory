Nama: Muhammad Rafi Zia Ulhaq<br>
NPM: 2206814551<br>
Kelas: PBP B
<hr>

1. Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.

    **Jawab:**

* **Synchronous Programming**<br>
Dalam *Synchronous Programming*, operasi yang memerlukan waktu akan memblokir eksekusi program. Hal ini berarti bahwa program akan menunggu sampai operasi tersebut selesai sebelum melanjutkan eksekusi kode selanjutnya. *Synchronous Programming* cocok untuk operasi-operasi yang sederhana, namun program ini cenderung kurang efisien dalam menangani operasi-operasi yang memakan waktu, seperti permintaan jaringan atau operasi file yang lambat.

* **Asynchronous Programming**<br>
Dalam *Asynchronous Programming*, operasi-operasi yang memerlukan waktu dapat dieksekusi tanpa menghentikan eksekusi program utama. Program dapat melanjutkan menjalankan kode lain sambil menunggu operasi asinkron selesai. *Asynchronous Programming* sangat berguna dalam aplikasi berbasis jaringan, aplikasi web, atau aplikasi yang memerlukan pengolahan data yang memakan waktu. *Asynchronous Programming* memungkinkan aplikasi untuk tetap responsif karena tidak menghentikan eksekusi untuk operasi yang memakan waktu.
<br><br>


2. Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma *event-driven programming*. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.

    **Jawab:**

Paradigma *event-driven programming* adalah pendekatan dalam pemrograman di mana program merespons peristiwa atau kejadian yang terjadi, seperti input pengguna, tindakan dari perangkat keras, atau peristiwa lain yang terjadi dalam sistem. Tidak seperti program biasa yang mengeksekusi kode secara berurutan dari atas ke bawah, program yang diimplementasikan dalam paradigma *event-driven* akan "mendengarkan" peristiwa yang terjadi dan meresponsnya dengan menjalankan kode tertentu yang telah ditentukan sebelumnya.
Dalam tugas ini penerapan dari *event-driven programming* misalnya adalah ketika kita mengklik tombol seperti tombol add item, hapus item, login, logout, dan sebagainya program akan merespons tindakan-tindakan tersebut dengan mengeksekusi suatu kode yang telah ditentukan sebelumnya.
<br><br>


3. Jelaskan penerapan *asynchronous programming* pada AJAX.

    **Jawab:**

*Asynchronous programming* pada AJAX memungkinkan pengembang web untuk mengirim permintaan HTTP ke server dan menerima respons tanpa harus memuat ulang seluruh halaman web. Penerapan *asynchronous programming* dalam AJAX sangat penting karena memungkinkan aplikasi web untuk tetap responsif dan tidak menghentikan eksekusi selama proses pengiriman atau penerimaan data. Sebagai hasilnya, pengguna dapat berinteraksi dengan halaman web tanpa harus menunggu untuk memuat ulang seluruh halaman setiap kali ada interaksi.
<br><br>


4. Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada library jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan.

    **Jawab**

**Fetch API**<br>
* **Promise-Based:** Fetch API mengembalikan objek Promise, yang memungkinkan pemrogram untuk mengatasi proses asinkron dengan lebih baik dan lebih mudah.
* **Lebih Ringan:** Fetch API lebih ringan karena tidak memuat banyak fitur tambahan seperti yang dimiliki jQuery.
* **Mendukung Format Data Modern:** Fetch API mendukung format data modern seperti JSON dengan baik, dan lebih mudah digunakan dengan berbagai jenis respons data.

**jQuery**<br>
* **Cross-Browser Compatibility:** jQuery menyediakan abstraksi tingkat tinggi yang mengatasi perbedaan dalam dukungan AJAX di berbagai browser sehingga membuatnya cocok untuk pengembangan lintas-platform.
* **Metode Pendekatan Lebih Mudah:** jQuery menggunakan pendekatan yang lebih dekat dengan API tradisional dan lebih mudah diimplementasikan oleh pengembang yang tidak terlalu akrab dengan JavaScript modern.
* **Banyak Fitur Tambahan:** jQuery memiliki banyak fitur tambahan yang melampaui AJAX, seperti animasi, manipulasi DOM, dan event handling.

Menurut saya pilihan antara Fetch API dan jQuery akan tergantung pada proyek yang dikembangkan. Jika ingin menggunakan pendekatan yang lebih modern dan lebih ringan, maka Fetch API mungkin menjadi pilihan yang baik. Namun, jika perlu mendukung browser lama atau ingin memanfaatkan fitur tambahan yang ditawarkan jQuery, maka jQuery masih menjadi pilihan yang valid.
<br><br>


5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

    **Jawab:**

* Membuat fungsi baru pada `views.py` dengan nama `get_item_json` yang menerima parameter request.
```
def get_item_json(request):
    product_item = Item.objects.all()
    return HttpResponse(serializers.serialize('json', product_item))
```
* Membuat fungsi baru pada `views.py` dengan nama `add_item_ajax` yang menerima parameter request serta menambah dekorator `@csrf_exempt` di atas fungsi tersebut.
```
def add_item_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        type = request.POST.get("type")
        atk = request.POST.get("atk")
        rarity = request.POST.get("rarity")
        description = request.POST.get("description")
        amount = request.POST.get("amount")
        user = request.user

        new_product = Item(name=name, type=type, atk=atk, rarity=rarity, description=description, amount=amount, user=user)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()
```
* Menambah *routing* untuk fungsi `get_item_json` dan `add_item_ajax`
```
    path('get-item/', get_item_json, name='get_item_json'),
    path('create-item-ajax/', add_item_ajax, name='add_item_ajax')
```
* Menghapus kode tabel pada berkas `main.html` dan menggantinya dengan `<table id="item_table"></table>`
* Membuat block `<Script>` di bagian bawah berkas kemudian membuat fungsi `getItems()` pada block `<Script>`
```
async function getItems() {
    return fetch("{% url 'main:get_item_json' %}").then((res) => res.json())
}
```
* Membuat fungsi `refreshItems()` pada block `<Script>`
```
async function refreshItems() {
    document.getElementById("item_table").innerHTML = ""
    const items = await getItems()
    let htmlString = `<tr>
        <th>Name</th>
        <th>Type</th>
        <th>ATK</th>
        <th>Rarity</th>
        <th>Description</th>
        <th>Amount</th>
    </tr>`
    items.forEach((item) => {
        htmlString += `\n<tr>
        <td>${item.fields.name}</td>
        <td style="text-align: center;">${item.fields.type}</td>
        <td style="text-align: center;">${item.fields.atk}</td>
        <td style="text-align: center;">${item.fields.rarity}</td>
        <td>${item.fields.description}</td>
        <td style="text-align: center;">${item.fields.amount}</td>
        <td><button class="btn btn-outline-danger btn-sm" data-item-id="${item.id}">Delete</button></td>
    </tr>` 
    
    })
    
    document.getElementById("item_table").innerHTML = htmlString
}

refreshItems()
```
* Membuat modal sebagai *form* untuk menambahkan produk
```
<div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog">
        <div class="modal-content" style="background-color: #262a33;">
            <div class="modal-header">
                <h1 class="modal-title fs-5" id="exampleModalLabel">Add New Item</h1>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <form id="form" onsubmit="return false;">
                    {% csrf_token %}
                    <div class="mb-3">
                        <label for="name" class="col-form-label">Name:</label>
                        <input type="text" class="form-control" id="name" name="name"></input>
                    </div>
                    <div class="mb-3">
                        <label for="type" class="col-form-label">Type:</label>
                        <input type="text" class="form-control" id="type" name="type"></input>
                    </div>
                    <div class="mb-3">
                        <label for="atk" class="col-form-label">ATK:</label>
                        <input type="number" class="form-control" id="atk" name="atk"></input>
                    </div>
                    <div class="mb-3">
                        <label for="rarity" class="col-form-label">Rarity:</label>
                        <input type="text" class="form-control" id="rarity" name="rarity"></input>
                    </div>
                    <div class="mb-3">
                        <label for="description" class="col-form-label">Description:</label>
                        <textarea class="form-control" id="description" name="description"></textarea>
                    </div>
                    <div class="mb-3">
                        <label for="amount" class="col-form-label">Amount:</label>
                        <input type="number" class="form-control" id="amount" name="amount"></input>
                    </div>
                </form>
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-outline-light" data-bs-dismiss="modal">Close</button>
                <button type="button" class="btn btn-outline-custom" id="button_add" data-bs-dismiss="modal">Add Item</button>
            </div>
        </div>
    </div>
</div>
```
* Menambah `button` untuk menampilkan modal
```
<button type="button" class="btn btn-outline-custom" data-bs-toggle="modal" data-bs-target="#exampleModal">Add New Item</button>
```
* Membuat fungsi `addItem()` dan fungsi `onclick` untuk menambah item
```
function addItem() {
    fetch("{% url 'main:add_item_ajax' %}", {
        method: "POST",
        body: new FormData(document.querySelector('#form'))
    }).then(refreshItems)

    document.getElementById("form").reset()
    return false
}
document.getElementById("button_add").onclick = addItem
```
* Melakukan perintah `python manage.py collectstatic` untuk mengumpulkan file static dari aplikasi


