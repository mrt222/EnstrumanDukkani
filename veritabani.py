import sqlite3 
import os 

class veritabani():
    def __init__(self):
        dizin_yol = os.path.dirname(os.path.abspath(__file__))
        self.db = os.path.join(dizin_yol, 'enstr_dukkanı.db')
        print(self.db)
        

    def vtac(self):
        self.conn = sqlite3.connect(self.db)
        self.cursor = self.conn.cursor()

    def vtkapat(self):
        self.cursor.close()

    def kayitEkle(self,enst_adi,fiyat,stok_sayisi,satis_sayisi):
       try:
        self.vtac()
        sql = "insert into enstrumanlar ('ENSTRÜMAN ADI','FİYAT','STOK SAYISI','SATIŞ SAYISI') values (?,?,?,?)"
        self.cursor.execute(sql,(enst_adi,fiyat,stok_sayisi,satis_sayisi))
        self.conn.commit()
        return True
       except:
          return False
       finally:
          self.vtkapat()

    def kayitGoster(self):
       try:
          self.vtac()
          sql = "select * from enstrumanlar order by id "
          self.cursor.execute(sql)
          veriler = self.cursor.fetchall()
          return veriler
       except:
          return False
       finally:
          self.vtkapat

    def _Guncelle(self, id, enst_adi, fiyat, stok_Sayisi, satis_Sayisi):
     try:
        self.vtac()
        sql = "UPDATE enstrumanlar SET 'ENSTRÜMAN ADI' = ?, 'FİYAT' = ?, 'STOK SAYISI' = ?, 'SATIŞ SAYISI' = ? WHERE ID = ?"
        self.cursor.execute(sql, (enst_adi, fiyat, stok_Sayisi, satis_Sayisi, id))
        self.conn.commit()
        return True
     except:
        return False
     finally:
        self.vtkapat()

    def sil(self,_id):
       try:
          self.vtac()
          sql = "DELETE FROM enstrumanlar WHERE  ID = ?"
          self.cursor.execute(sql,(_id))
          self.conn.commit()
          return True
       except:
          return False
       finally:
          self.vtkapat()

    def _mkayitGoster(self):
       try:
          self.vtac()
          sql = "select * from musteri order by id "
          self.cursor.execute(sql)
          veriler = self.cursor.fetchall()
          return veriler
       except:
          return False
       finally:
          self.vtkapat()

    def ara(self, enstruman_adi):
       try:
        self.vtac()
        sql = "SELECT * FROM enstrumanlar WHERE `ENSTRÜMAN ADI` LIKE '%" + enstruman_adi + "%' ORDER BY ID DESC"
        self.cursor.execute(sql)
        veriler = self.cursor.fetchall()
        return veriler
       except Exception as e:
        print("Arama hatası:", e)
        return False
       finally:
        self.vtkapat()

    def musteri_arama(self, ad):
       try:
          self.vtac()
          sql = "SELECT * FROM musteri WHERE ad LIKE ? ORDER BY id DESC"
          self.cursor.execute(sql, ('%' + ad + '%',))
          veriler = self.cursor.fetchall()
          return veriler
       except Exception as e:
          print("Arama Hatası:", e)
          return False
       finally:
          self.vtkapat()
