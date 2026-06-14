# SetImpedanceMode

> Category: `VTSystem` | Type: `method`

## Syntax

```c
Long SysVarNamespace.SetImpedanceMode (eVTSImpedanceMode Mode);
```

## Description

Switches for VT1004A/VT1104 between the mode with high impedance (default state) and low impedance. The behavior of a channel in mode with high impedance is the same as the behavior of a channel in older VT1004 modules. In the mode with lower impedance the accurateness of the measurement of PWM frequency and duty cycle. This provides significant advantages especially for measurement of very low or high duty cycles. The input resistance is lower in this mode and thus the load on ECU output is higher. Details you find in the VT System Manual.

## Parameters

| Name | Description |
|---|---|
| Mode | Sets the active impedance mode.Values see eVTSImpedanceMode |

## Example

PWM measurement with switching of the impedance mode.

```c
double frequency;
double dutyCycle;

  // Set PWM threshold to 12V
  sysvar::VTS::LowBeamLeft.SetPWMThreshold(12);
  // Set PWM measurement duration to 100ms
  sysvar::VTS::LowBeamLeft.SetPWMMeasurementDuration(0.1);
  // Enable low impedance mode to improve PWM measurement accuracy
  sysvar::VTS::LowBeamLeft.SetImpedanceMode(eVTSImpedanceModeLow);

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
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.1 | 13.0 | — | — | 1.0 |
| Restricted To | — | — | VT offline | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
