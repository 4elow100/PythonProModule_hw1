# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui_salary_app.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(339, 170)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.main_BTN = QPushButton(self.centralwidget)
        self.main_BTN.setObjectName(u"main_BTN")
        self.main_BTN.setGeometry(QRect(130, 80, 75, 24))
        self.id_employee_input = QLineEdit(self.centralwidget)
        self.id_employee_input.setObjectName(u"id_employee_input")
        self.id_employee_input.setGeometry(QRect(180, 50, 113, 21))
        self.title = QLabel(self.centralwidget)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(0, 0, 341, 41))
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.title.setFont(font)
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_id = QLabel(self.centralwidget)
        self.title_id.setObjectName(u"title_id")
        self.title_id.setGeometry(QRect(40, 50, 131, 16))
        self.salary_label = QLabel(self.centralwidget)
        self.salary_label.setObjectName(u"salary_label")
        self.salary_label.setGeometry(QRect(-2, 110, 341, 20))
        self.salary_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time_label = QLabel(self.centralwidget)
        self.time_label.setObjectName(u"time_label")
        self.time_label.setGeometry(QRect(0, 140, 341, 20))
        self.time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.main_BTN.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0440\u0438\u0442\u044c", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"Salary checker", None))
        self.title_id.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 id \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430:", None))
        self.salary_label.setText("")
        self.time_label.setText("")
    # retranslateUi

