from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from display.models import Message

class SmartSpeakerWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Умная колонка с дисплеем")
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()

        messages = Message.objects.all()
        for message in messages:
            label = QLabel(message.content)
            layout.addWidget(label)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

if __name__ == "__main__":
    app = QApplication([])
    window = SmartSpeakerWindow()
    window.show()
    app.exec()
