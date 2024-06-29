import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QCalendarWidget, QLabel


class CalendarWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Kalender')
        self.setGeometry(100, 100, 400, 300)

        # Membuat layout utama menggunakan QVBoxLayout
        layout = QVBoxLayout()

        # Membuat widget kalender
        self.calendar = QCalendarWidget(self)
        self.calendar.setMinimumDate(self.calendar.minimumDate().addYears(-1))  # Batasan tanggal minimal
        self.calendar.setMaximumDate(self.calendar.maximumDate().addYears(1))  # Batasan tanggal maksimal
        self.calendar.setGridVisible(True)  # Menampilkan garis grid pada kalender
        self.calendar.clicked.connect(self.show_selected_date)  # Menghubungkan klik tanggal dengan fungsi show_selected_date

        # Menambahkan widget kalender ke dalam layout
        layout.addWidget(self.calendar)

        # Label untuk menampilkan tanggal yang dipilih
        self.date_label = QLabel(self)
        layout.addWidget(self.date_label)

        # Mengatur layout utama pada window
        self.setLayout(layout)

    def show_selected_date(self):
        # Mendapatkan tanggal yang dipilih dari kalender
        selected_date = self.calendar.selectedDate()
        # Menampilkan tanggal yang dipilih pada label
        self.date_label.setText(f'Tanggal dipilih: {selected_date.toString("dd-MM-yyyy")}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CalendarWidget()
    ex.show()
    sys.exit(app.exec_())

