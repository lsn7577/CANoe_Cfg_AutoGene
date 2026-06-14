# CarMaker_WriteAbs

> Category: `CarMaker` | Type: `function`

## Syntax

```c
long CarMaker_WriteAbs(char varName[], double duration_ms, double value);
```

## Description

Modifies the value of a CarMaker quantity. The CarMaker quantity must support write access.

## Parameters

| Name | Description |
|---|---|
| varName | Absolute name of the CarMaker quantity. |
| duration_ms | Duration for fixing the value. |
| value | The new value to be set. |

## Return Values

APO return code

## Example

```c
gErrorState = CarMaker_WriteAbs("DM.Brake", 1000, 1.0);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 13.0 | — | — | — | 5.0 |
| Restricted To | — | CarMaker | — | — | — | CarMaker |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
