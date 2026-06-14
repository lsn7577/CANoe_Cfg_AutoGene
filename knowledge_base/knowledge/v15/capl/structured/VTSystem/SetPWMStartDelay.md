# SetPWMStartDelay

> Category: `VTSystem` | Type: `method`

## Syntax

```c
Long SysVarNamespace.SetPWMStartDelay (double StartDelay);
```

## Description

Sets the delay of the start for the output of PWM signals and curves. This function is supported by the modules VT2004 and VT2848.

## Parameters

| Name | Description |
|---|---|
| StartDelay | Time for that the start of PWM or curve output is delayed. This function can be used e.g. to put out several signals with a defined phase shift. The StartDelay is denoted in seconds. Allowed values are from 0.0...4.0 (4s). This parameter is transferred to the VT System with nanosecond resolution. |

## Example

In the following example the PWM output of two VT2004 channels is simulating two sensors with PWM output. The SetPWMStartDelay command ensures that the PWM output on channel Sensor2 is starting 2ms later to produce the corresponding phase shift.

```c
// Set up PWM stimulation for sensor 1

// Set voltage stimulation mode
sysvar::VTS::Sensor1.SetStimulationMode(1);
// Set curve type PWM
sysvar::VTS::Sensor1.SetCurveType(1);
// Set the low voltage of the PWM signal to 10V
sysvar::VTS::Sensor1.SetPWMVoltageLow(10);
// Set the high voltage of the PWM signal to 14V
sysvar::VTS::Sensor1.SetPWMVoltageHigh(14);
// Set duty cycle to 40%
@sysvar::VTS::Sensor1::PWMDC = 40;
// Set frequency to 100Hz
@sysvar::VTS::Sensor1::PWMFreq = 100;

// Set up PWM stimulation for sensor 2

// Set voltage stimulation mode
sysvar::VTS::Sensor2.SetStimulationMode(1);
// Set curve type PWM
sysvar::VTS::Sensor2.SetCurveType(1);
// Set the low voltage of the PWM signal to 10V
sysvar::VTS::Sensor2.SetPWMVoltageLow(10);
// Set the high voltage of the PWM signal to 14V
sysvar::VTS::Sensor2.SetPWMVoltageHigh(14);
// Set duty cycle to 40%
@sysvar::VTS::Sensor2::PWMDC = 40;
// Set frequency to 100Hz
@sysvar::VTS::Sensor2::PWMFreq = 100;

// set a start delay of 2ms for Sensor2
// -> PWM signals have a slight phase shift
sysvar::VTS::Sensor2.SetPWMStartDelay( 0.02);

// Start stimulation
sysvar::VTS::Sensor1.StartStimulation();
sysvar::VTS::Sensor2.StartStimulation();
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
