import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.uic import loadUi


class CoffeeInfoApp(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('main.ui', self)

        self.initDB()

        self.loadTableData()

    def initDB(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('coffee.sqlite')

    def loadTableData(self):
        model = QSqlTableModel()
        model.setTable('coffees')
        model.select()

        self.tableView.setModel(model)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CoffeeInfoApp()
    window.show()
    sys.exit(app.exec())
