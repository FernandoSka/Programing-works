long distancia;
long tiempo;
int cuenta;

void setup(){
  Serial.begin(9600);
  pinMode(36, OUTPUT); /*activación del pin 9 como salida: para el pulso ultrasónico*/
  pinMode(37, INPUT); /*activación del pin 8 como entrada: tiempo del rebote del ultrasonido*/
}

void loop(){
  digitalWrite(36,LOW); /* Por cuestión de estabilización del sensor*/
  delayMicroseconds(5);
  digitalWrite(36, HIGH); /* envío del pulso ultrasónico*/
  delayMicroseconds(10);
  tiempo=pulseIn(37, HIGH); /* Función para medir la longitud del pulso entrante. Mide el tiempo que transcurrido entre el envío
  del pulso ultrasónico y cuando el sensor recibe el rebote, es decir: desde que el pin 12 empieza a recibir el rebote, HIGH, hasta que
  deja de hacerlo, LOW, la longitud del pulso entrante*/
  distancia= double(0.017*tiempo); /*fórmula para calcular la distancia obteniendo un valor entero*/
  /*Monitorización en centímetros por el monitor serial*/
  //Serial.print("Distancia ");
  if(distancia>15&&distancia<200){
     Serial.print(1);
     delay(5000);
  }
 

  delay(500);
}
