from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 700)  # Pencere boyutunu genişlet
        Dialog.setSizeGripEnabled(True)  # Kullanıcının pencere boyutunu değiştirmesine izin ver
        Dialog.setWindowTitle("Dosya Organizasyonu - Binary Tree")
        self.mainLayout = QtWidgets.QVBoxLayout(Dialog)  # Ana layout
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        font = QtGui.QFont()
        font.setPointSize(20)  # Font boyutunu biraz küçült
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("QGroupBox { background-color: #f0f0f0; border: 1px solid gray; border-radius: 5px; margin-top: 1ex; }")  # Stil ekle

        # GroupBox için layout
        self.groupBoxLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.mainLayout.addWidget(self.groupBox)

        # Üst kısımdaki widget'lar için horizontal layout
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.TabloBuyuklugu_2 = QtWidgets.QLabel("Tablo Büyüklüğü", self.groupBox)
        self.TabloBuyuklugu_2.setFont(font)
        self.horizontalLayout.addWidget(self.TabloBuyuklugu_2)

        self.spinBox_tabloBuyuklukDegeri_2 = QtWidgets.QSpinBox(self.groupBox)
        self.horizontalLayout.addWidget(self.spinBox_tabloBuyuklukDegeri_2)
        
        self.pushButton_Olustur_2 = QtWidgets.QPushButton("Oluştur", self.groupBox)
        self.pushButton_Olustur_2.setFont(font)
        self.pushButton_Olustur_2.setStyleSheet("QPushButton { background-color: #aaddaa; }")  # Buton için stil
        self.horizontalLayout.addWidget(self.pushButton_Olustur_2)
        
        # Horizontal layout'u groupBox layout'una ekle
        self.groupBoxLayout.addLayout(self.horizontalLayout)

        # Butonlar için vertical layout
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.pushButton_ElemanEkle_5 = QtWidgets.QPushButton("Eleman Ekle", self.groupBox)
        self.pushButton_ElemanEkle_5.setFont(font)
        self.pushButton_ElemanEkle_5.setStyleSheet("QPushButton { background-color: #add8e6; }")  # Mavi tonu
        self.verticalLayout.addWidget(self.pushButton_ElemanEkle_5)

        self.pushButton_ElemanAra_5 = QtWidgets.QPushButton("Eleman Ara", self.groupBox)
        self.pushButton_ElemanAra_5.setFont(font)
        self.pushButton_ElemanAra_5.setStyleSheet("QPushButton { background-color: #ffa07a; }")  # Açık kırmızı tonu
        self.verticalLayout.addWidget(self.pushButton_ElemanAra_5)

        self.pushButton_ElemanSil_2 = QtWidgets.QPushButton("Eleman Sil", self.groupBox)
        self.pushButton_ElemanSil_2.setFont(font)
        self.pushButton_ElemanSil_2.setStyleSheet("QPushButton { background-color: #fa8072; }")  # Kırmızı tonu
        self.verticalLayout.addWidget(self.pushButton_ElemanSil_2)

        # Vertical layout'u groupBox layout'una ekle
        self.groupBoxLayout.addLayout(self.verticalLayout)

        # Ağaç widget'ı
        self.Tablo = QtWidgets.QTreeWidget(self.groupBox)
        self.Tablo.setHeaderLabels(["Adres", "Anahtar"])
        font.setPointSize(20)
        self.Tablo.setFont(font)
        self.Tablo.setStyleSheet("QTreeWidget { background-color: #ffffff; }")  # Arka plan rengi
        self.groupBoxLayout.addWidget(self.Tablo)

        Dialog.setLayout(self.mainLayout)

    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
