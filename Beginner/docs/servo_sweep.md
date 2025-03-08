
#### 3. **servo_sweep.md**

```markdown
# Servo Sweep

This example demonstrates how to control a servo motor to perform a sweep motion.

### Components Used:
- Servo motor
- Arduino board

### How it works:
- The servo motor sweeps between 0 and 180 degrees, moving back and forth.

### Code Example:
```cpp
#include <Servo.h>

Servo motor;

void setup() {
  motor.attach(9);
}

void loop() {
  for (int pos = 0; pos <= 180; pos++) {
    motor.write(pos);
    delay(15);
  }
  for (int pos = 180; pos >= 0; pos--) {
    motor.write(pos);
    delay(15);
  }
}
