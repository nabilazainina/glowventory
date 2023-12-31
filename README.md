# Welcome to Glowventory :revolving_hearts:

### Application Link
[Click Here!](https://glowventory.adaptable.app/main/) or (http://localhost:8000/login/) to access Glowventory by Bella :smiley:


#
# TUGAS 2

## Jelaskan bagimana cara kamu mengimplementasikan checklist secara step-by-step

### :white_check_mark: Membuat Project Django baru

Pada aplikasi Glowventory ini, saya memulai dengan membuat repositori baru bernama "glowventory" di github saya. Saya pastikan untuk mengatur visibilitas repositori saya sebagai public agar bisa dilihat dan diakses pihak luar. 

Setelah membuat repositori di github, hal berikutnya yang saya lakukan adalah mengclone repositori "glowventory" di github saya ke direktori lokal yang saya inginkan dengan cara melakukan perintah ```git clone <URL Glowventory>```. Dengan ini, repositori glowventory di github akan terduplikasi ke repositori di komputer lokal saya, tapa harus melakukan inisasi git di repositori lokal saya.

Selanjutnya, saya membuat sebuah projek Django baru menggunakan direktori glowventory yang sudah ada di komputer lokal saya. Saya mulai dengan mengaktifkan virtual environment di repositori tempat saya ingin menaruh repositori glowventory saya, untuk mengisolasi package dan dependencies aplikasi agar tidak bertabrakan dengan versi lain di komputer saya menggunakan perintah ```python -m venv env```. Kemudian, saya mengaktifkan virtual environment dengan perintah ```env\Scripts\activate.bat```. Apabila command prompt saya sudah memiliki kata ```(env)```, artinya saya telah berhasil mengaktifkan virtual environment.

Selanjutnya, saya menyiapkan dependencies atau komponen-komponen yang diperlukan perangkat lunak untuk berfungsi, termasuk library, framework, atau package yang akan membantu developer (seperti saya) untuk memanfaatkan kode yang telah ada dengan membuat berkas berjudul ```requirements.txt``` dan menambahkan beberapa dependencies, yakni

```
django
gunicorn
whitenoise
psycopg2-binary
requests
urllib3
```

Kemudian, saya menginstall dependencies tersebut di lingkungan virtual environment yang sudah saya aktifkan (aktif apabila ada tulisan ```(env)```) dengan menjalankan perintah ```pip install -r requirements.txt```. Terakhir, saya mengaktifkan proyek django dengan menjalankan perintah ```django-admin startproject glowventory .```. 

Untuk bisa menjalankan server, saya mulai dengan menambahkan ```*``` pada ```ALLOWED HOST``` di ```settings.py``` untuk mengizinkan akses ke semua host agar aplikasi glowventory dapat digunakan secara luas. Setelah memastikan direktori dan file di dalam glowventory sudah sesuai, saya menjalankan server Django dengan perintah ```python manage.py runserver```. Setelah membuka http://localhost:8000, terdapat roket yang artinya Project Django glowventory saya sudah terbuat ^_^

### :white_check_mark: Membuat aplikasi dengan nama ```main``` pada proyek tersebut

Saya mulai dengan perintah ```python manage.py startapp main``` di terminal untuk membuat aplikasi dengan nama _main_ baru. Setelah itu, akan muncul direktori baru dengan nama ```main``` di dalam repositori glowventory. Kemudian, saya mendaftarkan aplikasi ```main``` ke proyek dengan menambahkan line of code ```main``` ke dalam ```settings.py``` di proyek glowventory. Dengan step tersebut, aplikasi dengan nama ```main``` sudah terbentuk di repositori glowventory saya ^_^

### :white_check_mark: Melakukan _routing_ pada proyek agar dapat menjalankan aplikasi ```main```

Untuk menghubungkan rute URL dengan tampilan ```main```, saya mulai dengan membuka ```urls.py``` di direktori glowventory **(bukan direktori main)**. Kemudian, saya tambahkan line of code

```py
from django.urls import path, include

urlpatterns = [
    ...
    path('main/', include('main.urls')),
    ...
]
```

Bagian kode ini akan mengatur rute URL tingkat proyek di proyek glowventory saya. Fungsi ```include``` akan mengimpor rute URL dari aplikasi ```main``` ke dalam berkas ```urls.py``` proyek glowventory. Sementara itu, path ```'main/'``` ini akan digunakan untuk mengarahkan rute yang didefinisikan. Oleh karena itu, untuk mengakses tampilan main melalui link adaptable, kita harus menambahkan ```\main``` di akhir.

### :white_check_mark: Membuat model pada aplikasi ```main``` dengan nama ```Item``` dan memiliki atribut wajib ```name```, ```amount```, dan ```description```

Untuk menyempurnakan model dalam aplikasi main glowventory, saya mulai dengan membuka berkas ```models.py``` pada direktori ```main```. Kemudian, saya isi berkas ```models.py``` tersebut dengan atribut-atribut sesuai dengan ketentuan yang diharapkan, yaitu

```py
from django.db import models

class Items(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField()
    category = models.TextField()
```

Dengan ini, saya telah menambahkan beberapa atribut baru ke dalam model aplikasi main saya, yaitu ```name``` merepresentasikan nama item (dalam glowventory, nama skincare ^_^) dengan tipe ```CharField```, ```amount``` sebagai jumlah _item_ (dalam glowventory, nama skincare ^_^) dengan tipe ```IntegerField```, ```description``` sebagai deskripsi item (dalam glowventory, nama skincare ^_^) dengan tipe ```TextField```. Lalu, saya juga menambahkan _additional_ atribut, yakni ```category``` yang akan menampilkan kategori dari _skintype_ user seperti _dry_, _oily_, atau _combination to normal skin_ dengan tipe ```TextField``` dan ```price``` yang akan menampilkan harga dari skincare user dengan tipe ```IntegerField```

Setelah itu, saya memigrasi model agar Django dapat melacak perubahan model basis data glowventory, dengan menjalankan perintah

```
python manage.py makemigrations
python manage.py migrate
```

Perintah ```makemigration``` akan membuat suatu berkas migrasi yang berisi perubahan model yang belum diaplikasikan ke basis data. Sementara perintah ```migrate``` akan mengaplikasikan perubahan model ke berkas migrasi basis data.

### :white_check_mark: Membuat sebuah fungsi pada ```views.py``` untuk dikembalikan ke sebuah template HTML yang menampilkan nama aplikasi, nama, dan kelas

Saya memulai checklist ini dengan membuat sebuah direktori baru bernama ```templates``` di dalam direktori aplikasi ```main```. Saya lanjutkan dengan membuat berkas baru bernama ```main.html``` yang akan saya isi dengan nama aplikasi, nama, dan kelas saya.

Setelah menyelesaikan hal tersebut, saya akan menghubungkan view dengan template dengan membuat sebuah fungsi di ```views.py```. Fungsi yang saya tambahkan adalah fungsi ```show_main```. Saya akan mengimport ```render``` dari ```django.shortcuts``` untuk merender tampilan HTML. Kemudian, saya akan mengisi fungsi ```show_main``` dengan atribut application_name, name, dan class dengan kode seperti berikut

```py
from django.shortcuts import render

def show_main(request):
    context = {
        'application_name': 'glowventory',
        'name': 'Bella',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)
```

Pada kode di atas, ```context``` adalah dictionary yang valuenya berisi data yang akan dikirim ke tampilan, yakni application_name, name, dan class. Di line paling akhir, fungsi akan merender tampilan dari ```main.html```.

### :white_check_mark: Membuat sebuah __routing_ pada ```urls.py``` aplikasi ```main``` untuk memetakan fungsi yang telah dibuat

Pada bagian ini, saya akan mengkonfigurasikan rute url agar aplikasi ```main``` dapat diakses melalui peramban web.

Step pertama, adalah dengan membuat file bernama ```urls.py``` di dalam direktori ```main``` yang sudah saya buat. Saya akan mengimport ```path``` dari ```django.urls``` untuk bisa mendefinisikan pola URL. Kemudian, saya juga mengimport ```show_main``` dari ```main.views``` yang akan digunakan untuk menghandle request HTTP pada URL tertentu. Lalu, saya akan mendefinisikan ```main```  sebagai isi dari atribut app_name untuk mengidentifikasi aplikasi dalam proyek. Fungsi ```urls.py``` yang saya buat akan bertanggung jawab untuk mengatur rute URL yang terkait dengan aplikasi ```main```

```py
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```

### Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-teman

Pada bagian checklist ini, saya mulai dengan memasukkan akun github yang saya pakai untuk glowventory ke Adaptable.io. Kemudian, saya lanjutkan dengan memencet _New App_ pada Adaptable dan memilih repository ```glowventory``` dan memilih _branh main_ sebagai _deployment branch_ saya. Kemudian, saya pilih ```Python App Template``` sebagai _template deployment_ dan ```Postfre SQL``` sebagai tipe basis data. Saya masukkan python 3.10 sesuai dengan versi python di komputer saya, dan memasukkan perintah ```python manage.py migrate && gunicorn shopping_list.wsgi``` untuk Start Command. Saya masukkan nama aplikasi **glowventory** untuk domain situs web saya dan dilanjutkan dengan menndeploy aplikasi. Apabila semua proses terjalankan, Adaptable akan menunjukkan ceklis hijau besar yang artinya aplikasi **glowventory** berhasil dideploy ^_^.


## Buatlah bagan yang berisi _request client_ ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara ```urls.py```, ```views.py``, ````models.py```, dan berkas ```html```


**Bagan**

```

                                                    
+---------------------+        +-------------------+
|   Client Request    |        |    Django Web     |
| (HTTP Request)      |   -->  |     Server        |
+---------------------+        +-------------------+
                           |
                           |
                           v
                 +--------------------+
                 |    Django View     |
                 |    (views.py)      |
                 +--------------------+
                           |
                           |
                           v
                 +--------------------+
                 |    Model Data      |
                 |    (models.py)     |
                 +--------------------+
                           |
                           |
                           v
                 +--------------------+
                 |    HTML Template   |
                 |    (HTML File)     |
                 +--------------------+
                           |
                           |
                           v
                +--------------------+
                |  Server Response   |
                |  (HTTP Response)   |
                +--------------------+
                           |
                           |
                           v
                +--------------------+
                |  Client Browser    |
                +--------------------+
                                      

```

Penjelasan Proses:

1. Klien akan membuat permintaan HTTP ke Django Web Server yang kemudian akan merouting permintaan tersebut ke view yang sesuai berdasarkan konfigurasi pola URL di ```urls.py```
2. Apabila Django telah menemukan pola yang cocok, ```views.py``` akan memproses permintaan, termasuk berinteraksi dengan model-data jika diperlukan.
3. ```models.py``` atau Model-data akan mengatur interaksi dengan data  dan akan digunakan oleh ```views.py``` untuk mengambil, mengubah, atau menyimpan data dalam basis data. Views itu sendiri dapat berupa fungsi atau kelas, bergantung pada bagaimana kita (developer) mengatur views dari web kita.
4. Kemudian, view akan merender ```berkas HTML``` (template) yang sesuai dengan data yang diterima.
5. Selanjutnya, server akan mengirimkan respon HTTP yang berisi ```HTML``` yang telah dirender dengan menggabungkan data dari ```models.py```
6. Terakhir, client akan menerima respon dan menampilkan konten HTML dalam browser mereka


Oleh karena itu, beberapa kaitan dan fungsi ringkas dari ```urls.py```, ```views.py```, ```models.py```, dan ```Berkas HTML``` adalah :
1. **urls.py** = urls.py adalah tempat yang digunakan untuk mengatur URL-routing dalam aplikasi Django agar bisa mengarahkan permintaan client ke view yang sesuai
2. **views.py** = views.py adalah tempat yang berisi definisi dari view yang mengatur logika aplikasi. Bagian ini adalah tempat di mana permintaan client diproses dan respon dibuat. View akan mengambil data dari model jika diperlukan dan mengembalikan berkas HTML yang akan ditampilkan ke pengguna
3. **models.py** = models.py akan berisi definisi model-data untuk aplikasi. Model-data akan merepresentasikan objek dalam aplikasi dan akan digunakan oleh view untuk mengambil, mengubah, atau menyimpan data.
4. **Berkas HTML** = Berkas HTML digunakan untuk menampilkan konten yang akan diberikan kepada klien dan berisi struktur dan tampilan halaman web yang akan ditampilkan kepada pengguna

## Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

*Virtual Environment* (venv) adalah framework penting apabila kita melakukan pemebangan aplikasi web dengan bahasa pemrograman Python. Virtual Environment digunakan untuk mengisolasi dependensi dan paket yang digunakan dalam suatu proyek tertentu. Ini berarti, setiap proyek dapat memiliki versi paket Python yang berbeda tanpa saling berpengaruh, sehingga dapat mencegah adanya konflik antar-versi paket. Virtual Environment juga memastikan bahwa perubahan yang dibuat dalam suatu proyek tidak akan memengaruhi iinstalagi Python global dalam sistem sehingga dapat mencegah kerusakan atau konflik yang dapat terjadi apabila kita mengubah paket Python secara global.

Secara teknis, kita tetap bisa membuat aplikasi web berbasis Django tanpa Virtual Environment dengan melakukan instalasi _libraries_ secara global. Akan tetapi, tanpa Virtual Environment, kita harus sangat berhati-hati dengan manahemen paket Python dan versi yang digunakan dalam pengembangan proyek tersebut. Proyek yang dibuat tanpa menggunakan Virtual Environment lebih sulit untuk dikelola dibanding dengan menggunakan Virtual Environment. Oleh karena itu, penggunaan Virtual Environment dalam proses pengembangan aplikasi web merupakan praktik terbaik dalam pengembangan web dengan Django, untuk menjaga kebersihan isolasi, dan portabilitas proyek.

## Jelaskan apakah itu MVC, MVT, dan MVVM dan perbedaan dari ketiganya

1. MVC (Model, View, Controller)

    Model View Controller adalah sebuah pola design software yang digunakan untuk mengimplementasi user-interface dan menekankan pemisahan representasi data dari komponen-komponen yang berinteraksi dan memproses data (GeeksforGeeks). MVC memiliki 3 komponen :
    * Model: merupakan central komponen dari arsitektur MVC yang mengatur data dan logika aplikasi.  Model adalah komponen yang bertanggung jawab untuk memproses operasi yang berhubungan dengan data
    * View: View adalah tampilan data yang disajikan kepada pengguna dengan menampilkan informasi yang diambil dari model dan mengirimkannya ke pengguna
    * Controlle: Bertindak sebagai perantara antara model dan view yang akan mengatur aliran data antara keduanya.

2. MVT (Model, View, Template)

    Model View Template adalah sebuah pola design yang sebenarnya mirip dengan MVC dari segi kegunaan, yakni untuk mengimplementasikan interface dalam aplikasi web. Akan tetapi, MVT menggunakan kerangka kerja (framework) itu sendiri sebagai pengendali/controller (GeeksforGeeks). MVT juga memiliki 3 komponen, yakni
    * Model: Model dalam MVT juga memiliki kegunaan yang sama seperti MVC yaitu sebagai interface yang akan mengelola data dan logika aplikasi.
    * View: view dalam MTV di Django (framework python untuk web), View mengatur logika tampilan dan berperan sebagai pengontrol yang emenrima permintaan HTTP dari klien
    * Template: Template dalam MVT adalah bagian yang paling mirip dengan view dalam MVC. Template sendiri merupakan berkas HTML yang mengatur tampilan dan cara data disajikan ke pengguna tanpa melibatkan logika.

3. MVVM (Model-View-ViewModel) 

    MVVM itu sendiri mengusulkan pemisahan logikan presentasi data (User Interface) dari bagian inti logika aplikasi. MVVM ini sendiri umumnya digunakan dalam pengembangan aplikasi berbasis klien (seperti web berbasis JavaScript). Berikut komponen-komponennya:
    * Model: Lapisan ini akan bertanggung jawab atas abstraksi sumber data.
    * View: View dalam MVVM bertanggung jawab untuk menampilkan data kepada pengguna. Lapisan ini mengamati ViewModel dan tidak mengandung jenis logika aplikasi
    * ViewModel: ViewModel adalah komponen baru salam MVVM yang bertindak sebagai perantara antara Model dan View. ViewModel berisi logika presentasi yang memformat data dari Model agar dapat ditampilkan dengan baik di View sehingga berfungsi sebagai pengubung antara Model dan View

Perbedaan signifikan antara ketiga pola di atas adalah *peran dan fokus masing-masing terhadap pemisahan tanggung jawab dan kendali aplikasi*. MVC adalah pola yang umum digunakan dalam pengembangan aplikasi web sementara MVT adalah varian MVC yang digunakan dengan framework Django. Sementara itu, MVVM biasanya digunakan dalam pengembangan aplikasi berbasis klien yang memungkinkan tampilan yang lebih responsif. Pilihan antara ketiganya tergantung pada jenis aplikasi yang dikembangkan.

#

# TUGAS 3

## Perbedaan antara form ```POST``` dan form ```GET``` dalam Django

```GET``` dan ```POST``` adalah dua metode HTTP yang dugunakan saat berurusan dengan formulir.

* ```POST``` : Formulir login pada Django menggunakan metode ```POST``` yang akan mengumpulkan data formulir, mengenkripsi untuk pengiriman dan mengirimnya ke derver sebelum menerima respons. Untuk permintaan yang mengubah keadaan sistem -misalnya, permintaan yang membuat perubahan dalam database- harus menggunakan ```POST```. Selain itu, metode ```POST``` juga menawarkan lebih banyak kontrol atas akses -misalnya, formulir yang membutuhkan kata sandi-.

* ```GET``` : Metoe ```GET``` akan mengumpulkan data yang diserahkan ke dalam sebuah string, dan menggunakannya untuk membentuk URL. URL akan berisi alamat tempat data akan dikirimkan beserta kunci dan nilai data. Metode ```GET``` hanya bisa digunakan untuk permintaan yang tidak memengaruhi keadaan sistem dan juga tidak cocok untuk formulir kata sandi, dikarenakanan kata sandi akan muncul di URL sedemikian rupa dan akan tercata pada peramban dan log server dalam teks biasa sehingga menimbulkan risiko keamanan. Di sisi lain, GET cocok untuk hal-hal seperti formulir pencarian web, karena URL yang mewakili permintaan GET dapat dengan mudah ditandai, dibagikan, atau diajukan kembali.

## Perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data

- ```XML``` **eXtensible Markup Language** : XML adalah sebuah bahasa dan format file untuk menyimpan, mengirim, dan membangun kembali berbagai jenis data. XML didesain menjadi _self-descriptive_ dan harus mengandung **sebuah root _element_** uang merupakan _parent_ dari elemen lainnya, sehingga dengan membaca XML tersebut kita bisa mengerti informasi apa yang ingin disampaikan dari data yang tertulis. XML hanya berisi informasi yang dibungkus dalam _tag_ sehingga kita harus menulis program untuk mengirim, menerima, menyimpan, atau menampilkan informasi tersebut.

- ```JSON``` **JavaScript Object Notation** : JSON merupakan format file dan format pertukaran data standar yang menggunakan teks yang mudah dibaca manusia untuk menyimpan dan mengirimkan objek data yang terdiri dari pasangan atribut-nilai. JSON sendiri didesain menjadi _self-describing_, sehingga JSON sangat mudah untuk dimengerti. JSON dapat digunakan di bebragai aplikasi web maupun mobile, yaitu untuk menyimpan dan mengirimkan data.

- ```HTML``` **HyperText Markup Language** : HTML adalah bahasa markup yang digunakan oleh peramban web untuk mengartikan dan menyusun teks, gambar, dan materi lainnya menjadi halaman web yang dapat dilihat atau didengar.Dokumen HTML memiliki struktur yang terdiri dari elemen-elemen HTML bertingkat. Elemen-elemen ini ditandai dalam dokumen dengan menggunakan tag HTML. 

> [!NOTE]
> Berdasarkan pemaparan ketiganya, perbedaan mendasar antara ketiga format tersebut adalah ```XML``` dan ```JSON``` digunakan untuk menyimpan dan mengirim data, sementara ```HTML``` digunakan untuk menjelaskan bagaimana data tersebut ditampilkan.


## Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?

Seperti yang dipaparkan pada pertanyaan di atas, salah satu keunggulan JSON adalah kesederhanaan dan kemudahan membacanya. JSON mudah untuk ditulis dan dipahami, karena menggunakan format yang bisa dimengerti manusia dengan _keys_ dan _values_ nya. JSON tidak memerlukan tag, atribut, atau skema khusus seperti XML sehingga lebih mudah untuk dilihat dan dibaca.

## Jelaskan bagaimana cara kamu mengimplementasikan _checklist_ di atas secara _step=by-step_

### :white_check_mark: Membuat input ```form``` untuk menambahkan objek model pada app sebelumnya

Untuk menambahkan input ```form```, saya mulai dengan membuat **skeleton** yang berfungsi sebagai kerangka views dari glowventory. Kerangka views ini akan memastikan adanya konsistensi di desain situs web dan memperkecil kemungkinan terjadinya redundansi kode. 

Saya mulai dengan membuat folder ```templates``` pada root folder dan membuat sebuah file HTML baru bernama ```base.html``` yang akan menjadi _template_ dasar. Setelah itu, saya lanjutkan dengan mengisi baris ```TEMPLATES``` pada ```settings.py``` pada subdirektori ```shopping_list``` untuk memastikan file ```base.html``` terdeteksi sebagai berkas _template_ dengan line of code

```py
'DIRS': [BASE_DIR / 'templates']
```

Lalu saya lanjutkan dengan mengganti kode di ```main.html```  pada subdirektori ```templates``` dalam direktori ```main``` untuk membuat ```base.html``` sebagai _template_ utama dengan kode.

```py
{% extends 'base.html' %}
```

Step berikutnya adalah saya mulai mengeksekusi form input data. Fungsi form ini adalah untuk menginput data barang pada aplikasi. Saya mulai dengan membuat file baru ```forms.py``` pada direktori ```main``` yang akan membuat struktur _form_ agar bisa menerima data produk baru sesuai dengan models, yakni menambahkan kode

```py
from django.forms import ModelForm
from main.models import Item

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "amount", "price", "description", "category"]
```

* ```model = Item``` adalah line of code yang akan menunjukan model untuk form. Data form akan disimpan dan isisnya akan disimpan menjadi _object_ ```item```
* ```fields = ["name", "amount", "price", "description", "category"]``` adalah _fields_ dari Item yang digunakan untuk form sesuai dengan models glowventory


### :white_check_mark: Tambahkan 5 fungsi ```views``` untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID dan JSON by ID

* ```HTML``` :
    Setelah membuat form di checklist sebelumnya, saya lanjutkan dengan membuat function ```create_item``` pada ```views.py``` dengan mengimport ```ItemForm``` dari ```main.forms``` dan ```reverse``` dari ```django.urls``` pada file ```views.py```. 

    ```py
    def create_item(request):
        form = ItemForm(request.POST or None)

        if form.is_valid() and request.method == "POST":
            form.save()
            return HttpResponseRedirect(reverse('main:show_main'))

        context = {'form': form}
        return render(request, "create_item.html", context)
    ```

    Lalu, saya menambahkan line of code ```item = Item.objects.all()``` pada fungsi ```show_main``` untuk mengambil seluruh object Items yang tersimban di database. Serta menambahkan variabel ```items : item,``` pada dictionary ```context```. 
    

* ```XML``` :
    Untuk mengembalikan data dalam bentuk XML, saya mulai dengan menambah _import_ ```HttpResponse``` dan ```serializerz``` pada ```views.py```.

    Selanjutnya, masih di file yang sama, saya implementasikan fungsi pertama yang akan mengembalikan data dalam bentuk XML dengan menambah function ```show_xml```. Fungsi ```show_xml``` akan menyimpan keseluruhan hasil _query_ dari ```Item``` mereturn berupa ```HttpResponse``` yang berisi parameter data hasil _query_ yang diserialisasi menjadi XML dan parameter ```content_type="application/xml"``` .

    ```py
    def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
    ```

* ```JSON``` :

    Untuk mengembalikan data dalam bentu JSON, saya mulai dengan menambah menambah function ```show_json```. Fungsi ```show_json``` akan menerima parameter ```request``` dan menyimpan hasil _query_ dari seluruh data yang ada pada ```Item``` dan akan mereturn ```HttpResponse``` (yang sudah diimport) yang berisi hasil _query_ yang serialisasi menjadi JSON dan parameter ```content_type="application/json"```.

    ```py
    def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    ```

* ```XML by ID``` dan ```JSON by ID``` :

    Kedua metode ini akan mengembalikan data sesuai dengan index ID dari input item. Saya mulai dengan menambahkan dua fungsi baru yaitu ```def show_xml_by_id``` dan ```def show_json_by_id``` dengan parameter yang sama yaitu ```(request, id)```. 
    
    ```py
    def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

    def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    ```
    Fungsi ini akan menerima request sesuai dengan ID atau index product dan mengembalikannya ke views JSON atau XML.

### :white_check_mark: Membuat routing URL untuk masing-masing ```views``` yang telah ditambahkan pada poin 2.

* ```HTML``` :

    Setelah membuat fungsi ```create_item```,  saya lanjutkan dengan membuat sebuah berkas HTML baru dengan nama ```create_item.html``` di folder ```templates``` yang akan menampilkan _fields_ form sebagai table.

    Setelah membuat berkas ```create_item.html``` saya lanjutkan dengan mengimport ```create_item``` pada ```urls.py``` di subdirektori ```main``` dan menambahkan path urls ```create-item``` ke fungsi ```urlspatterns``` dengan line of code ```path('create-item/', create_item, name='create_item'),``` untuk merouting keseluruhan views dari fungsi ```create_item``` melalui HTML.

* ```XML``` :

    Setelah menyelesaikan fungsi ```show_xml```, saya lanjutkan dengan mengimport fungsi ```show_xml``` ke ```urls.py``` dan menambahkan path ```path('xml/', show_xml, name='show_xml'), ``` untuk bisa mengakses proyek Django melalui http://localhost:8000/xml.

* ```JSON``` :

    Setelah menyelesaikan fungsi ```show_json```, saya mengimport  fungsi ```show_json``` ke ```urls.py``` dan menambahkan path ```path('json/', show_json, name='show_json'), ``` untuk bisa mengakses proyek Django melalui http://localhost:8000/json.

* ```XML by ID``` dan ```JSON by ID``` :

    Setelah menyelesaikan kedua fungsi ```show_xml_by_id``` dan ```show_json_by_id```, saya lanjutkan dengan mengimport kedua fungsi tersebut ke ```urls.py``` di ```main``` dan menambahkan path
    ```py
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    ```
    untuk bisa mengakses proyek Django melalui  http://localhost:8000/xml/[id] atau http://localhost:8000/json/[id] sesuai dengan id item yang diinginkan

## Mengakses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.


**XML**

<img width="644" alt="xml fix" src="https://github.com/nabilazainina/glowventory/assets/112367952/eb1e6832-8905-4a9b-a5cf-a41083166225">


**JSON**

<img width="651" alt="json" src="https://github.com/nabilazainina/glowventory/assets/112367952/f565a07e-9587-402d-9995-cdbb58191aa9">


**HTML (create-item)**

<img width="668" alt="create-item" src="https://github.com/nabilazainina/glowventory/assets/112367952/3eb6e9e3-d641-4bdd-97cb-87b1893bdc1d">


**XML by ID**

<img width="665" alt="xml 1" src="https://github.com/nabilazainina/glowventory/assets/112367952/80983a68-6e49-428e-8cef-8d41d976eb9b">


**JSON by ID**

<img width="417" alt="json 2" src="https://github.com/nabilazainina/glowventory/assets/112367952/4a954ba7-dbb5-41cd-a400-43fb1e5bc009">

#
# TUGAS 4

## Apa itu Django ```UserCreationForm```, dan jelaskan apa kelebihan dan kekurangannya?

Django memiliki sistem autentikasi user yang akan menghandle akun, grup, akses, dan cookie-based user session. UserCreationForm sendiri digunakan untuk membuat suatu autentikasi pengguna baru. UserCreationForm pada Django akan membuat dan menyimpan pengguna baru dengan tiga bidang: username, password1, dan password2 untuk konfirmasi kata sandi pertama. UserCreationForm harus diimport dari django.contrib.auth.forms dan merupakan modul bawaan yang mewarisi kelas ModelForm

## Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?

Di dalam konteks Django, autentikasi dan otorisasi adalah dua konsep yang berbeda namun saling terkait dalam manajemen pengguna dan akses ke fitur aplikasi web. 

* ```AUTENTIKASI``` Autentikasi adalah proses memverifikasi identitas user yang terhubung ke aplikasi. Autentikasi akan memastikan bahwa pengguna adalah orang yang mereka klaim sebelum diizinkan untuk mengakses lebih lanjut. Django memiliki sistem autentikasi pengguna yang sudah tersedia secara bawaan seperti permission dan groups. Django juga tidak menyajikan beberapa fitur yang sering ditemukan dalam sistem autentikasi web karena masalah umu biasanya sudah diimplementasikan dalam paket eksternal seperti memeriksa kekuatan sandi dll

* ```OTORISASI``` Otorisasi sendiri adalah proses yang menentukan akses dan izin yang dimiliki pengguna yang sudah terverifikasi. Otorisasi ini akan mengontrol apa yang dapat diakses atau dilakukan pengguna setelah berhasil login. Dalam Django sendiri, otorisasi melibatkan pengatursan izin akses dan kontrol akses ke fitur.

> Dengan kata lain, autentikasi akan menverifikasi identitas pengguna yang akan masuk ke aplikasi, sementara otorisasi akan menentukan apa yang diizinkan untuk dilakukan oleh pengguna yang telah terotentikasi.

## Apa itu _cookies_ dalam konteks aplikasi web, dan bagaimana Django menggunakan _cookies_ untuk mengelola data sesi pengguna?

Cookies adalah text file kecil yang dibuat peramban web dan disimpan sebagai respons terhadap permintaan tertentu ke Web-Server. Permintaan tersebut dikirim menggunakan protokol HTTP, namun bersifat _stateless_ atau tanpa status sehingga tidak membantu mengenali apakah pengguna yang masuk merupakan pengguna baru atau pengguna yang telah mengunjungi situs sebelumnya. Django memanfaatkan cookies untuk mengelola informasi sesi pengguna melalui serangkaian metode yang tersedia pada objek HttpResponse. Dalam konteks ini, objek tersebut menawarkan metode untuk mengatur, menghapus, dan membaca cookies, memungkinkan pengelolaan yang efektif terhadap data sesi yang terkait dengan pengguna.

## Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?

Secara umum, cookies sangat aman ketika diimplementasikan dengan benar. Akan tetapi, banyak sekali serangan yang dapat dilakukan melalui cookies. Dalam kondisi yang normal, cookie tidak dapat mentransfer malware atau virus karena data yang dibawa tidak berubah saat berpindah dari komputer lokal ke website dan sebaliknya.

Akan tetapi, pengguna atau developer tetap harus berhati-hati untuk selalu menghindari pengunjungan situs berbahaya dan mencurigakan. Hal tersebut dilakukan untuk mencegah informasi dalam cookie user direbut dari pihak tidak bertanggung jawab.

Contohnya salah satu jenis cookie yakni third-party cookies yang dihasilkan oleh situs web berbeda dari yang pengunjung kunjungi. Misalnya cookies hasil iklan di web-web bajakan dan semacamnya. Pengunjungan situs-switus ilegal atau bajakan dapat menjadi keamanan yang cukup besar karena dapat mengancam privasi pengguna perdasarkan pola penelusuran dan riwayat individu. 

Bahaya lain yang dapat diperhatikan adalah cookie-hijacking, yaitu kegiatan cyberattack yang menargetkan user dengan memanfaatkan section cookies yang tidak terhubung dengan web. 

## Jelaskan secara step-by-step cara kamu mengimplementasikan checklist di atas secara step-by-step

### :white_check_mark: Mengimplementasikan fungsi ```registrasi```, ```login```, dan ```logout`` untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar

Saya mulai checklist ini dengan menambahkan beberapa import seperti ```redirect```, ```UserCreationForm```, dan ```messages``` pada ```views.py``` untuk mengimpor formulir bawaan yang akan memudahkan pembuatan formulir pendaftaran pengguna dalam aplikasi web. 

Kemudian, saya mulai mengimplementasikan fungsi pertama yaitu fungsi registrasi. Saya membuat suatu function ```register``` yang menerima parameter ```request``` di views.py yang akan membuat UserCreationForm baru, memvalidasi input, serta menyimpan data dari form tersebut. Function juga akan mengembalikan messages apabila akun sudah berhasil tersimpan.

Kemudian, pada file yang sama, saya implementasikan fungsi kedua untuk menghandle login yaitu, ```login_user```. Setelah mengimport ```authenticate``` dan ```login``` dari ```django.contrib.auth```, saya lanjutkan dengan membuat fungsi baru yaitu ```def login_user``` yang menerima parameter ```request```. Function tersebut akan melakukan autentikasi pengguna berdasarkan username dan password yang diterima dari request pengguna yang akan login. 

Selanjutnya, saya akan membuat fungsi terakhir yaitu fungsi ```logout```. Saya akan mengimport ```logout``` dari ```django.contrib.auth``` dan menambahkan potongan kode function ```def logout_user()``` yang akan menghapus sesi pengguna yang masuk dan mengarahkan pengguna ke halaman login dalam aplikasi.

Setelah membuat function untuk views, saya lanjutkan dengan membuat sebuah berkas ```html``` baru untuk masing-masing fungsi yang akan mengimplementasikan register, login, dan logout. Apabila ```register.html```, ```login.html```, dan ```logout.html``` sudah dibuat, saya lanjutkan dengan menambahkan _path url_ dari ketiga function baru (login, logout, register) ke dalam ```urlpatterns``` untuk bisa mengakses ketiga fungsi yang sudah diimport ke ```urls.py``` di main.

### :white_check_mark: Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal

Checklist ini saya mulai dengan menekan button ```Register Now``` dan memasukkan beberapa data ke dalamnya, sesuai dengan yang diminta yaitu username, pass, dan autentikasi pass. Akun yang saya buat adalah

|   Nama Akun    |   Password     |
| -------------  | -------------- |
| nabila.zainina |  bisapbpletsgo |
|    bella       |  halohalohalo  |

Setelah itu, ketika masuk ke user yang saya inginkan, saya lanjutkan dengan menambahkan item dengan menekan tombol add item serta mengisi field di masing-masing tabel user. 

### :white_check_mark: Menghubungkan model ```Item``` dengan ```User```

Bagian ini akan menghubungkan section halaman user dengan item yang dia masukkan. Daya mulai dengan mengimport ```User``` ke ```models.py``` pada ```main```. Kemudian saya tambahkan line of code
```py
user = models.ForeignKey(User, on_delete=models.CASCADE)
```
pada mode ```Item``` yang akan mrnghubungkan suatu item dengan satu user melalui hubungan dimana sebuah item pasti terasosiasikan dengan seorang user. Setelah itu, saya melakukan beberapa perubahan pada fungsi ```create_item``` saya di ```views.py``` dengan menambahkan 
```py
item = form.save(commit=False)
```
Yang digunakan untuk mencegah agar Django tidak langsung menyimpan objek yang telah dibuat dari form langsung ke database agar objek bisa dimodifikasi lebih dulu. Kemudian, saya juga menambahkan
```py
item.user = request.user
```
Yang akan menandakan bahwa suatu objek dimiliki pengguna yang sedang login.

Saya lanjutkan dengan mengubah beberapa hal di fungsi ```show_main``` seperti ```item = Item.objects.filter(user=request.user)``` untuk menampilkan object ```Item``` yang sudah terasosiasi dengan pengguna yang sedan login. Serta kode ```'name': request.user.username``` yang akan menampilkan _username_ pengguna yang sedang login.

Saya menyimpan semua perubahan dengan melakukan migrasi model dan checklist sudah terpenuhi.

### :white_check_mark: Menampilkan detail informasi pengguna yang sedang _logged in_ seperti _username_ dan menerapkan ```cookies``` seperti ```last login``` pada halaman utama aplikasi.

Untuk menjawab checklist ini, saya mulai dengan menambahkan ```datetime``` pada ```views.py```. Kemudian, saya akan menambahkan _cookie_ yang bernama ```last_login``` pada fungsi ```login_user``` untuk bisa melihat kapan terakhir kali pengguna melakukan _login_ dengan menambahkan beberapa line of code
* ```login(request, user)``` = Akan melakukan login
* ```response = HttpResponseRedirect(reverse("main:show_main"))``` yang akan membuat response
* ```response.setcookie('last_login', str(datetime.datetime.now()))``` yang akan membuat _cookie_ _lastlogin_ dan menambahkannya ke rensponse.

Kemudia saya menambahkan ```'last_login': request.COOKIES['last_login']``` pada ```context``` fungsi ```show_main``` untuk menambahkan informasdi cookie pada respon yang akan ditampilkan. Kemudian, saya modifikasi fungsi ```logout_user``` dengan menambahkan ```response.delete_cookie('last_login')``` untuk mengahpus _cookie_ kast_login saat pengguna logout. Saya tambahkan ```<h5>Sesi terakhir login: {{ last_login }}</h5>``` pada ```main.html``` untuk menampilkan data dari last_login.

#
# TUGAS 5

### :white_check_mark: Jelaskan manfaat setiap _element selector_ dan kapan waktu yang tepat untuk menggunakannya

Selector elemen pada CSS adalah cara untuk menargetkan dan memilih elemen HTML tertentu yang ingin di-styling. Selector ini memungkinkan Anda mendefinisikan gaya atau style CSS yang akan diterapkan pada elemen-elemen tersebut. Berikut adalah beberapa jenis selector elemen yang umum digunakan dalam CSS:

**Selector Elemen (Tag Name)** 
* Memilih elemen berdasarkan tag name (misalnya, div, p, h1) bermanfaat apabila ingin menerapkan gaya umum untuk sekelompok elemen dengan tag yang sama.

**Selector ID (#)**
* Memilih elemen berdasarkan ID unik, bermanfaat apabila ingin menerapkan gaya khusus untuk satu elemen tertentu yang memiliki ID unik.

**Selector Kelas (.kelas)**
* Memilih elemen berdasarkan kelas yang diberikan, berguna apabila digunakan ketika ingin menerapkan gaya yang sama pada sekelompok elemen yang memiliki kelas yang sama

**Selector Kombinasi (,)**
* Memilih beberapa elemen dengan gaya yang sama, bermanfaat apabila ingin menerapkan gaya yang sama pada beberapa elemen dengan tag name atau kelas berbeda

**Selector Universal (*)**
* Memilih semua elemen dalam dokumen dan dapat digunakan jika ingin menggunakan satu gaya pada keseluruhan halaman web.

## :white_check_mark: Jelaskan HTML5 Tag yang kamu ketahui

<nav>:
Menyediakan navigasi untuk halaman web.

<main>:
Mendefinisikan konten utama dari halaman web.

<section>:
Mengelompokkan konten terkait dalam suatu bagian.

<p>:
Mendefinisikan sebuah paragraf teks.

<a>:
Membuat tautan (link) ke halaman web atau sumber daya lainnya.

## :white_check_mark: Jelaskan perbedaan antara _margin_ dan _padding_

1. **Margin (Margin):**
   Margin adalah area di sekitar elemen, yang mencakup ruang antara elemen tersebut dan elemen lain di sekitarnya. Margin tidak memiliki warna latar belakang dan tidak dapat diisi dengan konten. Margin digunakan untuk mengatur jarak antara elemen dengan elemen lain di sekitarnya.

2. **Padding (Padding):**
   Padding adalah ruang di antara batas elemen dan kontennya. Padding berada di dalam elemen dan memberikan jarak antara konten elemen dan batas elemen. Padding dapat memiliki warna latar belakang dan akan mempengaruhi tampilan elemen tersebut.

Jadi, sementara margin mengendalikan jarak antara elemen dan elemen lain di sekitarnya, padding mengendalikan jarak antara konten elemen dan batas elemen itu sendiri. Dengan kata lain, properti margin mengontrol ruang di luar elemen, sedangkan properti padding mengontrol ruang di dalam elemen.

## :white_check_mark: Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?

Bootstrap dan Tailwind CSS adalah dua kerangka kerja (framework) yang populer untuk membangun tata letak dan antarmuka pengguna pada aplikasi web. Berikut adalah perbedaan dan ringkasan dari keduanya:

### Bootstrap:
- **Deskripsi**: Bootstrap adalah salah satu kerangka kerja paling populer untuk mengembangkan aplikasi web responsif dan mobile-first.
- **Karakteristik Utama**:
  - Menyediakan tema dan template siap pakai.
  - Memiliki kelas-kelas bawaan yang mudah digunakan dan didesain untuk membangun antarmuka pengguna.
  - Aplikasi yang dibuat dengan Bootstrap cenderung memiliki tata letak yang mirip karena menggunakan template bawaan.
  - Sudah ada sejak lama dan dikenal efisien dalam responsivitasnya, menghemat waktu pengembangan.
- **Ukuran File**: Memerlukan ukuran file yang cukup besar.

### Tailwind CSS:

- **Deskripsi**: Tailwind CSS adalah kerangka kerja CSS yang semakin populer untuk menciptakan antarmuka pengguna yang dioptimalkan dan fleksibel.
- **Karakteristik Utama**:
  - Menggunakan kelas utilitas yang memungkinkan pengembang membangun antarmuka pengguna yang unik dan sesuai kebutuhan.
  - Tidak memiliki templat atau tata letak bawaan, memungkinkan fleksibilitas tinggi dalam desain.
  - Masih merupakan kerangka kerja yang terus berkembang dan memperbarui fungsionalitasnya.
- **Ukuran File**: Memerlukan ukuran file yang lebih kecil.

### Ringkasan:
-Bootstrap menyediakan template dan kelas bawaan untuk membangun antarmuka dengan cepat dan relatif seragam sementara Tailwind CSS memungkinkan pembuatan antarmuka yang unik dengan menggunakan kelas utilitas tanpa templat bawaan.Bootstrap sendiri telah ada lebih lama dan efisien dalam responsivitas, sementara Tailwind CSS masih dalam perkembangan dan memiliki ukuran file yang lebih kecil.

## :white_check_mark: Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Saya memulai pekerjaan saya dengan membuat Bootstrap ke aplikasi melalui base.html sesuai ketentuan. Kemudian, saya lanjutkan dengan menambahkan vitur edit pada aplikasi.

Fitur edit saya lakukan dengan menambahkan fungsi ```def edit_product(request, id)``` ke ```views.py```. Kemudian saya tambahkan berkas ```edit_product.html``` pada ```main/templates``` sesuai dengan ketentuan format edit product yang saya inginkan.Selanjutnya saya tambahkan pasth url ke   ```urlpatterns``` untuk mengakses fungsi yang sudah diimpor. Selanjutnya, saya tambahkan button baru di ```main.html``` untuk mengedit product, dan memastikan url pattern tepat.

Step berikutnya, saya mulai melakukan edit dan mendesign web saya menggunakan CSS. Pertama, saya tambahkan navbar pada main.html saya. Setelah itu, saya tambahkan CSS code dengan ```<style>``` yang akan menampung keseluruhan design saya. Untuk mendesign saya lakukan dengan memilih element selector yang sekiranya saya ingin design bersama, berikut contohnya:

```
   <style>
        body {
            font-family: 'Poppins', sans-serif;
            background-color: #f0f8ff; /* Baby Blue / Soft Blue */
            margin: 0;
            padding: 0;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        nav.navbar {
            width: 100%;
            font-size: 18px;
            color: white;
            background-color: #000080; /* Dark Blue */
            display: flex;
            justify-content: space-between;
            padding: 10px 10px;
            text-align: center;
        }

        nav.navbar a {
            text-align: left;
            color: white;
            margin-left: 20px;
            font-weight: bold;
        }

        .user-info.welcome-text {
            font-family: Verdana, sans-serif; /* Change font to Verdana */
            font-size: 12px; /* Adjusted font size */
            margin-top: 3px; /* Adjusted margin */
            align-items: baseline;
        }

        .logout-button {
            display: flex;
            align-items: center;
            margin-right: 20px; /* Adjusted margin */
        }
        
        .logout-button i {
            margin-right: 5px; /* Adjusted margin */
        }

        .container {
            padding: 20px;
            text-align: center;
        }

        h1 {
            color: #000080; /* Dark Blue */
            padding: 20px 0;
        }

        h4{
            color: #333; /* Dark Gray */
            font-size: 13px;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
            text-align: center;
            border: 2px solid #004d40; /* Darker Soft Blue */
        }

        th, td {
            border: 1px solid #004d40; /* Darker Soft Blue */
            padding: 15px;
            text-align: center;
            background-color: #e0f7fa; /* Light Blue */
        }

        td {
            font-size: 13px;
        }

        th {
            background-color: #004d40; /* Darker Soft Blue */
            color: white;
        }

        a.button {
            text-decoration: none;
            color: white;
            background-color: #00838f; /* Soft Blue */
            padding: 12px 24px;
            border-radius: 5px;
            font-size: 14px;
            transition: background-color 0.3s;
            margin: 10px 10px 0; /* Adjusted margin */
            display: inline-block;
        }

        a.button:hover {
            background-color: #004d40; /* Darker Soft Blue on hover */
        }

        p {
            margin: 10px 0 5px; /* Adjusted margin */
            font-size: 12px; /* Reduced font size for item count */
            padding-bottom: 2%;
            padding-top: 5%;
        }

        .last-login {
            font-size: 10px; /* Reduced font size for last login */
            color: #000080; /* Dark Blue */
            margin-top: 10px; /* Adjusted margin top */
            padding-top: 8%;
        }

        .container {
            padding: 20px;
            text-align: center;
            margin-bottom: 50px; /* Tambahkan margin bottom yang cukup besar */
        }

        .footer {
            position: fixed;
            bottom: 0;
            width: 100%;
            background-color: #f0f0f0;
            padding: 10px;
            padding-left: 5%;
            text-align: left;
            text-decoration: solid;
            z-index: 999; /* Atur z-index untuk memastikan footer muncul di atas konten lain */
            font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
        }
    </style>
```

Implementasi tersebut saya lakukan di file-file lainnya, tergantung dengan design yang saya inginkan di laman web saya, baik di halaman main, register, login. Saya juga mendesign kembali navbar serta halaman edit item.

#
# TUGAS 6

## Jelaskan perbedaan antara asynchronous programming dengan synchronous programming

* **Synchronous Programming**
Dalam pemrograman sinkron, tugas-tugas dieksekusi secara berurutan, satu per satu. Program menunggu tugas saat ini selesai sebelum melanjutkan ke tugas selanjutnya

* **Asynchronous Programming**
Asynchronous programming merupakan sebuah pendekatan pemrograman yang tidak terikat pada input output (I/O)  protokol. Dalam pemrograman asinkron, tugas-tugas dapat dieksekusi secara bersamaan tanpa harus menunggu tugas sebelumnya selesai. Ini memungkinkan program untuk melakukan beberapa operasi secara bersamaan.

## Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma event-driven programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini

Paradigma event-driven adalah pendekatan di mana program merespons kejadian atau "event" yang terjadi pada suatu waktu tertentu, seperti klik mouse, pengisian formulir, atau permintaan AJAX. Program akan merespons event ini dengan menjalankan fungsi atau tindakan yang telah ditentukan sebelumnya.

Dalam penggunaan AJAX di program, event-driven programming dapat dilihat ketika user ingin menambahkan item ke inventory. Ketika user menekan tombol "Add Item by AJAX", program akan langsung berpindah ke event berikutnya yaitu form pengisian barang.

## Jelaskan penerapan asynchronous programming pada AJAX

Asynchronous programming adalah paradigma pemrograman yang memungkinkan operasi untuk dilakukan secara bersamaan atau tanpa menghalangi operasi lain. Dalam konteks pengembangan web, pemrograman asinkron digunakan untuk meningkatkan kinerja dan responsifitas aplikasi web. AJAX (Asynchronous JavaScript and XML) adalah teknik yang menggunakan pemrograman asinkron untuk mengirim dan menerima data dari server web tanpa perlu me-refresh seluruh halaman web.

Berikut penjelasan mengenai penerapan pemrograman asinkron pada AJAX, beserta contohnya:

### Objek XMLHttpRequest(XHR)
Objek XMLHttpRequest adalah dasar dari AJAX dan memungkinkan Anda untuk mengirimkan permintaan HTTP ke server web secara asynchronous.

### Penanganan Event
Operasi asynchronous dalam AJAX dikelola melalui penanganan event. Penanganan event ini dipicu ketika suatu tindakan asynchronous, seperti penyelesaian permintaan HTTP, terjadi.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)

### :white_check_mark: Mengubah tugas 5 yang telah dibuat sebelumnya menjadi menggunakan AJAX

Untuk bagian ini, saya menggunakan AJAX GET dan AJAX POST. Pertama, saya lakukan dengan membuat dua fungsi baru, pertama untuk get json dan kedua untuk menambahkan item baru menggunakan AJAX. Untuk metode get, saya lakukan dengan menambahkan views baru bernama ```get_product_json``` untuk mengembalikan data JSON dan menampilkan data produk pada HTML dengan ```fetch ```. Kemudian, pada main.html saya akan menambahkan script untuk AJAX yang diisi fungsi ```getProducts()``` yang akan menggunakan ```fetch()``` API ke data JSON secara _asynchronus_ yang kemudian akan melakukan _parse_ dengan fungsi ```then()``` untuk mengubah data JSON menjadi objek JavaScript. Kemudian, saya menambahkan function ```refreshProducts()``` pada script yang akan menampilkan card product saya. Kode yang saya masukkan adalah

```
            const productTable = document.getElementById("product_table");
            productTable.innerHTML = "";

            const products = await getProducts();
            let htmlString = "<div class='row'>";  // Start a new row

            products.forEach((item, index) => {
                if (index % 3 === 0 && index !== 0) {
                    htmlString += "</div><div class='row'>";  // Close previous row and start a new row for every 3 cards
                }

                htmlString += `
                    <div class="col-md-4">
                        <div class="card-item">
                            <div class="card mx-auto p-3" style="width: 18rem;">
                                <div class="card-body">
                                    <h2 class="card-title">${item.fields.name}</h2>
                                    <p class="card-text">Amount: ${item.fields.amount}</p>
                                    <p class="card-text">Price: ${item.fields.price}</p>
                                    <p class="card-text">${item.fields.description}</p>
                                    <p class="card-text">Category: ${item.fields.category}</p>
                                    <a style="justify-content: baseline;" href='edit-item/${item.pk}' class="btn btn-outline-warning" onclick="editItem(${item.pk})">Edit</a>
                                    <button style="justify-content: baseline;" class="btn btn-outline-danger" onclick="deleteProduct(${item.pk})">Delete</button>
                                </div>
                            </div>
                        </div>
                    </div>`;
            });

            htmlString += "</div>";  // Close the last row
            productTable.innerHTML = htmlString;
```

Fungsi ```refreshProducts()``` akan digunakan untuk memanggil fungsi tersebut lagi apabila user membuka halaman web.

Untuk AJAX POST, saya mulai dengan membuat sebuah fungsi baru ```add_product_ajax``` pada views.py. Saya menggunakan ```@csrf_exempt``` melalui ```from django.views.decorators.csrf import csrf_exempt```. Fungsi ```add_product_ajax``` akan mengambil value dari model dan akan membuat object baru dengan parameter sesuai values dari request.

Selanjutnya, saya tambahkan url dari kedua fungsi tersebut di urls.py

```
    path('get-product/', get_product_json, name='get_product_json'),
    path('create-ajax/', add_product_ajax, name='add_product_ajax'),
```

Setelah mempersiapakan function, saya mulai mengeksekusi di ```main.html``` dengan mengubah fitur table card item saya menjadi ajax. Pertama, saya tambahkan kode
```
<div class="card-container" id="product_table"></div>
```
Kode tersebut dibuat untuk menampilkan struktur card yang sudah dibuat di atas.

Selanjutnya, saya tambahkan kode untuk mengimplementasikan modal Bootstrap pada aplikasi. Modal bootstrap ini akan menjadi struktur form yang terhubung dengan AJAX. Form pada modal tersebut saya sesuaikan dengan model pada aplikasi Glowventory. Di akhir block code ```<Script>``` tidak lupa saya tambahkan pemanggilan fungsi ```refreshProduct()``` yang nantinya akan menampilkan daftar item terbaru tanpa reload halaman utama secara keseluruhan. Terakhir saya tambahkan ```button``` yang akan menampilkan modal dan juga mengclose dengan kode
```
<button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
<button type="button" class="btn btn-primary" id="button_add" data-bs-dismiss="modal">Add Item</button>
```

Selain itu, saya menambahkan beberapa fungsi pada block ```<Script>``` saya untuk menambahkan item, menghapus, dan mengedit item dengan kode block seperti berikut.

```
function addProduct() {
    fetch("{% url 'main:add_product_ajax' %}", {
        method: "POST",
        body: new FormData(document.querySelector('#form'))
    }).then(refreshProducts)

    document.getElementById("form").reset()
    return false
}

function editProduct(productId) {
    fetch(`{% url 'main:edit_item' 0 %}${productId}/`, {
    method: "POST",
    body: new FormData(document.querySelector('#form'))
}).then(refreshProducts)

document.getElementById("form").reset()
return false
}

function deleteProduct(productId) {
    fetch(`{% url 'main:delete' 0 %}`.replace("0", productId), {
        method: "POST",
        body: new FormData(document.querySelector('#form'))
    }).then(refreshProducts)

    document.getElementById("form").reset()
    return false
}
```

### :white_check_mark: Melakukan perintah collectstatic

Untuk bagian ini saya mulai dengan menambahkan ```STATIC_ROOT``` pada ```settings.py``` saya. Kemudian, saya tambahkan potongan kode
```STATIC_ROOT = os.path.join(BASE_DIR, 'static')``` 
yang akan menentukan absolute path ke direktori static files ketika menjalankan perintah collectstatic. Kemudian saya lanjutkan dengan menjalankan perintah ```collectstatic``` dengan menjalankan perintah ```python manage.py collectstatic``` yang kemudian akan membuat sebuah direktori ```static/admin``` baru pada proyek saya.





