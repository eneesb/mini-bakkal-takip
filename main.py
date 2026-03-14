import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox
from bakkal_ui import Ui_MainWindow
from pymongo import MongoClient

# ---------------- MONGODB BAĞLANTISI ----------------
client = MongoClient("mongodb://localhost:27017/")
db = client["bakkal"]
collection = db["urunler"]

# ---------------- ANA PENCERE SINIFI ----------------
class BakkalApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Buton bağlantıları
        self.ui.btnUrunEkle.clicked.connect(self.urun_ekle)
        self.ui.btnSatisYap.clicked.connect(self.satis_yap)

        # Toplam geliri başlat
        self.toplam_gelir = 0

        # Table widget'ı MongoDB verileri ile doldur
        self.tabloyu_guncelle()

    # ---------------- ÜRÜN EKLEME ----------------
    def urun_ekle(self):
        isim = self.ui.lineUrunAdi.text().strip().lower()
        fiyat = self.ui.spinFiyat.value()
        stok = self.ui.spinStok.value()

        if not isim:
            QMessageBox.warning(self, "Hata", "Ürün adı boş olamaz!")
            return
        

        urun = collection.find_one({"isim": isim})
        if urun:
            # Stok güncelle
            collection.update_one({"isim": isim}, {"$inc": {"stok": stok}})
            # Güncel stok miktarını tekrar çek
            urun = collection.find_one({"isim": isim})
            QMessageBox.information(self, "Stok Güncellendi",
                                    f"'{isim}' stoku arttırıldı. Yeni stok: {urun['stok']}")
        else:
            # Yeni ürün ekle
            collection.insert_one({"isim": isim, "fiyat": fiyat, "stok": stok})
            QMessageBox.information(self, "Ürün Eklendi",
                                    f"'{isim}' başarıyla eklendi. Stok: {stok} | Fiyat: {fiyat}")

        self.tabloyu_guncelle()

    # ---------------- TABLOYU GÜNCELLE ----------------
    def tabloyu_guncelle(self):
        urunler = list(collection.find())
        self.ui.tableUrunler.setRowCount(len(urunler))
        for row, urun in enumerate(urunler):
            self.ui.tableUrunler.setItem(row, 0, QTableWidgetItem(urun["isim"]))
            self.ui.tableUrunler.setItem(row, 1, QTableWidgetItem(str(urun["fiyat"])))
            self.ui.tableUrunler.setItem(row, 2, QTableWidgetItem(str(urun["stok"])))

    # ---------------- SATIŞ YAP ----------------
    def satis_yap(self):
        isim = self.ui.lineSatisUrun.text().strip().lower()
        adet = self.ui.spinSatisAdet.value()

        urun = collection.find_one({"isim": isim})
        if not urun:
            QMessageBox.warning(self, "Hata", "Ürün bulunamadı!")
            return

        if adet <= 0:
            QMessageBox.warning(self, "Hata", "Satılan adet pozitif olmalıdır!")
            return

        if urun["stok"] >= adet:
            # Stok azalt ve gelir hesapla
            collection.update_one({"isim": isim}, {"$inc": {"stok": -adet}})
            # Güncel stok ve fiyatı tekrar çek
            urun = collection.find_one({"isim": isim})
            satıs_geliri = urun["fiyat"] * adet
            self.toplam_gelir += satıs_geliri
            QMessageBox.information(self, "Satış Yapıldı",
                                    f"{adet} adet '{isim}' satıldı.\nBu satıştan gelir: {satıs_geliri} TL")
            self.ui.labelGelir.setText(f"Toplam Gelir: {self.toplam_gelir} TL")
            self.tabloyu_guncelle()
        else:
            QMessageBox.warning(self, "Hata", f"Yeterli stok yok! Güncel stok: {urun['stok']}")

# ---------------- UYGULAMA BAŞLAT ----------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BakkalApp()
    window.show()
    sys.exit(app.exec_())
