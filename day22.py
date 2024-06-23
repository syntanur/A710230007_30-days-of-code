import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLCDNumber
from PyQt5.QtCore import QTimer, QTime
from PyQt5.QtGui import QFont  # Import QFont untuk mengatur jenis font

class DigitalClock(QWidget):
    def _init_(self):
        super()._init_()
        
        self.setWindowTitle('Digital Clock')
        self.setGeometry(200, 200, 300, 100)
        
        self.initUI()
        
    def initUI(self):
        self.lcd = QLCDNumber(self)
        self.lcd.setDigitCount(8)  # Menampilkan format HH:MM:SS
        self.lcd.resize(250, 100)
        
        # Mengatur jenis font menjadi Arial dengan ukuran 48
        font = QFont("Arial", 48, QFont.Bold)
        self.lcd.setFont(font)
        
        timer = QTimer(self)
        timer.timeout.connect(self.updateTime)
        timer.start(1000)  # Memperbarui setiap 1000 ms (1 detik)
        
        self.updateTime()  # Memastikan waktu ditampilkan saat aplikasi dimulai
        
    def updateTime(self):
        currentTime = QTime.currentTime()
        displayText = currentTime.toString('hh:mm:ss')
        self.lcd.display(displayText)

if __name__ == '_main_':
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())