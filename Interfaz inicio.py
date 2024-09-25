from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, \
    QPushButton, QLabel, QLineEdit, QComboBox, QHBoxLayout, QVBoxLayout, QGridLayout, QSizePolicy
from PyQt6 import QtGui
from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtGui import QIcon
import sys
from pathlib import Path

# Función para obtener el camino absoluto/la ruta del archivo
def abs_path(nombre):
    return str(Path(__file__).parent.absolute() / nombre)

# Clase caja_texto heredada de QLineEdit
class caja_texto(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setStyleSheet(
            f"""Border: 1px solid green;
            border-radius:1px;
            background-color:#bae3f6;
            color: black;  /* Establecer el color del texto en negro */
            font-family: Arial;  /* Establecer la fuente como Arial */
            """)

# Clase Caja heredada de QLabel
class Caja(QLabel):
    def __init__(self, color: str = ""):
        super().__init__()
        self.setStyleSheet(
            f"""Border: 1px solid green;
            background-color:#ebeff1;
            """)

# Clase Ventana heredada de QMainWindow
class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Primera Evaluación")
        
        # Aquí establecemos el icono de la ventana
        self.setWindowIcon(QIcon(abs_path("imagen.ico")))  # Asegúrate de tener el archivo .ico

        caja_de_texto = caja_texto()
        caja = Caja("#CFD1D4")

        # Inicializar los ComboBox
        self.combo = QComboBox()
        self.combo.addItems(["Puerto", "Opción 1", "Opción 2", "Opción 3"])
        self.combo2 = QComboBox()
        self.combo2.addItems(["Baudrate", "Opción 1", "Opción 2", "Opción 3"])
        self.combo3 = QComboBox()
        self.combo3.addItems(["Bits de datos", "Opción 1", "Opción 2", "Opción 3"])
        self.combo4 = QComboBox()
        self.combo4.addItems(["Bits parada", "Opción 1", "Opción 2", "Opción 3"])
        self.combo5 = QComboBox()
        self.combo5.addItems(["Paridad", "Opción 1", "Opción 2", "Opción 3"])

        self.layout_general = QGridLayout()
        layout_superior = QHBoxLayout()
        self.layout_superior_der = QGridLayout()
        layout_inferior = QGridLayout()

        layout_izq = QGridLayout()
        layout_der = QGridLayout()
        layout_renglon1 = QHBoxLayout()
        layout_renglon2 = QHBoxLayout()
        layout_renglon3 = QHBoxLayout()
        layout_renglon4 = QHBoxLayout()
        layout_renglon5 = QGridLayout()

        layout_izq.setVerticalSpacing(15)
        layout_der.setVerticalSpacing(5)

        # Establecer márgenes para evitar que los elementos se desplacen al redimensionar
        self.layout_general.setContentsMargins(10, 10, 10, 10)  # Márgenes generales para el layout principal
        layout_superior.setContentsMargins(5, 5, 5, 5)  # Márgenes para el layout superior
        layout_izq.setContentsMargins(5, 5, 5, 5)  # Márgenes para el layout izquierdo
        layout_der.setContentsMargins(5, 5, 5, 5)  # Márgenes para el layout derecho
        layout_renglon1.setContentsMargins(5, 5, 5, 5)  # Márgenes para el primer renglón
        layout_renglon2.setContentsMargins(5, 5, 5, 5)  # Márgenes para el segundo renglón
        layout_renglon3.setContentsMargins(5, 5, 5, 5)  # Márgenes para el tercer renglón
        layout_renglon4.setContentsMargins(5, 5, 5, 5)  # Márgenes para el cuarto renglón
        layout_renglon5.setContentsMargins(5, 5, 5, 5)  # Márgenes para el quinto renglón

        # Crear etiquetas con estilo
        self.etiqueta_rojo = QLabel()
        self.etiqueta_rojo.setStyleSheet(
            f"""Border: 1px solid blue;
            border-radius:32px;
            background-color:red;
            """)
        self.etiqueta_rojo.setFixedSize(64, 64)

        self.etiqueta_amarillo = QLabel()
        self.etiqueta_amarillo.setStyleSheet(
            f"""Border: 1px solid yellow;
            border-radius:32px;
            background-color:#DCBF11;
            """)
        self.etiqueta_amarillo.setFixedSize(64, 64)

        self.etiqueta_verde = QLabel()
        self.etiqueta_verde.setStyleSheet(
            f"""Border: 1px solid #008000;
            border-radius:32px;
            background-color:#18F478;
            """)
        self.etiqueta_verde.setFixedSize(64, 64)

        boton_enviar = QPushButton("Enviar")
        self.boton_Conectar = QPushButton("Conectar")
        self.boton_Conectar.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)  # Permite que el botón ajuste su tamaño

        # Agregar layouts a la estructura general
        self.layout_general.addLayout(self.layout_superior_der, 0, 0)
        self.layout_general.addLayout(layout_superior, 1, 0)
        self.layout_general.addLayout(layout_inferior, 2, 0)
        layout_superior.addLayout(layout_izq)
        layout_superior.addLayout(layout_der)
        layout_der.addLayout(layout_renglon1, 0, 0)
        layout_der.addLayout(layout_renglon2, 1, 0)
        layout_der.addLayout(layout_renglon3, 2, 0)
        layout_der.addLayout(layout_renglon4, 3, 0)
        layout_der.addLayout(layout_renglon5, 4, 0)

        # Añadir etiquetas al layout izquierdo
        layout_izq.addWidget(self.etiqueta_rojo, 1, 1, 1, 1)
        layout_izq.addWidget(self.etiqueta_amarillo, 2, 1, 1, 1)
        layout_izq.addWidget(self.etiqueta_verde, 3, 1, 1, 1)

        # Añadir texto y comboboxes a los layouts correspondientes
        texto = QLabel("Monitor")
        layout_renglon1.addWidget(texto)
        texto.setStyleSheet("qproperty-alignment: AlignCenter")
        layout_renglon2.addWidget(self.combo)
        layout_renglon2.addWidget(self.combo2)
        layout_renglon3.addWidget(self.combo3)
        layout_renglon3.addWidget(self.combo4)
        layout_renglon3.addWidget(self.combo5)
        layout_renglon4.addWidget(caja_de_texto)
        layout_renglon4.addWidget(boton_enviar)
        layout_renglon5.addWidget(caja, 0, 10, 10, 10)

        layout_inferior.addWidget(self.boton_Conectar, 0, 0, 1, 1)

        # Establecer tamaños fijos para los QComboBox y el botón
        for combo in [self.combo, self.combo2, self.combo3, self.combo4, self.combo5]:
            combo.setFixedSize(100, 30)  # Tamaño fijo para los QComboBox

        boton_enviar.setFixedSize(80, 30)  # Tamaño fijo para el botón "Enviar"
        self.boton_Conectar.setFixedSize(100, 30)  # Tamaño fijo para el botón "Conectar"

        widget = QWidget()
        widget.setLayout(self.layout_general)
        self.setCentralWidget(widget)
        self.setFixedSize(460, 310)

        # Crear etiqueta para el mensaje de conexión y establecer geometría (posición en la esquina superior derecha)
        self.mensaje_conexion = QLabel("", self)
        self.mensaje_conexion.setFixedSize(150, 20)  # Tamaño fijo para que no cambie
        self.mensaje_conexion.setStyleSheet("color: green; font-weight: bold;")
        self.mensaje_conexion.setGeometry(self.width() - 160, 10, 150, 20)  # Posición fija en la esquina superior derecha
        self.mensaje_conexion.setAlignment(Qt.AlignmentFlag.AlignRight)  # Alinear el texto a la derecha

        # Conectar el botón de conectar con la función de cambio de estado
        self.boton_Conectar.clicked.connect(self.manejar_conexion)

        # Estado de conexión
        self.conectado = False

    # Método para alternar entre conectar y desconectar
    def manejar_conexion(self):
        if not self.conectado:
            self.boton_Conectar.setText("Desconectar")
            self.boton_Conectar.adjustSize()  # Ajusta el tamaño del botón al texto
            self.mostrar_mensaje_conexion("Se ha conectado con éxito", "green")  # Cambiar el mensaje aquí
            self.conectado = True
        else:
            self.boton_Conectar.setText("Conectar")
            self.boton_Conectar.adjustSize()  # Ajusta el tamaño del botón al texto
            self.conectado = False

    # Método para mostrar el mensaje de conexión
    def mostrar_mensaje_conexion(self, mensaje, color):
        # Mostrar mensaje de "Conectado" con el color especificado
        self.mensaje_conexion.setText(mensaje)
        self.mensaje_conexion.setStyleSheet(f"color: {color}; font-weight: bold;")
        
        # Temporizador para ocultar el mensaje después de 2 segundos
        QTimer.singleShot(2000, self.ocultar_mensaje_conexion)

    # Método para ocultar el mensaje de conexión
    def ocultar_mensaje_conexion(self):
        self.mensaje_conexion.setText("")  # Vaciar el texto para ocultar

def main():
    app = QApplication(sys.argv)
    
    # Aquí se asigna el icono a toda la aplicación
    app.setWindowIcon(QIcon(abs_path('imagen.ico')))  # Cambia esto si es otro archivo de icono
    
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
