# vtsSetPWMStartDelay

> Category: `VTSystem` | Type: `function`

## Syntax

```c
long vtsSetPWMStartDelay (char Target[], double StartDelay);
```

## Description

Specifies a delay for the start of a curve stimulation or PWM stimulation. This function is supported by the modules VT2004 and VT2848.

## Parameters

| Name | Description |
|---|---|
| Target | Name of the system variable/namespace that will be affected by this function call. |
| StartDelay | Time for that the start of PWM or curve output is delayed. This function can be used e.g. to put out several signals with a defined phase shift. The StartDelay is denoted in seconds. Allowed values are from 0.0...4.0 (4s). This parameter is transferred to the VT System with nanosecond resolution. |

## Example

In the following example the PWM output of two VT2004 channels is simulating two sensors with PWM output. The SetPWMStartDelay command ensures that the PWM output on channel Sensor2 is starting 2ms later to produce the corresponding phase shift.

```c
// Set up PWM stimulation for sensor 1

// Set voltage stimulation mode
vtsSetStimulationMode( "VTS::Sensor1", 1);
// Set curve type PWM
vtsSetCurveType("VTS::Sensor1", 1);
// Set the low voltage of the PWM signal to 10V
vtsSetPWMVoltageLow("VTS::Sensor1", 10);
// Set the high voltage of the PWM signal to 14V
vtsSetPWMVoltageHigh("VTS::Sensor1", 14);
// Set duty cycle to 40%
@sysvar::VTS::Sensor1::PWMDC = 40;
// Set frequency to 100Hz
@sysvar::VTS::Sensor1::PWMFreq = 100;

// Set up PWM stimulation for sensor 2

// Set voltage stimulation mode
vtsSetStimulationMode("VTS::Sensor2", 1);
// Set curve type PWM
vtsSetCurveType("VTS::Sensor2", 1);
// Set the low voltage of the PWM signal to 10V
vtsSetPWMVoltageLow("VTS::Sensor2", 10);
// Set the high voltage of the PWM signal to 14V
vtsSetPWMVoltageHigh("VTS::Sensor2", 14);
// Set duty cycle to 40%
@sysvar::VTS::Sensor2::PWMDC = 40;
// Set frequency to 100Hz
@sysvar::VTS::Sensor2::PWMFreq = 100;

// set a start delay of 2ms for Sensor2
// -> PWM signals have a slight phase shift
vtsSetPWMStartDelay("VTS::Sensor2",  0.002);

// Start stimulation
vtsStartStimulation("VTS::Sensor1");
vtsStartStimulation("VTS::Sensor2");
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
