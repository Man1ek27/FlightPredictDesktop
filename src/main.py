import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt


class FlightDelayApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Predykcja opóźnień lotów")
        self.resize(400, 200)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        status_label = QLabel("Załadowano pomyślnie")
        status_label.setStyleSheet("font-size: 14px; font-weight: bold;")

        status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(status_label) 


def main():
    app = QApplication(sys.argv)
    window = FlightDelayApp()
    window.show()
    sys.exit(app.exec())



if __name__ == "__main__":
    main()