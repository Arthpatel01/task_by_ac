import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QVBoxLayout, QComboBox, QCheckBox, QTableWidget, \
    QTableWidgetItem, QRadioButton, QTabWidget, QPushButton, QComboBox, QMessageBox, QWidget


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt Application")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QTabWidget(self)

        # Combo box with checkbox
        combo_checkbox_tab = QWidget()
        combo_layout = QVBoxLayout()
        self.central_widget.addTab(combo_checkbox_tab, "Combo Box with Checkbox")
        combo_checkbox = QComboBox()
        combo_checkbox.setEditable(False)
        combo_checkbox.setMaxCount(5)
        combo_checkbox.addItems(["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"])
        combo_checkbox_tab.setLayout(combo_layout)
        combo_layout.addWidget(combo_checkbox)
        combo_layout.addWidget(QCheckBox("Select All"))

        # table with radio buttons
        table_radio_tab = QWidget()
        table_layout = QVBoxLayout()
        self.central_widget.addTab(table_radio_tab, "Table with Radio Buttons")
        table_widget = QTableWidget()
        table_widget.setColumnCount(2)
        table_widget.setRowCount(5)
        for row in range(5):
            item = QTableWidgetItem(f"Row {row}")
            table_widget.setItem(row, 0, item)
            radio_button = QRadioButton()
            table_widget.setCellWidget(row, 1, radio_button)
        table_radio_tab.setLayout(table_layout)
        table_layout.addWidget(table_widget)

        # table with combo boxes
        table_combo_tab = QWidget()
        combo_table_layout = QVBoxLayout()
        self.central_widget.addTab(table_combo_tab, "Table with Combo Boxes")
        combo_table_widget = QTableWidget()
        combo_table_widget.setColumnCount(2)
        combo_table_widget.setRowCount(5)
        for row in range(5):
            item = QTableWidgetItem(f"Row {row}")
            combo_table_widget.setItem(row, 0, item)
            combo_box = QComboBox()
            combo_box.addItems(["Option 1", "Option 2", "Option 3"])
            combo_table_widget.setCellWidget(row, 1, combo_box)
        table_combo_tab.setLayout(combo_table_layout)
        combo_table_layout.addWidget(combo_table_widget)

        # pushbutton
        pushbutton_tab = QWidget()
        pushbutton_layout = QVBoxLayout()
        self.central_widget.addTab(pushbutton_tab, "Pushbutton")
        pushbutton = QPushButton("Click Me")
        pushbutton_layout.addWidget(pushbutton)
        pushbutton_tab.setLayout(pushbutton_layout)
        pushbutton.clicked.connect(self.show_message)

        self.setCentralWidget(self.central_widget)

    def show_message(self):
        QMessageBox.information(self, "Message", "Button Clicked!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
