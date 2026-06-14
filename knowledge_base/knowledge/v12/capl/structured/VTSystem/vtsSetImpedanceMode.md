# vtsSetImpedanceMode

> Category: `VTSystem` | Type: `function`

## Syntax

```c
long vtsSetImpedanceMode (char Target[], eVTSImpedanceMode Mode);
```

## Description

Switches for VT1004A/VT1104 between the mode with high impedance (default state) and low impedance. The behavior of a channel in mode with high impedance is the same as the behavior of a channel in older VT1004 modules. In the mode with lower impedance the accurateness of the measurement of PWM frequency and duty cycle. This provides significant advantages especially for measurement of very low or high duty cycles. The input resistance is lower in this mode and thus the load on ECU output is higher. Details you find in the VT System Manual.

## Return Values

0: Successful call

## Example

PWM measurement with switching of the impedance mode.

```c
double frequency;
double dutyCycle;

  // Set PWM threshold to 12V
  vtsSetPWMThreshold( "LowBeamLeft", 12);
  // Set PWM measurement duration to 100ms
  vtsSetPWMMeasurementDuration( "LowBeamLeft", 0.1);
  // Enable low impedance mode to improve PWM measurement accuracy
  vtsSetImpedanceMode( "LowBeamLeft", eVTSImpedanceModeLow);

  // Wait a bit until the PWM measurement has finished
  testWaitForTimeout(200);

  // Get measured values
  frequency = @sysvar::VTS::LowBeamLeft::PWMFreq;
  dutyCycle = @sysvar::VTS::LowBeamLeft::PWMDC;

  // Check the frequency and duty cycle
  if( frequency > 50 && dutyCycle > 20 )
  {
    testStepPass();
  }
  else
  {
    testStepFail();
  }
  <vtsystem_configure title="Set PWM threshold and measurement duration">
    <pwm_measurement_duration channel="LowBeamLeft">100ms</pwm_measurement_duration>
    <pwm_threshold channel="LowBeamLeft">12</pwm_threshold>
    <impedance_mode channel="LowBeamLeft" mode="low" />
  </vtsystem_configure>

  <statecheck wait="200" title="Check frequency and duty cycle">
    <expected>
      <sysvar name="PWMFreq" namespace="VTS::LowBeamLeft">
        <gt>50</gt>
      </sysvar>
      <sysvar name="PWMDC" namespace="VTS::LowBeamLeft">
        <gt>20</gt>
      </sysvar>
    </expected>
  </statecheck>
```

## Availability

| Since Version |
|---|
