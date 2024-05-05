from PyQt5.QtWidgets import *
from yeni_kayit2_python import Ui_Form
from veritabani import veritabani


class YeniKayitSayfa(QWidget):
    def __init__(self):
        super().__init__()
        self.YeniKayit = Ui_Form()  
        self.YeniKayit.setupUi(self)
        self.YeniKayit.kaydet_pushButton.clicked.connect(self.kaydet)
        self.veritabani = veritabani()

    def float_mi(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    def integer_mi(self, value):
        try:
            int(value)
            return True
        except ValueError:
            return False

    def kaydet(self):
        enst_adi = self.YeniKayit.enstruman_lineEdit.text()
        fiyat = self.YeniKayit.fiyat_lineEdit.text()
        stok_sayisi = self.YeniKayit.stok_saysi_lineEdit.text()
        satis_sayisi = self.YeniKayit.satis_sayisi_lineEdit.text()

        if not  (self.float_mi(fiyat) and self.integer_mi(stok_sayisi) and self.integer_mi(satis_sayisi)):
            QMessageBox.warning(self, "Uyarı", "Fiyat, stok sayısı ve satış sayısı sayısal olmalıdır!")
            return 

        fiyat = float(fiyat)
        stok_sayisi = int(stok_sayisi)
        satis_sayisi = int(satis_sayisi)

        if stok_sayisi < 0 or satis_sayisi < 0 or fiyat < 0:
            QMessageBox.warning(self, "Uyarı", "Negatif değer girişi yapılamaz!")
            return
        elif satis_sayisi > stok_sayisi:
            QMessageBox.warning(self, "Uyarı", "Satış sayısı stok sayısından fazla olamaz!")
            return
        else:
            
            kayit_islemi = self.veritabani.kayitEkle(enst_adi, fiyat, stok_sayisi, satis_sayisi)
            if kayit_islemi > 0:
                QMessageBox.information(self, "Bilgi", "Kayıt başarıyla eklendi!")
                return
            else:
                QMessageBox.warning(self, "Uyarı", "Kayıt ekleme başarısız!")
                return
