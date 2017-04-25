import processing.serial.*;

Serial serial;

void setup() {
  //size(320, 240);
  size(920, 640); // +600, +400
  rect(300, 200, 320, 240);
  
  printArray(Serial.list());
  serial = new Serial(this, Serial.list()[0], 115200);
  out:
  while (true) {
    delay(100);
    try {
      if (serial.readStringUntil('\n').equals("1023\r\n")) break out;
    } catch(NullPointerException e) {
      continue;
    }
  }
}

void draw() {
  while (serial.available() > 10) {
    background(192);
    fill(255);
    stroke(0);
    rect(300, 200, 320, 240); // outline
    
    // read serial input
    int f = 0;
    if (serial.readChar() == 'F') {
      f = Integer.parseInt(Character.toString(serial.readChar())); // 1,2,3,4
      serial.readChar(); // [space]
      print('F');
      print(f);
      print(' ');
    } else {
      print("   ");
    }
    serial.readChar(); // (
    int x = Integer.parseInt(serial.readStringUntil(' ').trim());
    serial.readChar(); // ,
    serial.readChar(); // [space]
    int y = Integer.parseInt(serial.readStringUntil(')').replace(')', ' ').trim());
    serial.readStringUntil('\n');
    
    // draw function button
    if (f != 0) { // draw function button (if one is pressed)
      fill(0, 255, 0); // green
      noStroke(); // no outlines used with function button drawing
      rect(301, 141+60*f, 20, 60);
    }
    
    // draw cursor
    print('(');
    print(x, ',', y);
    print(")\n");
    if (!(x==0 && y==0)) { // draw circle for cursor (if the screen is touched)
      fill(255);
      stroke(0);
      ellipse(300+(320-x), 200+y, 10, 10);
    }
  }
}
