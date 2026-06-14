# SetPWMResistanceLow

> Category: `VTSystem` | Type: `method`

## Syntax

```c
long SysVarNamespace.SetPWMResistanceLow (double Resistance);
```

## Description

Specifies the resistance value of a low signal on PWM output in Resistance output PWM mode.

## Parameters

| Name | Description |
|---|---|
| Resistance | Resistance value in ohms.Resistance may have values from 1.0 (1 Ω) up to 250000.0 (250 kΩ). This range is only supported by channel 4 of the VT2004 module. The other channels can handle values from 10.0 (10 Ω) up to 150000.0 (150 kΩ).In special cases Resistance may be set to -1 on each channel to get infinite resistance. Values outside the hardware's possible range of values are rounded up to the next highest value or the highest or lowest possible value is used. |

## Example

See example SetPWMResistanceHigh

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
