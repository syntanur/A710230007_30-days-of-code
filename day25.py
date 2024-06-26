import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QPushButton, QLineEdit, QLabel


class VehicleListApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Daftar Kendaraan')

        # Layout utama menggunakan QVBoxLayout
        layout = QVBoxLayout()

        # ListWidget untuk menampilkan daftar kendaraan
        self.list_widget = QListWidget()
        layout.addWidget(self.list_widget)

        # Label dan LineEdit untuk input kendaraan baru
        add_layout = QHBoxLayout()
        add_layout.addWidget(QLabel('Kendaraan Baru:'))
        self.add_line_edit = QLineEdit()
        add_layout.addWidget(self.add_line_edit)

        # Button untuk menambahkan kendaraan baru
        add_button = QPushButton('Tambah')
        add_button.clicked.connect(self.add_vehicle)
        add_layout.addWidget(add_button)

        layout.addLayout(add_layout)

        self.setLayout(layout)
        self.show()

    def add_vehicle(self):
        # Ambil teks dari LineEdit
        new_vehicle = self.add_line_edit.text()

        # Tambahkan kendaraan ke ListWidget
        if new_vehicle:
            self.list_widget.addItem(new_vehicle)

        # Kosongkan LineEdit setelah menambahkan
        self.add_line_edit.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = VehicleListApp()
    sys.exit(app.exec_())
