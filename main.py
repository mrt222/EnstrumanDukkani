from PyQt5.QtWidgets import *
from main_python_2 import Ui_Form
from ykayit import YeniKayitSayfa
from mbilgi import BilgiSayfa
from islem import islemSayfa
from veritabani import veritabani

class Anasayfa(QWidget):
    def __init__(self):
        super().__init__()
        self.formAnasayfa = Ui_Form()  
        self.formAnasayfa.setupUi(self)
        self.yeniKayit = YeniKayitSayfa()
        self.bilgi = BilgiSayfa()
        self.islem = islemSayfa()
        self.veritabani = veritabani()

        self.kayitGoster()
        self.formAnasayfa.enstr_ekle_buton.clicked.connect(self.yeniKayitAc)
        self.formAnasayfa.musteri_bilgi_button.clicked.connect(self.bilgigoster)
        self.formAnasayfa.tableWidget.clicked.connect(self.Islem)
        self.formAnasayfa.arama_yap.textChanged[str].connect(self.ara)
        
        
    def ara(self):
        kolonlar = ["ID", "ENSTRÜMAN ADI", "FİYAT", "STOK SAYISI", "SATIŞ SAYISI", "İŞLEM"]
        self.formAnasayfa.tableWidget.setColumnCount(len(kolonlar))  # Sütun sayısını ayarla
        self.formAnasayfa.tableWidget.setHorizontalHeaderLabels(kolonlar)  # Kolon başlıklarını ayarla
        enst_adi = self.formAnasayfa.arama_yap.text()

        veriler = self.veritabani.ara(enst_adi)
        print(veriler)
        if veriler:
            self.formAnasayfa.tableWidget.setRowCount(len(veriler))  # Satır sayısını ayarla
            for satir, veri in enumerate(veriler):
                self.formAnasayfa.tableWidget.setItem(satir, 0, QTableWidgetItem(str(veri[0])))  # ID değerini ekleyin
                for sutun, deger in enumerate(veri[1:], 1):  # 1'den başlayarak diğer sütunları ekleyin
                    self.formAnasayfa.tableWidget.setItem(satir, sutun, QTableWidgetItem(str(deger)))
                # İşlem sütununa "İŞLEM" yazısını ekleyin
                self.formAnasayfa.tableWidget.setItem(satir, len(kolonlar) - 1, QTableWidgetItem("İŞLEM"))

        # Tablonun genişliğini sığabilecek şekilde ayarlayın
        self.formAnasayfa.tableWidget.horizontalHeader().setStretchLastSection(True)

    def Islem(self,):
        secili_Satir = self.formAnasayfa.tableWidget.currentRow()
        tiklanan_sutun_no = self.formAnasayfa.tableWidget.currentColumn()
        if tiklanan_sutun_no == 5:
            secilen_id = self.formAnasayfa.tableWidget.item(secili_Satir,0).text()
            secilen_ad = self.formAnasayfa.tableWidget.item(secili_Satir,1).text()
            seceilen_fiyat = self.formAnasayfa.tableWidget.item(secili_Satir,2).text()
            secilen_stok = self.formAnasayfa.tableWidget.item(secili_Satir,3).text()
            secilen_satis =  self.formAnasayfa.tableWidget.item(secili_Satir,4).text()
            
            self.islem.islem.id_label.setText(secilen_id)
            self.islem.islem.enst_lineEdit.setText(secilen_ad)
            self.islem.islem.fiyat_lineEdit.setText(seceilen_fiyat)
            self.islem.islem.stok_sayisi_lineEdit.setText(secilen_stok)
            self.islem.islem.satis_sayisi_lineEdit.setText(secilen_satis)


            self.islem.show()

    def yeniKayitAc(self):
        self.yeniKayit.show()

    def bilgigoster(self):
        self.bilgi.show()

    def destekAl(self):
        self.destek.show()

    def kayitGoster(self):
        kolonlar = ["ID", "ENSTRÜMAN ADI", "FİYAT", "STOK SAYISI", "SATIŞ SAYISI", "İŞLEM"]
        self.formAnasayfa.tableWidget.setColumnCount(len(kolonlar))  # Sütun sayısını ayarla
        self.formAnasayfa.tableWidget.setHorizontalHeaderLabels(kolonlar)  # Kolon başlıklarını ayarla

        veriler = self.veritabani.kayitGoster()
        if veriler:
            self.formAnasayfa.tableWidget.setRowCount(len(veriler))  # Satır sayısını ayarla
            for satir, veri in enumerate(veriler):
                self.formAnasayfa.tableWidget.setItem(satir, 0, QTableWidgetItem(str(veri[0])))  # ID değerini ekleyin
                for sutun, deger in enumerate(veri[1:], 1):  # 1'den başlayarak diğer sütunları ekleyin
                    self.formAnasayfa.tableWidget.setItem(satir, sutun, QTableWidgetItem(str(deger)))
                # İşlem sütununa "İŞLEM" yazısını ekleyin
                self.formAnasayfa.tableWidget.setItem(satir, len(kolonlar) - 1, QTableWidgetItem("İŞLEM"))

        # Tablonun genişliğini sığabilecek şekilde ayarlayın
        self.formAnasayfa.tableWidget.horizontalHeader().setStretchLastSection(True)






app = QApplication([])
pencere = Anasayfa()
pencere.show()
app.exec_()
