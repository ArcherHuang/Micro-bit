
#define LED_ROW2 27
#define LED_COL3 10

void setup() {
  // put your setup code here, to run once:
  pinMode(LED_ROW2, OUTPUT);
  pinMode(LED_COL3, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(LED_ROW2, 0);
  digitalWrite(LED_COL3, 0);
}
