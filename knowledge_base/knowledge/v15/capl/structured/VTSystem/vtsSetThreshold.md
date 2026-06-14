# vtsSetThreshold

> Category: `VTSystem` | Type: `function`

## Syntax

```c
long vtsSetThreshold (char Target[], dword Group, double Threshold);
```

## Description

Sets the threshold value for differentiating between high and low levels of a group of channels on a VT2848 module.There is only one threshold setting for each group.Voltages at the input exceeding this threshold value are evaluated as high level and voltages undershooting it are evaluated as low level.

## Parameters

| Name | Description |
|---|---|
| Target | Name of the system variable/namespace that will be affected by this function call. |
| Group | Values see eVTSThresholdGroup |
| Threshold | Voltage value in volts in the range from 0…40 V. |

## Example

The following example demonstrates how to configure the first channel of a VT2848 module for PWM measurement. The channel used in this example is called RPM_Sensor, the VT2848 is called Sensors.

```c
PWMMeasurement ()
{
   // Set the PWM thresholds of channels 1 to 8 to 2.5V
   vtsSetThreshold("Sensors", eVTSThresholdGroupChannels1To8, 2.5);

   // Set the PWM measurement duration of the first channel to 100ms
   vtsSetPWMMeasurementDuration("RPM_Sensor", 0.1);

   // Wait 500ms and output the measured PWM frequency and duty cycle
   TestWaitForTimeout(500);
   write("Measured frequency %fHz and DC %f", @sysvar::VTS::RPM_Sensor::PWMFreq, @sysvar::VTS::RPM_Sensor::PWMDC);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.6 SP4 | 13.0 | — | — | 1.0 |
| Restricted To | — | — | VT offline | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
