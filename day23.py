import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QTextEdit, QDialog, QMessageBox

class Mahasiswa:
    def __init__(self, nim, nama, jurusan):
        self.nim = nim
        self.nama = nama
        self.jurusan = jurusan

class DataMahasiswa(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Data Mahasiswa')
        self.setGeometry(100, 100, 400, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.label_title = QLabel('<h2>Data Mahasiswa</h2>')
        self.layout.addWidget(self.label_title)

        self.text_edit = QTextEdit()
        self.layout.addWidget(self.text_edit)

        self.button_tambah = QPushButton('Tambah Mahasiswa')
        self.button_tambah.clicked.connect(self.tambahMahasiswa)
        self.layout.addWidget(self.button_tambah)

        self.central_widget.setLayout(self.layout)

        self.daftar_mahasiswa = []

    def tambahMahasiswa(self):
        dialog = TambahMahasiswaDialog(self)
        if dialog.exec_():
            nim = dialog.nim_input.text()
            nama = dialog.nama_input.text()
            jurusan = dialog.jurusan_input.text()

            if self.validasiData(nim):
                QMessageBox.warning(self, 'Duplikasi NIM', 'Mahasiswa dengan NIM tersebut sudah terdaftar!')
            else:
                mahasiswa = Mahasiswa(nim, nama, jurusan)
                self.daftar_mahasiswa.append(mahasiswa)
                self.updateText()

    def validasiData(self, nim):
        for mahasiswa in self.daftar_mahasiswa:
            if mahasiswa.nim == nim:
                return True
        return False

    def updateText(self):
        text = "<h3>Daftar Mahasiswa:</h3>"
        for idx, mahasiswa in enumerate(self.daftar_mahasiswa, start=1):
            text += f"<b>Mahasiswa {idx}:</b><br>"
            text += f"NIM: {mahasiswa.nim}<br>"
            text += f"Nama: {mahasiswa.nama}<br>"
            text += f"Jurusan: {mahasiswa.jurusan}<br><br>"
        self.text_edit.setHtml(text)

class TambahMahasiswaDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle('Tambah Mahasiswa')
        self.setGeometry(200, 200, 300, 200)

        layout = QVBoxLayout()

        self.nim_label = QLabel('NIM:')
        self.nim_input = QLineEdit()
        layout.addWidget(self.nim_label)
        layout.addWidget(self.nim_input)

        self.nama_label = QLabel('Nama:')
        self.nama_input = QLineEdit()
        layout.addWidget(self.nama_label)
        layout.addWidget(self.nama_input)

        self.jurusan_label = QLabel('Jurusan:')
        self.jurusan_input = QLineEdit()
        layout.addWidget(self.jurusan_label)
        layout.addWidget(self.jurusan_input)

        self.button_tambah = QPushButton('Tambah')
        self.button_tambah.clicked.connect(self.accept)
        layout.addWidget(self.button_tambah)

        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DataMahasiswa()
    window.show()
    sys.exit(app.exec_())
