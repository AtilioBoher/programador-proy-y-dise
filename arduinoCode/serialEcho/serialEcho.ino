int incomingByte = 0; // for incoming serial data

void setup() {
  Serial.begin(9600); // opens serial port, sets data rate to 9600 bps
}

void loop() {
  // send data only when you receive data:
  if (Serial.available() > 0) {
    // read the incoming byte:
    incomingByte = Serial.read();

    // say what you got:
    Serial.print("ASCII HEX BIN DEC: ");
    Serial.print((char)incomingByte);
    Serial.print("  ");
    Serial.print(incomingByte, HEX);
    Serial.print("  ");
    Serial.print(incomingByte, BIN);
    Serial.print("  ");
    Serial.println(incomingByte, DEC);
  }
}

