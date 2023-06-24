import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QGridLayout, QPushButton


class ScientificCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Scientific Calculator")
        self.setWindowIcon(QIcon("calculator_icon.png"))  # Replace with your own icon
        self.setStyleSheet("background-color: #202020; color: white;")
        self.setup_ui()

    def setup_ui(self):
        main_layout = QVBoxLayout()

        self.input_line = QLineEdit()
        self.input_line.setAlignment(Qt.AlignRight)
        self.input_line.setReadOnly(True)
        self.input_line.setStyleSheet(
            "background-color: #303030; color: white; border: none; padding: 10px;"
        )
        self.input_line.setFont(QFont("Arial", 16))
        main_layout.addWidget(self.input_line)

        buttons_layout = QGridLayout()

        # Define the buttons for the calculator
        buttons = [
            '7', '8', '9', '/', 'C',
            '4', '5', '6', '*', '(',
            '1', '2', '3', '-', ')',
            '0', '.', '=', '+', '√',
            'sin', 'cos', 'tan', 'π', '^'
        ]

        # Add buttons to the layout
        row, col = 1, 0
        for button_text in buttons:
            button = QPushButton(button_text)
            button.setFixedSize(60, 60)
            button.setStyleSheet(
                "background-color: #505050; color: white; border: none; font-size: 18px;"
            )
            buttons_layout.addWidget(button, row, col)
            col += 1
            if col > 4:
                col = 0
                row += 1

        main_layout.addLayout(buttons_layout)
        self.setLayout(main_layout)

        # Connect button signals to slots
        for i in range(buttons_layout.count()):
            button = buttons_layout.itemAt(i).widget()
            button.clicked.connect(self.button_clicked)

    def button_clicked(self):
        button = self.sender()
        text = button.text()

        if text == '=':
            try:
                result = eval(self.input_line.text())
                self.input_line.setText(str(result))
            except Exception as e:
                self.input_line.setText("Error")
        elif text == 'C':
            self.input_line.clear()
        elif text == '√':
            try:
                result = eval(self.input_line.text())
                self.input_line.setText(str(result ** 0.5))
            except Exception as e:
                self.input_line.setText("Error")
        else:
            current_text = self.input_line.text()
            new_text = current_text + text
            self.input_line.setText(new_text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = ScientificCalculator()
    calculator.show()
    sys.exit(app.exec_())
