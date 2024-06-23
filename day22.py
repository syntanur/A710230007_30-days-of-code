import sys
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QLCDNumber
from PyQt5.QtGui import QFont


class Clock(QWidget):
    def init(self):
        super().init()

        self.setWindowTitle("Jam dunia")
        self.setGeometry(100, 100, 300, 200)

        # Membuat LCD Number untuk menampilkan jam
        self.lcd = QLCDNumber(self)
        self.lcd.setSegmentStyle(QLCDNumber.Flat)
        self.lcd.setDigitCount(8)
        self.lcd.setStyleSheet("background-color: black; color: white;")
        self.lcd.setFont(QFont("Arial", 18))

        # Membuat label untuk menampilkan tanggal dan zona waktu
        self.date_label = QLabel("Jum, 7 Jun", self)
        self.date_label.setStyleSheet("color: white;")
        self.date_label.setFont(QFont("Arial", 12))
        self.time_label = QLabel("Waktu Indonesia Barat", self)
        self.time_label.setStyleSheet("color: white;")
        self.time_label.setFont(QFont("Arial", 10))

        # Menata layout
        layout = QVBoxLayout()
        layout.addWidget(self.lcd)
        layout.addWidget(self.date_label)
        layout.addWidget(self.time_label)
        self.setLayout(layout)

        # Timer untuk memperbarui waktu setiap detik
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        self.update_time()

    def update_time(self):
        # Mendapatkan waktu saat ini
        current_time = QTime.currentTime()
        time_text = current_time.toString("hh:mm:ss")

        # Mengatur teks LCD Number dan label tanggal
        self.lcd.display(time_text)
        self.date_label.setText("Jum, 7 Jun")


if name == "main":
    app = QApplication(sys.argv)
    clock = Clock()
    clock.show()
    sys.exit(app.exec_())