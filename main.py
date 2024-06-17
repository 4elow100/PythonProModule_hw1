from datetime import datetime
import sys
from PySide6.QtWidgets import QMainWindow, QApplication
from application import gui_salary_app
from application.salary import calculate_salary


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = gui_salary_app.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.main_BTN.clicked.connect(self.get_salary)

    def get_salary(self):
        salary = calculate_salary(int(self.ui.id_employee_input.text()))
        self.ui.salary_label.setText(f'Ваша зарплата: {salary}р.')
        self.ui.time_label.setText(f'Актуально на: {datetime.now():%d-%m-%Y %H:%M:%S}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
