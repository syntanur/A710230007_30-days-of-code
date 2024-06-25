import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton

class InfoWidget(QWidget):
    def init(self):
        super().init()

        self.setWindowTitle('Info Mahasiswa')
        self.setGeometry(100, 100, 300, 200)

        self.label_nama = QLabel('Nama:', self)
        self.label_nim = QLabel('NIM:', self)
        self.label_univ = QLabel('Universitas:', self)

        self.input_nama = QLineEdit(self)
        self.input_nim = QLineEdit(self)
        self.input_univ = QLineEdit(self)

        self.button_submit = QPushButton('Submit', self)
        self.button_submit.clicked.connect(self.submit_data)

        layout = QVBoxLayout()
        layout.addWidget(self.label_nama)
        layout.addWidget(self.input_nama)
        layout.addWidget(self.label_nim)
        layout.addWidget(self.input_nim)
        layout.addWidget(self.label_univ)
        layout.addWidget(self.input_univ)
        layout.addWidget(self.button_submit)

        self.setLayout(layout)

    def submit_data(self):
        nama = self.input_nama.text()
        nim = self.input_nim.text()
        universitas = self.input_univ.text()

        self.label_nama.setText(f'Nama: {nama}')
        self.label_nim.setText(f'NIM: {nim}')
        self.label_univ.setText(f'Universitas: {universitas}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = InfoWidget()
    window.show()
    sys.exit(app.exec_())