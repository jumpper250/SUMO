// ----------------- ตั้งค่าขา -----------------
int LS = 3;
int RS = 2;

int PWM1 = 10;
int RM1 = 4;
int RM2 = 5;

int PWM2 = 11;
int LM1 = 6;
int LM2 = 7;

int speed1 = 70;
int speed2 = 95;

// ✅ ปรับให้ LOW = ขาว (เพราะของคุณเหมือนจะกลับด้าน)
int line_detect = LOW;

void setup() {
  pinMode(LS, INPUT);
  pinMode(RS, INPUT);

  pinMode(RM1, OUTPUT);
  pinMode(RM2, OUTPUT);
  pinMode(PWM1, OUTPUT);

  pinMode(LM1, OUTPUT);
  pinMode(LM2, OUTPUT);
  pinMode(PWM2, OUTPUT);

  stopMoving();
  Serial.begin(9600);
}

void loop() {
  int leftSensor = digitalRead(LS);
  int rightSensor = digitalRead(RS);

  Serial.print("Left: ");
  Serial.print(leftSensor);
  Serial.print(" | Right: ");
  Serial.println(rightSensor);

  if (leftSensor == line_detect && rightSensor == line_detect) {
    moveForward();
  } else if (rightSensor != line_detect) {
    reverseLong();
    pivotTurnRight();  // เพิ่มเวลาหมุนขวาให้มากขึ้น
  } else if (leftSensor != line_detect) {
    reverseLong();
    pivotTurnLeft();  // เพิ่มเวลาหมุนซ้ายให้มากขึ้น
  }
}

// ----------------- ฟังก์ชันควบคุมการเคลื่อนที่ -----------------

void moveForward() {
  digitalWrite(RM1, HIGH);
  digitalWrite(RM2, LOW);
  analogWrite(PWM1, speed1);

  digitalWrite(LM1, HIGH);
  digitalWrite(LM2, LOW);
  analogWrite(PWM2, speed2);
}

void pivotTurnRight() {
  digitalWrite(RM1, LOW);
  digitalWrite(RM2, HIGH);
  analogWrite(PWM1, speed1);

  digitalWrite(LM1, HIGH);
  digitalWrite(LM2, LOW);
  analogWrite(PWM2, speed2);

  delay(500);  // ✅ หมุนขวานานขึ้น (เพิ่มเวลาเป็น 500ms)
}

void pivotTurnLeft() {
  digitalWrite(RM1, HIGH);
  digitalWrite(RM2, LOW);
  analogWrite(PWM1, speed1);

  digitalWrite(LM1, LOW);
  digitalWrite(LM2, HIGH);
  analogWrite(PWM2, speed2);

  delay(500);  // ✅ หมุนซ้ายมากขึ้น (เพิ่มเวลาเป็น 500ms)
}

void reverseLong() {
  digitalWrite(RM1, LOW);
  digitalWrite(RM2, HIGH);
  analogWrite(PWM1, speed1);

  digitalWrite(LM1, LOW);
  digitalWrite(LM2, HIGH);
  analogWrite(PWM2, speed2);

  delay(1000);  // ✅ ถอยหลังนานขึ้น (เพิ่มเวลาเป็น 1000ms)
}

void stopMoving() {
  analogWrite(PWM1, 0);
  analogWrite(PWM2, 0);

  digitalWrite(RM1, LOW);
  digitalWrite(RM2, LOW);
  digitalWrite(LM1, LOW);
  digitalWrite(LM2, LOW);
}
