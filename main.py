from PyQt5.QtWidgets import QApplication
from PyQt5.uic import loadUi
import sys
import string
import random
import pyperclip #ця біліотека не встрояна її треба встановити щоб програма успішно запустилася

class Window:
    def __init__(self):
        self.start()
        self.isPasswordGenerate=False;

    def start(self):
        self.window=loadUi("window.ui")
        self.window.show()
        self.connect()

    def connect(self):
        self.window.btn.clicked.connect(self.generatePassword)
        self.window.btnCopy.clicked.connect(self.copy)

    def generatePassword(self):
        letters= string.ascii_letters if self.window.check2.isChecked() else ""
        numbers=string.digits if self.window.check1.isChecked() else ""
        characters = letters + numbers + string.punctuation
        password="".join(random.choice(characters) for i in range(self.window.lengthPassword.value()))
        self.window.label_result.setText(password)
        self.isPasswordGenerate=True

    def copy(self):
        if(self.isPasswordGenerate):
            pyperclip.copy(self.window.label_result.text())
            self.window.label_result.setText("Техт успішно скопійований")
            self.isPasswordGenerate=False


if __name__=="__main__":
    app=QApplication(sys.argv)
    window=Window()
    sys.exit(app.exec_())

