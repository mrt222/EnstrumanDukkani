Enstrüman Dükkanı Uygulaması Kullanım Kılavuzu
Bu kullanım kılavuzu, Enstrüman Dükkanı uygulamasının nasıl kullanılacağına dair adım adım talimatlar içermektedir. Uygulamayı başarıyla kullanabilmek için aşağıdaki adımları takip edebilirsiniz:

1. Enstrüman Dükkanı Uygulamasını Başlatma
Uygulamayı başlatmak için main.py dosyasını çalıştırın. Bu, Ana Sayfa penceresini açacaktır.

bash
Copy code
python main.py
2. Enstrüman Ekleme
Ana Sayfa'da, "Enstrüman Ekle" butonuna tıklayarak yeni bir enstrüman ekleyebilirsiniz. Açılan pencerede:

"Enstrüman Adı": Yeni enstrümanın adını girin.
"Fiyat": Enstrümanın fiyatını girin.
"Stok Sayısı": Enstrümanın mevcut stok sayısını belirtin.
"Satış Sayısı": Enstrümanın daha önce gerçekleşmiş satış sayısını girin.
Tüm bilgileri doldurduktan sonra "Kaydet" düğmesine basarak enstrümanı kaydedin. Eğer girdiğiniz bilgiler geçerli değilse, uyarı mesajlarıyla bilgilendirileceksiniz.

3. Enstrümanları Görüntüleme ve İşlem Yapma
Ana Sayfa'da, mevcut enstrümanları listeleyen bir tablo bulunmaktadır. Bu tablodaki herhangi bir satıra tıkladığınızda, ilgili enstrümanın bilgilerini görmek ve düzenlemek için "İŞLEM" butonuna tıklayabilirsiniz.

"İŞLEM" butonuna tıkladığınızda, seçili enstrümanın bilgileri "İşlem Sayfası"nda görüntülenir.
"Güncelle" düğmesini kullanarak enstrüman bilgilerini güncelleyebilirsiniz.
"Sil" düğmesini kullanarak enstrümanı veritabanından silebilirsiniz.
4. Müşteri Bilgilerini Görüntüleme
Ana Sayfa'da, "Müşteri Bilgileri" butonuna tıklayarak müşteri bilgilerini görüntüleyebilirsiniz. Açılan pencerede:

"Arama": Müşteri adına göre arama yapabilirsiniz. Arama kutusuna müşteri adını girerek tabloda filtreleme yapabilirsiniz.
Müşteri tablosunda, müşteri adı, soyadı, aldığı enstrüman, adedi, toplam tutarı ve iletişim bilgileri listelenir.




KAYNAK KODLARININ BULUNDUĞU SAYFALAR:
main.py
ykayit.py
islem.py
mbilgi.py
veritabani.py

