import time
import sys
import keyboard
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QPlainTextEdit, QFileDialog, QMenu


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Type Bot")

        menu_bar = self.menuBar()
        self.code_bar = menu_bar.addMenu("Code Snippets")
        self.code_bar.addAction('Getter', self.print_getter)
        self.code_bar.addAction('Setter', self.print_setter)
        self.code_bar.addAction('HaschCode', self.print_hashcode)

        self.input = QPlainTextEdit(self)

        self.button_open = QPushButton("Open File")
        self.button_open.clicked.connect(self.open_file)

        self.button_paste = QPushButton("Paste")
        self.button_paste.clicked.connect(self.paste)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.button_open)
        layout.addWidget(self.button_paste)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def paste(self):
        text = self.input.toPlainText()

        lines = text.splitlines()

        time.sleep(3)

        for line in lines:
            if line.__contains__("}"):
                keyboard.press("down")
            else:
                line_mod = line.strip(' ')
                keyboard.write(line_mod, exact=True)
                time.sleep(1)
        self.input.clear()

    def open_file(self):
        file_dialog = QFileDialog()
        file_name = file_dialog.getOpenFileName(self, 'Open file', '', '*.java')

        with open(file_name[0], encoding = 'utf-8') as java_file:
            self.input.clear()
            java_string = java_file.read()
            self.input.setPlainText(java_string)

    def print_getter(self):
        self.input.clear()
        self.input.setPlainText('''
        public Color getColor(){
            return color;
        }''')

    def print_setter(self):
        self.input.clear()
        self.input.setPlainText('''
        public void setColor(Color color){
            this.color = color;
        }''')

    def print_hashcode(self):
        self.input.clear()
        self.input.setPlainText('''
        @Override
        public int hashCode(){
            int hc = super.hashCode();
            final int mul = 31;
            hc = hc * mul + Objects.hash(color); 
            return hc;
        }''')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
