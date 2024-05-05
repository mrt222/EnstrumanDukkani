from PyQt5.QtWidgets import *
from musteri_bilgi_python_3 import Ui_Form
from veritabani import veritabani

class BilgiSayfa(QWidget):
    def __init__(self):
        super().__init__()
        self.bilgi = Ui_Form()  
        self.bilgi.setupUi(self)
        self.veritabani = veritabani()
        self.musteriKayitGoster()
        self.bilgi.lineEdit.textChanged[str].connect(self.musteri_arama )




    def musteriKayitGoster(self):
     kolonlar = ["ID", "AD", "SOYAD", "ENSTRÜMAN", "ADET", "TOPLAM TUTAR","İLETİŞİM"]
     self.bilgi.tableWidget.setColumnCount(len(kolonlar))  # Sütun sayısını ayarla
     self.bilgi.tableWidget.setHorizontalHeaderLabels(kolonlar)  # Kolon başlıklarını ayarla

     veriler = self.veritabani._mkayitGoster()
     if veriler:
        self.bilgi.tableWidget.setRowCount(len(veriler))  # Satır sayısını ayarla
        for satir, veri in enumerate(veriler):
            self.bilgi.tableWidget.setItem(satir, 0, QTableWidgetItem(str(veri[0])))  # ID değerini ekleyin
            for sutun, deger in enumerate(veri[1:], 1):  # 1'den başlayarak diğer sütunları ekleyin
                self.bilgi.tableWidget.setItem(satir, sutun, QTableWidgetItem(str(deger)))

        # Tablonun genişliğini sığabilecek şekilde ayarlayın
        self.bilgi.tableWidget.horizontalHeader().setStretchLastSection(True)

    def musteri_arama(self):
     kolonlar = ["ID", "AD", "SOYAD", "ENSTRÜMAN", "ADET", "TOPLAM TUTAR","İLETİŞİM"]
     self.bilgi.tableWidget.setColumnCount(len(kolonlar))  # Sütun sayısını ayarla
     self.bilgi.tableWidget.setHorizontalHeaderLabels(kolonlar)  # Kolon başlıklarını ayarla
     musteri_Ad = self.bilgi.lineEdit.text()

     veriler = self.veritabani.musteri_arama(musteri_Ad)
     if veriler:
        self.bilgi.tableWidget.setRowCount(len(veriler))  # Satır sayısını ayarla
        for satir, veri in enumerate(veriler):
            self.bilgi.tableWidget.setItem(satir, 0, QTableWidgetItem(str(veri[0])))  # ID değerini ekleyin
            for sutun, deger in enumerate(veri[1:], 1):  # 1'den başlayarak diğer sütunları ekleyin
                self.bilgi.tableWidget.setItem(satir, sutun, QTableWidgetItem(str(deger)))

        # Tablonun genişliğini sığabilecek şekilde ayarlayın
        self.bilgi.tableWidget.horizontalHeader().setStretchLastSection(True)


   
   

