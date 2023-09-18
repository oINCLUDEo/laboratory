import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

class RegistrationWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setWindowTitle("Окно регистрации")
        self.setGeometry(100, 100, 400, 200)

        self.label_username = QLabel("Введите логин:")
        self.username_input = QLineEdit()
        layout.addWidget(self.label_username)
        layout.addWidget(self.username_input)

        self.label_password = QLabel("Введите пароль:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.label_password)
        layout.addWidget(self.password_input)

        self.register_button = QPushButton("Зарегистрироваться")
        self.register_button.clicked.connect(self.register)
        layout.addWidget(self.register_button)

        self.setLayout(layout)

    def register(self):
        username = self.username_input.text()
        password = self.password_input.text()

        QMessageBox.information(self, "Регистрация успешна", "Пользователь " + str(username) + " успешно "
                                                                                               "зарегистрирован!")
        self.username_input.clear()
        self.password_input.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RegistrationWindow()
    window.show()
    sys.exit(app.exec_())
