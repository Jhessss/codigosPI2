const int relePin = 7;  // pino onde o relé está conectado

void setup() {
  pinMode(relePin, OUTPUT);
  digitalWrite(relePin, LOW);  // Inicialmente, o relé está desligado

  // Se o Arduino está ligado, então liga o relé por 30 segundos
  digitalWrite(relePin, HIGH);  // Liga o relé
  delay(30000);                 // Mantém ligado por 30 segundos
  digitalWrite(relePin, LOW);   // Desliga o relé
}

void loop() {
  // Não precisa fazer nada no loop
}
