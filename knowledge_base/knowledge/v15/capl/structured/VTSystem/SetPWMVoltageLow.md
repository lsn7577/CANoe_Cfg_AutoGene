# SetPWMVoltageLow

> Category: `VTSystem` | Type: `method`

## Syntax

```c
long SysVarNamespace.SetPWMVoltageLow (double Voltage);
```

## Description

Specifies the low level on output of a digital output signal, especially a PWM signal.

## Parameters

| Name | Description |
|---|---|
| Voltage | Voltage of the low level in volts in the range 0 ... 27 V (VT2004), 0... 40V (VT2004A) resp. 0 ... 25 V (VT2516). |

## Example

See example SetStimulationMode

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.0 SP5 | 13.0 | — | — | 1.0 |
| Restricted To | — | — | VT offline | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
