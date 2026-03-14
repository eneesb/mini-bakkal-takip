from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.vboxlayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.vboxlayout.setObjectName("vboxlayout")

        # ---------------- Ürün Ekle ----------------
        self.groupUrunEkle = QtWidgets.QGroupBox(self.centralwidget)
        self.groupUrunEkle.setTitle("Ürün Ekle")
        self.formLayout = QtWidgets.QFormLayout(self.groupUrunEkle)
        self.formLayout.setObjectName("formLayout")

        self.labelUrunAdi = QtWidgets.QLabel("Ürün Adı", self.groupUrunEkle)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelUrunAdi)
        self.lineUrunAdi = QtWidgets.QLineEdit(self.groupUrunEkle)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineUrunAdi)

        self.labelFiyat = QtWidgets.QLabel("Fiyat", self.groupUrunEkle)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelFiyat)
        self.spinFiyat = QtWidgets.QSpinBox(self.groupUrunEkle)
        self.spinFiyat.setMaximum(100000)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.spinFiyat)

        self.labelStok = QtWidgets.QLabel("Stok", self.groupUrunEkle)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.labelStok)
        self.spinStok = QtWidgets.QSpinBox(self.groupUrunEkle)
        self.spinStok.setMaximum(100000)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.spinStok)

        self.btnUrunEkle = QtWidgets.QPushButton("Ürün Ekle", self.groupUrunEkle)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.btnUrunEkle)

        self.vboxlayout.addWidget(self.groupUrunEkle)

        # ---------------- Ürünler Tablosu ----------------
        self.groupUrunler = QtWidgets.QGroupBox(self.centralwidget)
        self.groupUrunler.setTitle("Ürünler")
        self.vboxUrunler = QtWidgets.QVBoxLayout(self.groupUrunler)
        self.tableUrunler = QtWidgets.QTableWidget(self.groupUrunler)
        self.tableUrunler.setColumnCount(3)
        self.tableUrunler.setHorizontalHeaderLabels(["İsim", "Fiyat", "Stok"])
        self.vboxUrunler.addWidget(self.tableUrunler)
        self.vboxlayout.addWidget(self.groupUrunler)

        # ---------------- Satış Yap ----------------
        self.groupSatis = QtWidgets.QGroupBox(self.centralwidget)
        self.groupSatis.setTitle("Satış Yap")
        self.formSatis = QtWidgets.QFormLayout(self.groupSatis)

        self.labelSatisUrun = QtWidgets.QLabel("Ürün Adı")
        self.formSatis.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelSatisUrun)
        self.lineSatisUrun = QtWidgets.QLineEdit()
        self.formSatis.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineSatisUrun)

        self.labelSatisAdet = QtWidgets.QLabel("Adet")
        self.formSatis.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelSatisAdet)
        self.spinSatisAdet = QtWidgets.QSpinBox()
        self.spinSatisAdet.setMaximum(100000)
        self.formSatis.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.spinSatisAdet)

        self.btnSatisYap = QtWidgets.QPushButton("Satış Yap")
        self.formSatis.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.btnSatisYap)

        self.vboxlayout.addWidget(self.groupSatis)

        # ---------------- Rapor ----------------
        self.groupRapor = QtWidgets.QGroupBox(self.centralwidget)
        self.groupRapor.setTitle("Rapor")
        self.vboxRapor = QtWidgets.QVBoxLayout(self.groupRapor)
        self.labelGelir = QtWidgets.QLabel("Toplam Gelir: 0 TL")
        self.vboxRapor.addWidget(self.labelGelir)
        self.vboxlayout.addWidget(self.groupRapor)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Mini Bakkal Takip"))
