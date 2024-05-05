import sys
import networkx as nx
import matplotlib.pyplot as plt
from PyQt5 import QtWidgets
from arayuz import Ui_Dialog as MainUi_Dialog
from ElemanEkle import Ui_Dialog as EkleUi_Dialog
from ElemanAra import Ui_Dialog as AraUi_Dialog
from ElemanSil import Ui_Dialog as SilUi_Dialog
from binaryTree import binary_Tree, Node

class ana_menu(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(ana_menu, self).__init__(parent)
        self.ui = MainUi_Dialog()
        self.ui.setupUi(self)
        self.agac = None
        # Butona tıklama olayı ekleme
        self.ui.pushButton_Olustur_2.clicked.connect(self.tablo_olusturma)
        self.ui.pushButton_ElemanEkle_5.clicked.connect(self.eleman_ekle)
        self.ui.pushButton_ElemanAra_5.clicked.connect(self.eleman_ara)
        self.ui.pushButton_ElemanSil_2.clicked.connect(self.eleman_sil)
    
    
    def tablo_olusturma(self):
        self.ui.Tablo.clear()  # Tabloyu temizle
        tablo_buyuklugu = self.ui.spinBox_tabloBuyuklukDegeri_2.value()
        self.agac = binary_Tree(tablo_buyuklugu)
        for i in range(tablo_buyuklugu):
            deger = QtWidgets.QTreeWidgetItem(self.ui.Tablo)
            deger.setText(0, str(i))  # Adres sütunu

    def eleman_ekle(self):
        dialog = QtWidgets.QDialog()
        ui = EkleUi_Dialog()
        ui.setupUi(dialog)
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            eleman = int(ui.Eleman_ekle.text())
            self.agac.elemanEkle(eleman)
            self.ui.Tablo.clear()
            tablo_buyuklugu = self.ui.spinBox_tabloBuyuklukDegeri_2.value()
            for i in range(tablo_buyuklugu):
                deger = QtWidgets.QTreeWidgetItem(self.ui.Tablo)
                deger.setText(0, str(i))  # Adres sütunu
                if(self.agac.liste[i] is not None):
                    deger.setText(1, str(self.agac.liste[i]))  # Adres sütunu
            print("Eklenen eleman:", eleman)
            

    def eleman_ara(self):
        dialog = QtWidgets.QDialog()
        ui = AraUi_Dialog()
        ui.setupUi(dialog)
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            eleman = int(ui.Eleman_ara.text())
            if(self.agac.elemanAra(eleman)):
                QtWidgets.QMessageBox.information(self, "Arama Sonucu", f"{eleman} elemanı tabloda bulunmaktadır.")
            else:
                QtWidgets.QMessageBox.warning(self, "Arama Sonucu", f"{eleman} elemanı tabloda bulunamadı!")

    def eleman_sil(self):
        dialog = QtWidgets.QDialog()
        ui = SilUi_Dialog()
        ui.setupUi(dialog)
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            eleman = int(ui.Eleman_sil.text())
            if self.agac.elemanSil(eleman):  # Eleman ağaçtan siliniyor
                QtWidgets.QMessageBox.information(self, "Silme İşlemi", f"{eleman} elemanı başarılı bir şekilde silindi.")
            else:
                QtWidgets.QMessageBox.warning(self, "Silme İşlemi", f"{eleman} elemanı tabloda bulunamadı, silinemedi.")
            
            self.ui.Tablo.clear()
            tablo_buyuklugu = self.ui.spinBox_tabloBuyuklukDegeri_2.value()
            
            for i in range(tablo_buyuklugu):
                deger = QtWidgets.QTreeWidgetItem(self.ui.Tablo)
                deger.setText(0, str(i))  # Adres sütunu
                if(self.agac.liste[i] is not None):
                    deger.setText(1, str(self.agac.liste[i]))  # Adres sütunu
                    
           

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ana_menu = ana_menu()
    ana_menu.show()
    sys.exit(app.exec_())
