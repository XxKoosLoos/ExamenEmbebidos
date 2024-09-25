from PyQt6.QtWidgets import QApplication, QMainWindow, \
    QPushButton, QLabel, QLineEdit, QSpinBox, QDoubleSpinBox, \
    QComboBox, QHBoxLayout, QVBoxLayout, QWidget

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QPixmap
import sys
from pathlib import Path

def abs_path(nombre):
    return str(Path(__file__).parent.absolute() / nombre )

class Caja(QLabel):
    def __init__(self, color:str=""):
        super().__init__()
        self.setStyleSheet(f"Background-color:{color}")

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        
        
        self.Puerto = QComboBox()
        self.Puerto.addItems(["Puerto"])
        self.Puerto.currentTextChanged.connect(self.cambiar_texto)
        self.Puerto.currentIndexChanged.connect(self.cambiar_texto)

        self.Baudrate = QComboBox()
        self.Baudrate.addItems(["Baudrate"])
        self.Baudrate.currentTextChanged.connect(self.cambiar_texto)
        self.Baudrate.currentIndexChanged.connect(self.cambiar_texto)

        
        self.Bits_de_datos = QComboBox()
        self.Bits_de_datos.addItems(["Bits de datos"])
        self.Bits_de_datos.currentTextChanged.connect(self.cambiar_texto)
        self.Bits_de_datos.currentIndexChanged.connect(self.cambiar_texto)
        
        self.Bits_parada = QComboBox()
        self.Bits_parada.addItems(["Bits parada"])
        self.Bits_parada.currentTextChanged.connect(self.cambiar_texto)
        self.Bits_parada.currentIndexChanged.connect(self.cambiar_texto)
     
        self.Pariada = QComboBox()
        self.Pariada.addItems(["Pariada"])
        self.Pariada.currentTextChanged.connect(self.cambiar_texto)
        self.combo.currentIndexChanged.connect(self.cambiar_texto)


        botonrojo = Caja("red")
        botonamarillo = Caja("yellow")
        botonverde = Caja("green")








def main():
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()