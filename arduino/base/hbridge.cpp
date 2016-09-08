#include "hbridge.h"
#include "Arduino.h"

#define HBRIDGE_PWM_MAX 255
#define HBRIDGE_PWM_MIN 0
#define HBRIDGE_SAT(x) ( ((x) > HBRIDGE_PWM_MAX) ? HBRIDGE_PWM_MAX : ( ((x) < HBRIDGE_PWM_MIN) ? HBRIDGE_PWM_MIN : (x) ) )

HBridge::HBridge(uint8_t pinPwm, uint8_t pinA, uint8_t pinB):
  _pinPwm(pinPwm),
  _pinA(pinA),
  _pinB(pinB)
{
  pinMode(_pinPwm, OUTPUT);
  pinMode(_pinA, OUTPUT);
  pinMode(_pinB, OUTPUT);
  brake();
}

void HBridge::forward()
{
  digitalWrite(_pinA, HIGH);
  digitalWrite(_pinB, LOW);
}

void HBridge::backward()
{
  digitalWrite(_pinA, LOW);
  digitalWrite(_pinB, HIGH);
}

void HBridge::brake()
{
  digitalWrite(_pinA, LOW);
  digitalWrite(_pinB, LOW);
}

void HBridge::activeBrake()
{
  digitalWrite(_pinA, HIGH);
  digitalWrite(_pinB, HIGH);
}

void HBridge::setRawPwm(uint8_t pwm)
{
  analogWrite(_pinPwm, pwm);
}

void HBridge::set(int16_t target)
{
  uint8_t pwm_target;

  if (target > 0)
  {
    forward();
    pwm_target = HBRIDGE_SAT(target);
  }
  else
  {
    backward();
    pwm_target = HBRIDGE_SAT(-target);
  }
  setRawPwm(pwm_target);
}
