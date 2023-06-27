import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton
from PyQt6.QtCore import Qt
import requests

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Валютный калькулятор')
        self.setGeometry(200, 200, 300, 200)

      
        widget = QWidget()
        layout = QVBoxLayout()
        widget.setLayout(layout)


        self.result_label = QLabel()
        layout.addWidget(self.result_label)


        self.amount_input = QLineEdit()
        layout.addWidget(self.amount_input)


        self.convert_button = QPushButton('Конвертировать')
        self.convert_button.clicked.connect(self.convert)
        layout.addWidget(self.convert_button)


        self.setCentralWidget(widget)

    def convert(self):
        amount = self.amount_input.text()
        if not amount:
            return

        data = {
            'amount': float(amount),
            'from': 'USD',
            'to': 'EUR'
        }

        response = requests.post('http://localhost:5000/convert', json=data)
        if response.status_code == 200:
            result = response.json()
            converted_amount = result['converted_amount']
            self.result_label.setText(f'Результат: {converted_amount}')
        else:
            self.result_label.setText('Ошибка при конвертации')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
