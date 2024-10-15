# QTpy is an abstraction for developing Desktop based Applications in Python.
# It internally does API calls to libraries like PyQT or PySide which are the 2 bindings for
# Qt Framework.
# Primarily used for providing platform-independent GUIs that shall run on desktops. It also
# provides tools for networking, SQL databases OpenGL and many GUI based libraries.
# Contains classes and Widgets (ready to use UI components) that can created using python and
# build the Front End Applications that run directly on the OS.
# It is compatible with Windows, Linux, MacOs and Andriod.
# All U need is to download the packages and use them to create components and execute them as
# python applications.
# The implementors or bindings are done using libraries like PyQT5, PyQT6. U must install both
# the qtpy and any of the bindings.
# import qtpy
# import PyQt5
# All UI components are classes that are used for developing the UI for the App
from PyQt5.QtWidgets import QFormLayout, QLabel, QLineEdit, QPushButton
from qtpy.QtWidgets import  QApplication, QWidget, QMessageBox

class SampleForm(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QFormLayout()

        #Field for Name:
        self.name_label = QLabel("Name")
        self.name_input = QLineEdit()
        self.layout.addRow(self.name_label, self.name_input)

        #Field for address:
        self.addr_label = QLabel("Address")
        self.addr_input = QLineEdit()
        self.layout.addRow(self.addr_label, self.addr_input)

        # Creating Buttons:
        self.submit_button = QPushButton('Submit')
        self.submit_button.clicked.connect(self.on_click)
        self.layout.addRow(self.submit_button)

        self.setLayout(self.layout)
        self.setWindowTitle("Sample form for UI")

    def on_click(self):
        name = self.name_input.text()
        addr = self.addr_input.text()

        msg_box = QMessageBox()
        msg_box.setText(f"Name: {name} from {addr}")
        msg_box.exec_()

if __name__ == '__main__':
    app = QApplication([])

    form = SampleForm()
    form.show()

    app.exec_()

