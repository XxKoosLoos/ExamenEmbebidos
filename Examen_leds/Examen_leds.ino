// Definición de pines
const int LedVerde = 16;          // Pin para LED verde
const int LedAmarillo = 2;        // Pin para LED amarillo
const int LedRojo = 15;           // Pin para LED rojo
const int LedEntradaDatos = 18;   // Pin para LED de entrada de datos

const int BotonArranque = 35;     // Pin para el botón de arranque
const int BotonParo = 14;         // Pin para el botón de paro

// Duraciones de tiempo en milisegundos
const unsigned long intervalVerde = 9000;     // Intervalo para el LED verde (9 segundos)
const unsigned long intervalRojo = 12000;     // Intervalo para el LED rojo (12 segundos)
const unsigned long blinkOnDuration = 600;     // Duración del LED de transferencia de datos encendido (600 ms)
const unsigned long blinkOffDuration = 400;    // Duración del LED de transferencia de datos apagado (400 ms)
const unsigned long transferPauseDuration = 2000; // Pausa de 2 segundos después de parpadeos

// Contadores y temporizadores
unsigned long previousMillis = 0;               // Almacena el tiempo previo para el semáforo
unsigned long previousAmarilloMillis = 0;       // Almacena el tiempo previo para el parpadeo del LED amarillo
unsigned long previousBlinkMillis = 0;          // Almacena el tiempo previo para el parpadeo del LED de entrada de datos
unsigned long transferPauseMillis = 0;          // Almacena el tiempo para la pausa del LED de entrada de datos

// Estado de los LEDs
enum State {
  VERDE,
  AMARILLO,
  ROJO
};

State currentState = VERDE;                     // Estado inicial del semáforo

// Variables para el ciclo del LED de entrada de datos
int blinkCountEntrada = 0;                       // Contador de parpadeos del LED de entrada de datos
bool ledEntradaState = false;                    // Estado del LED de entrada de datos
bool waitingForPause = false;                    // Estado para indicar que se está en pausa

// Variables para controlar los botones
bool cicloPausado = false;                       // Estado pausado del ciclo
bool estadoBotonArranque = HIGH;                 // Estado del botón de arranque
bool estadoBotonParo = HIGH;                     // Estado del botón de paro
bool lastBotonArranque = HIGH;                   // Último estado del botón de arranque
bool lastBotonParo = HIGH;                       // Último estado del botón de paro

void setup() {
  // Configuración de pines como salida
  pinMode(LedVerde, OUTPUT);
  pinMode(LedAmarillo, OUTPUT);
  pinMode(LedRojo, OUTPUT);
  pinMode(LedEntradaDatos, OUTPUT);              // Configurar LED de entrada de datos como salida

  // Configuración de los botones como entradas con resistencia pull-up
  pinMode(BotonArranque, INPUT_PULLUP);         // Configurar botón de arranque como entrada
  pinMode(BotonParo, INPUT_PULLUP);             // Configurar botón de paro como entrada

  // Inicializar todos los LEDs apagados
  digitalWrite(LedVerde, LOW);
  digitalWrite(LedAmarillo, LOW);
  digitalWrite(LedRojo, LOW);
  digitalWrite(LedEntradaDatos, LOW);

  // Encender el LED verde
  digitalWrite(LedVerde, HIGH);  // Enciende el LED verde
  previousMillis = millis();      // Reinicia el temporizador para el LED verde
  previousBlinkMillis = millis(); // Reinicia el temporizador para el LED de entrada de datos
}

void loop() {
  unsigned long currentMillis = millis(); // Obtiene el tiempo actual

  // Leer los estados actuales de los botones
  estadoBotonArranque = digitalRead(BotonArranque);
  estadoBotonParo = digitalRead(BotonParo);

  // Detectar flanco descendente (cuando se presiona) para el botón de paro
  if (estadoBotonParo == LOW && lastBotonParo == HIGH) {
    cicloPausado = true;  // Pausar el ciclo del semáforo
    Serial.println("Ciclo pausado");
  }

  // Detectar flanco descendente (cuando se presiona) para el botón de arranque
  if (estadoBotonArranque == LOW && lastBotonArranque == HIGH) {
    cicloPausado = false;   // Reanudar el ciclo del semáforo
    Serial.println("Ciclo reanudado");
    previousMillis = millis();  // Ajustar el temporizador para continuar donde se dejó
  }

  // Guardar los últimos estados de los botones para la detección de flancos
  lastBotonArranque = estadoBotonArranque;
  lastBotonParo = estadoBotonParo;

  // Controlar el semáforo solo si el ciclo no está pausado
  if (!cicloPausado) {
    switch (currentState) {
      case VERDE:
        // Controlar el LED verde
        if (currentMillis - previousMillis >= intervalVerde) {
          digitalWrite(LedVerde, LOW); // Apaga el LED verde
          currentState = AMARILLO;     // Cambia al estado amarillo
          previousMillis = currentMillis; // Reinicia el temporizador
          previousAmarilloMillis = millis(); // Reinicia el temporizador para el LED amarillo
        }
        break;

      case AMARILLO:
        // Controlar el parpadeo del LED amarillo (2 parpadeos)
        if (currentMillis - previousAmarilloMillis >= blinkOnDuration) {
          previousAmarilloMillis = currentMillis; // Reinicia el temporizador
          digitalWrite(LedAmarillo, !digitalRead(LedAmarillo)); // Cambia el estado del LED amarillo

          // Contador para los parpadeos
          static int blinkCountAmarillo = 0;
          if (digitalRead(LedAmarillo) == HIGH) {
            blinkCountAmarillo++; // Incrementa el contador solo si el LED está encendido
          }

          // Cambiar al estado rojo después de 4 cambios de estado (2 parpadeos)
          if (blinkCountAmarillo >= 4) { // 2 parpadeos equivalen a 4 cambios de estado (encendido y apagado)
            digitalWrite(LedAmarillo, LOW); // Asegúrate de que está apagado
            currentState = ROJO;             // Cambia al estado rojo
            previousMillis = currentMillis;   // Reinicia el temporizador
            blinkCountAmarillo = 0; // Reiniciar contador de parpadeo
          }
        }
        break;

      case ROJO:
        digitalWrite(LedRojo, HIGH); // Enciende el LED rojo
        if (currentMillis - previousMillis >= intervalRojo) {
          digitalWrite(LedRojo, LOW); // Apaga el LED rojo
          currentState = VERDE;       // Cambia al estado verde
          digitalWrite(LedVerde, HIGH); // Enciende nuevamente el LED verde
          previousMillis = currentMillis; // Reinicia el temporizador
        }
        break;
    }
  }

  // Controlar el parpadeo del LED de entrada de datos
  if (ledEntradaState) {
    // Si el LED de entrada de datos está encendido, revisa si debe apagarse
    if (currentMillis - previousBlinkMillis >= blinkOnDuration) {
      ledEntradaState = false; // Apagar el LED de entrada de datos
      digitalWrite(LedEntradaDatos, LOW); // Actualiza el LED
      previousBlinkMillis = currentMillis; // Reinicia el temporizador
    }
  } else {
    // Si el LED de entrada de datos está apagado, revisa si debe encenderse
    if (currentMillis - previousBlinkMillis >= blinkOffDuration) {
      ledEntradaState = true; // Encender el LED de entrada de datos
      digitalWrite(LedEntradaDatos, HIGH); // Actualiza el LED
      previousBlinkMillis = currentMillis; // Reinicia el temporizador

      // Incrementa el contador de parpadeos
      blinkCountEntrada++; // Incrementa el contador de parpadeos
    }
  }

  // Manejo de la pausa de parpadeo
  if (blinkCountEntrada >= 4 && !waitingForPause) {
    digitalWrite(LedEntradaDatos, LOW); // Apaga el LED de entrada de datos
    waitingForPause = true; // Activar el estado de espera
    transferPauseMillis = currentMillis; // Guarda el tiempo actual
    blinkCountEntrada = 0; // Reinicia el contador de parpadeos
  } else if (waitingForPause) {
    // Controlar la pausa de 2 segundos
    if (currentMillis - transferPauseMillis >= transferPauseDuration) {
      waitingForPause = false; // Reiniciar el ciclo de parpadeo
    }
  }

  // Imprimir el estado de los LEDs en una sola línea
  Serial.print("led verde: ");
  Serial.print(digitalRead(LedVerde));
  Serial.print(", led amarillo: ");
  Serial.print(digitalRead(LedAmarillo));
  Serial.print(", led rojo: ");
  Serial.println(digitalRead(LedRojo));
}
