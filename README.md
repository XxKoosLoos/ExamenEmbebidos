# ExamenEmbebidos

Prototipo académico colaborativo con una interfaz de escritorio en Python/PyQt6 y firmware Arduino C++ para un semáforo de LEDs.

## Alcance verificable

- `Interfaz inicio.py`: interfaz con indicadores, opciones de configuración y botones.
- `Examen_leds/Examen_leds.ino`: secuencia de LEDs, botones de pausa y arranque, y salida serie a 9600 baudios.
- `imagen.ico`: recurso gráfico.
- `venv/`: entorno virtual original de Windows incluido en Git.

La interfaz y el firmware no están integrados mediante comunicación serie en el código revisado. «Conectar» solo cambia el estado visual y muestra un mensaje; «Enviar» no tiene una acción asociada. Los indicadores no reciben datos del dispositivo. No se acredita una conexión funcional ni una prueba de hardware.

## Instalación y ejecución propuestas

Las instrucciones siguientes no fueron probadas. Se necesita Python, una sesión gráfica compatible con PyQt6 y una copia completa del repositorio.

Crear un entorno nuevo:

```bash
python -m venv .venv
```

Activarlo en PowerShell con `.\.venv\Scripts\Activate.ps1`, o en Linux/macOS con `source .venv/bin/activate`. Después:

```bash
python -m pip install PyQt6
python "Interfaz inicio.py"
```

El entorno original registra Python 3.12.5 y contiene metadatos de PyQt6 6.7.1 y pyserial 3.5. Estas versiones son evidencia del entorno incluido; no constituyen requisitos mínimos ni una matriz de compatibilidad validada. La interfaz revisada no utiliza pyserial.

## Firmware y montaje pendiente de confirmar

El código asigna LEDs a los GPIO 16, 2, 15 y 18; arranque a GPIO35 y paro a GPIO14. Antes de cargarlo deben confirmarse modelo de placa, niveles eléctricos, resistencias y esquema. No se incluye una configuración reproducible de compilación. Los botones utilizan `INPUT`; no debe asumirse que el código habilita resistencias pull-up. En un ESP32 clásico, GPIO35 no dispone de pull-up interno.

## Limitaciones conocidas por lectura del código

- El contador amarillo cuenta encendidos hasta cuatro, aunque los comentarios describen dos parpadeos.
- La lógica de parpadeo continúa durante `waitingForPause`, por lo que requiere revisar la pausa prevista.
- No hay antirrebote explícito.
- La reanudación reinicia `previousMillis` y no conserva el tiempo restante.
- La ventana tiene tamaño fijo.
- No se identificaron pruebas propias ni CI; no se ejecutó ni compiló el proyecto durante la auditoría.

Estos puntos son hallazgos pendientes de corrección y validación, no reparaciones ya realizadas.

## Integrantes

Se conserva la atribución del README original:

- Concha Reyes Cristian Antonio
- Acosta Hernandes Jesus Eduardo
- Gonzalez Valencia Hostyn Axel
- Reyes Lemus Miguel Angel
- Molina Vargas Alexis Adair
- Laguna Aburto Alma

Las contribuciones individuales deben confirmarse con el equipo. Los commits de una cuenta no demuestran autoría exclusiva. No se ha establecido una licencia de redistribución en esta revisión.

## Evidencia histórica

Los diez commits alcanzables desde `main` durante la auditoría registran actividad el **25 de septiembre de 2024 (UTC)**, incluidos tres merges. Referencia de la versión auditada: [`ce9570c`](https://github.com/XxKoosLoos/ExamenEmbebidos/commit/ce9570c81725e4bb36593506fbf9be62acc05b34). Esta fecha documenta actividad en Git, no el comienzo real del desarrollo.

Las ramas `main` y `master` se conservan. Los cambios posteriores se registran en [CHANGELOG.md](CHANGELOG.md).
