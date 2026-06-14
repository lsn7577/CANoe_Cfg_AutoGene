# _round

> Category: `Other` | Type: `function`

## Syntax

```c
long _round(double x); // form 1
int64 _round64(double x); // from 2
```

## Description

Rounds x to the nearest integral number. The rounding method used is symmetric arithmetic rounding.

## Parameters

| Name | Description |
|---|---|
| x | Number to be rounded |

## Return Values

Nearest integral number.
For very large numbers, you should use _round64, which returns a 64 bit integer.

## Example

```c
long result;
result = _round(2.4); // result == 2
result = _round(2.5); // result == 3
result = _round(-3.5); // result == -4
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.0 | 7.0 | 13.0 | — | 14 | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | ✔ | N/A |
