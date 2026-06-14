# interpretAsDword, interpretAsFloat, interpretAsQword, interpretAsDouble

> Category: `Other` | Type: `function`

## Syntax

```c
dword interpretAsDword(float x);
float interpretAsFloat(dword x);
qword interpretAsQword(double x);
double interpretAsDouble(qword x);
```

## Description

These functions interpret the actual bytes of a value as if the value was of another data type.

InterpretAsFloat for example takes the four bytes or a dword, interprets them as if they were four bytes of an IEEE single precision floating point number, and returns that number.

InterpretAsDouble interprets eight bytes as if they were an IEEE double precision floating point number.

InterpretAsDword and InterpretAsQword are the inverse functions.

## Parameters

| Name | Description |
|---|---|
| x | The number which shall be interpreted. |

## Return Values

The interpreted value.

## Example

```c
// take a message with 8 bytes representing a double number
on message MessageWithDoubleSignal
{
  qword rawBytes;
  double value;
  rawBytes = this.qword(0);
  value = interpretAsDouble(rawBytes);
  write("The value is %g", value);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.5 | 8.5 | 13.0 | 13.0 | 14 | 2.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | ✔ | N/A |
