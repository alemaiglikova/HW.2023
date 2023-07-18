from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

class Contact:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class ContactsApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Contacts App")

        self.contacts = []

        self.setup_ui()

    def setup_ui(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.name_label = QLabel("Name:")
        self.name_input = QLineEdit()
        self.layout.addWidget(self.name_label)
        self.layout.addWidget(self.name_input)

        self.email_label = QLabel("Email:")
        self.email_input = QLineEdit()
        self.layout.addWidget(self.email_label)
        self.layout.addWidget(self.email_input)

        self.add_button = QPushButton("Add Contact")
        self.add_button.clicked.connect(self.add_contact)
        self.layout.addWidget(self.add_button)

    def add_contact(self):
        name = self.name_input.text()
        email = self.email_input.text()

        if name and email:
            contact = Contact(name, email)
            self.contacts.append(contact)
            self.show_message("Contact Added", "Contact has been added successfully.")
            self.clear_inputs()
        else:
            self.show_message("Error", "Please enter both name and email.")

    def show_message(self, title, message):
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec()

    def clear_inputs(self):
        self.name_input.clear()
        self.email_input.clear()

if __name__ == "__main__":
    app = QApplication([])
    window = ContactsApp()
    window.show()
    app.exec()
