import cv2
import time
import sys
import os
import shutil
import cryptocode
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow,QMessageBox

path = 'img'
IDENTITY = len([f for f in os.listdir(path)
                if os.path.isfile(os.path.join(path, f))])

class MainWindow(QMainWindow):
    def setupUi(self, Other):
        Other.setObjectName("Other")
        Other.setFixedSize(221, 179)
        self.pushButton = QtWidgets.QPushButton(Other)
        self.pushButton.setGeometry(QtCore.QRect(20, 10, 181, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Other)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 90, 181, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Other)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 50, 181, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit = QtWidgets.QLineEdit(Other)
        self.lineEdit.setGeometry(QtCore.QRect(20, 130, 181, 31))
        self.lineEdit.setObjectName("lineEdit")

        self.pushButton.clicked.connect(self.cam)
        self.pushButton_2.clicked.connect(self.changePass)
        self.pushButton_3.clicked.connect(self.removeAll)

        self.retranslateUi(Other)
        QtCore.QMetaObject.connectSlotsByName(Other)

    def retranslateUi(self, Other):
        _translate = QtCore.QCoreApplication.translate
        Other.setWindowTitle(_translate("Other", "Other"))
        self.pushButton.setText(_translate("Other", "Добавить личность"))
        self.pushButton_2.setText(_translate("Other", "Изменить пароль"))
        self.pushButton_3.setText(_translate("Other", "Удалить все личности"))

    def cam(self):  # сохранение модели лица
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Press 'F' to add identity")
        msg.setInformativeText("This is additional information")
        msg.setWindowTitle("info")
        msg.setDetailedText("The details are as follows:")
        global IDENTITY
        # self.error_dialog = QtWidgets.QErrorMessage()
        # self.error_dialog.showMessage('Press 'F' to shoot!')
        face_cascade_db = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        cap = cv2.VideoCapture(0)
        a, img_save = cap.read()

        while True:
            success, img = cap.read()
            img = cv2.flip(img, 1)
            cv2.imshow('FaceID', img)
            try:
                img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_cascade_db.detectMultiScale(img_gray, 1.1, 19)

                for (x, y, w, h) in faces:  # обрезка лица с камеры
                    crop_img = img[y:y + h, x:x + w]
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            except:
                pass
            try:
                if cv2.waitKey(1) & 0xff == ord('f'):  # сохранение модели при нажжатии 'f'
                    cv2.imwrite(f'img/source{IDENTITY}.png', crop_img)
                    time.sleep(1)
                    IDENTITY = IDENTITY + 1
                    break
            except:
                pass
        cap.release()
        cv2.destroyAllWindows()

    def removeAll(self):
        path = os.path.join(os.path.dirname(os.path.abspath("__file__")), 'img')
        shutil.rmtree(path)
        os.mkdir('img')

    def changePass(self):
        passkey = 'denchik'
        password_raw = self.lineEdit.text()
        password = cryptocode.encrypt(password_raw, passkey)
        with open('pass', 'w') as f:
            f.writelines(password)

entering = 0
class Password(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Password")
        Dialog.setFixedSize(265, 350)
        Dialog.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(10, 80, 71, 51))
        self.pushButton.setStyleSheet("font: 14pt \"Terminal\";\n"
                                      "background-color: rgb(184, 184, 184);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 80, 71, 51))
        self.pushButton_2.setStyleSheet("font: 14pt \"Terminal\";\n"
                                        "background-color: rgb(184, 184, 184);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(190, 80, 71, 51))
        self.pushButton_3.setStyleSheet("font: 14pt \"Terminal\";\n"
                                        "background-color: rgb(184, 184, 184);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(190, 150, 71, 51))
        self.pushButton_6.setStyleSheet("font: 14pt \"Terminal\";\n"
                                        "background-color: rgb(184, 184, 184);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(100, 150, 71, 51))
        self.pushButton_5.setStyleSheet("font: 14pt \"Terminal\";\n"
                                        "background-color: rgb(184, 184, 184);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 150, 71, 51))
        self.pushButton_4.setStyleSheet("font: 14pt \"Terminal\";\n"
                                        "background-color: rgb(184, 184, 184);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_7 = QtWidgets.QPushButton(Dialog)
        self.pushButton_7.setGeometry(QtCore.QRect(190, 220, 71, 51))
        self.pushButton_7.setStyleSheet("font: 14pt \"Terminal\";\n"
                                        "background-color: rgb(184, 184, 184);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(Dialog)
        self.pushButton_8.setGeometry(QtCore.QRect(100, 220, 71, 51))
        self.pushButton_8.setStyleSheet("font: 14pt \"Terminal\";\n"
                                        "background-color: rgb(184, 184, 184);")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_0 = QtWidgets.QPushButton(Dialog)
        self.pushButton_0.setGeometry(QtCore.QRect(100, 290, 71, 51))
        self.pushButton_0.setStyleSheet("font: 14pt \"Terminal\";\n"
                                        "background-color: rgb(184, 184, 184);")
        self.pushButton_0.setObjectName("pushButton_0")
        self.pushButton_9 = QtWidgets.QPushButton(Dialog)
        self.pushButton_9.setGeometry(QtCore.QRect(10, 220, 71, 51))
        self.pushButton_9.setMinimumSize(QtCore.QSize(0, 51))
        self.pushButton_enter = QtWidgets.QPushButton(Dialog)
        self.pushButton_enter.setGeometry(QtCore.QRect(190, 290, 71, 51))
        self.pushButton_enter.setStyleSheet("font: 14pt \"Terminal\";\n"
                                            "background-color: rgb(184, 184, 184);")
        self.pushButton_enter.setObjectName("pushButton_enter")
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("font: 14pt \"Terminal\";\n"
                                        "background-color: rgb(184, 184, 184);")
        self.pushButton_9.setObjectName("pushButton_9")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 20, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.pushButton.clicked.connect(self.one)
        self.pushButton_2.clicked.connect(self.two)
        self.pushButton_3.clicked.connect(self.three)
        self.pushButton_4.clicked.connect(self.four)
        self.pushButton_5.clicked.connect(self.five)
        self.pushButton_6.clicked.connect(self.six)
        self.pushButton_7.clicked.connect(self.seven)
        self.pushButton_8.clicked.connect(self.eight)
        self.pushButton_9.clicked.connect(self.nine)
        self.pushButton_0.clicked.connect(self.ou)
        self.pushButton_enter.clicked.connect(self.enter)
        self.pas = ""

    def one(self):
        self.pas = self.pas + '1'
        self.label.setText(self.pas)

    def two(self):
        self.pas = self.pas + '2'
        self.label.setText(self.pas)

    def three(self):
        self.pas = self.pas + '3'
        self.label.setText(self.pas)

    def four(self):
        self.pas = self.pas + '4'
        self.label.setText(self.pas)

    def five(self):
        self.pas = self.pas + '5'
        self.label.setText(self.pas)

    def six(self):
        self.pas = self.pas + '6'
        self.label.setText(self.pas)

    def seven(self):
        self.pas = self.pas + '7'
        self.label.setText(self.pas)

    def eight(self):
        self.pas = self.pas + '8'
        self.label.setText(self.pas)

    def nine(self):
        self.pas = self.pas + '9'
        self.label.setText(self.pas)

    def ou(self):
        self.pas = self.pas + '0'
        self.label.setText(self.pas)

    def enter(self):

        passkey = 'denchik'
        with open('pass', 'r') as f:
            password_raw = f.readlines()
        password = cryptocode.decrypt(''.join(password_raw), passkey)

        if self.pas == password:
            global entering
            entering = 1
            global Dialoger
            global uir
            Dialoger = QtWidgets.QDialog()
            uir = MainWindow()
            uir.setupUi(Dialoger)
            Dialoger.show()

            #menu()
            #pass
            self.label.setText("Correct!")
        else:
            self.label.setText("Incorrect!")
        self.pas = ''

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "1"))
        self.pushButton_2.setText(_translate("Dialog", "2"))
        self.pushButton_3.setText(_translate("Dialog", "3"))
        self.pushButton_4.setText(_translate("Dialog", "4"))
        self.pushButton_5.setText(_translate("Dialog", "5"))
        self.pushButton_6.setText(_translate("Dialog", "6"))
        self.pushButton_7.setText(_translate("Dialog", "7"))
        self.pushButton_8.setText(_translate("Dialog", "8"))
        self.pushButton_9.setText(_translate("Dialog", "9"))
        self.pushButton_0.setText(_translate("Dialog", "0"))
        self.pushButton_enter.setText(_translate("Dialog", "ENTER"))
        self.label.setText(_translate("Dialog", "Input password"))


def check_pass():
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Password()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

check_pass()