# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ElemanSil.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(222, 104)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 201, 82))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.verticalLayoutWidget.setFont(font)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.Eleman_sil = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Eleman_sil.setFont(font)
        self.Eleman_sil.setObjectName("Eleman_sil")
        self.verticalLayout.addWidget(self.Eleman_sil)
        self.button_Eleman_sil = QtWidgets.QDialogButtonBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.button_Eleman_sil.setFont(font)
        self.button_Eleman_sil.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_Eleman_sil.setObjectName("button_Eleman_sil")
        self.verticalLayout.addWidget(self.button_Eleman_sil)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.Eleman_sil.returnPressed.connect(Dialog.accept)
        
        self.button_Eleman_sil.accepted.connect(Dialog.accept)  # OK button
        self.button_Eleman_sil.rejected.connect(Dialog.reject)  # Cancel button

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Silmek istediğiniz elemanı giriniz:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
