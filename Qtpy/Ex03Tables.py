from qtpy.QtWidgets import (QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem,
                            QPushButton, QMessageBox)

from mysql_database import MySqlDatabase


class DbForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MySQL DB Program")
        self.resize(400,400)

        self.layout = QVBoxLayout()

        self.mysql_table = QTableWidget()
        self.layout.addWidget(self.mysql_table)

        self.my_button = QPushButton("Get Records")
        self.my_button.clicked.connect(self.get_records)
        self.layout.addWidget(self.my_button)

        self.setLayout(self.layout)

    def get_records(self):
        try:
            db = MySqlDatabase()
            rows = db.get_all_users()
            self.mysql_table.setRowCount(len(rows))
            self.mysql_table.setColumnCount(4)
            self.mysql_table.setHorizontalHeaderLabels(['SlNo', 'UserName', 'Password',
                                                         'EmailAddress'])
            for row_index, row_data in enumerate(rows):
                for col_index, data in enumerate(row_data):
                    self.mysql_table.setItem(row_index, col_index, QTableWidgetItem(str(data)))
        except Exception as ex:
            QMessageBox.information(f"{ex}")

if __name__ == '__main__':
    app = QApplication([])

    form = DbForm()
    form.show()

    app.exec_()