from PyQt5.QtWidgets import *
from islem_python import Ui_Form
from veritabani import veritabani

class islemSayfa(QWidget):
    def __init__(self):
        super().__init__()
        self.islem = Ui_Form()  
        self.islem.setupUi(self)
        self.veritabani = veritabani()
        self.islem.guncelle_pushButton.clicked.connect(self.Guncelle)
        self.islem.sil_pushButton.clicked.connect(self.sil)
        
    def Guncelle(self):
        _id_text = self.islem.id_label.text()
        if _id_text:
            try:
                _id = int(_id_text)
                enst_adi = self.islem.enst_lineEdit.text()
                fiyat = self.islem.fiyat_lineEdit.text()
                stok_Sayisi = self.islem.stok_sayisi_lineEdit.text()
                satis_Sayisi = self.islem.satis_sayisi_lineEdit.text()
                
                # Herhangi bir alanın boş olup olmadığını kontrol et
                if not enst_adi or not fiyat or not stok_Sayisi or not satis_Sayisi:
                    QMessageBox.warning(self, "Bilgi", "Lütfen tüm alanları doldurun")
                    return

                # Satış sayısının stok sayısından büyük olup olmadığını kontrol et
                if int(satis_Sayisi) > int(stok_Sayisi):
                    QMessageBox.warning(self, "Bilgi", "Satış sayısı stok sayısından büyük olamaz")
                    return
                
                # Negatif sayı girişini kontrol et
                if float(fiyat) < 0 or int(stok_Sayisi) < 0 or int(satis_Sayisi) < 0:
                    QMessageBox.warning(self, "Bilgi", "Negatif değer girişi yapılamaz")
                    return

                # Güncelleme işlemini gerçekleştir
                self.veritabani._Guncelle(_id, enst_adi, fiyat, stok_Sayisi, satis_Sayisi)
                
                QMessageBox.information(self, "Bilgi", "Güncelleme işlemi başarıyla gerçekleşti")
            except ValueError:
                QMessageBox.warning(self, "Bilgi", "Geçersiz kimlik (ID) veya sayısal değer")
        else:
            QMessageBox.warning(self, "Bilgi", "Geçersiz kimlik (ID) değeri")

    def sil(self):
        _id = self.islem.id_label.text()
        sil = self.veritabani.sil(_id)

        if sil:
            QMessageBox.information(self,"Bilgi","Kayıt Başarıyla Silindi")
            self.hide()
        else:
            QMessageBox.warning(self,"Bilgi","Kayıt Silinemedi.")
