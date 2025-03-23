from PyQt5.QtWidgets import QMainWindow, QTabWidget
from .tabs import EquationTab, SystemTab


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Решение нелинейных уравнений и систем")
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        self.eq_tab = EquationTab()
        self.sys_tab = SystemTab()

        self.tabs.addTab(self.eq_tab, "Уравнения")
        self.tabs.addTab(self.sys_tab, "Системы")
