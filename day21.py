import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox

class BMICalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('BMI Calculator')
        self.initUI()

    def initUI(self):
        # Widgets
        self.label_height = QLabel('Height (cm):')
        self.label_weight = QLabel('Weight (kg):')
        self.input_height = QLineEdit()
        self.input_weight = QLineEdit()
        self.btn_calculate = QPushButton('Calculate BMI')
        self.label_result = QLabel('BMI Result:')

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label_height)
        layout.addWidget(self.input_height)
        layout.addWidget(self.label_weight)
        layout.addWidget(self.input_weight)
        layout.addWidget(self.btn_calculate)
        layout.addWidget(self.label_result)

        self.setLayout(layout)

        # Connect button to calculate function
        self.btn_calculate.clicked.connect(self.calculate_bmi)

    def calculate_bmi(self):
        height = float(self.input_height.text()) / 100  # Convert cm to meters
        weight = float(self.input_weight.text())

        if height <= 0 or weight <= 0:
            QMessageBox.critical(self, 'Input Error', 'Height and weight must be greater than zero.')
            return

        bmi = weight / (height * height)
        self.label_result.setText(f'BMI Result: {bmi:.2f}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BMICalculator()
    window.show()
    sys.exit(app.exec_())