# startValuesUpdateSymbols

> Category: `Other` | Type: `function`

## Syntax

```c
void startValuesUpdateSymbols(char groupName[]);
```

## Description

Sets the variables/signals contained in a specific group to their individual start values in the CANoeStart Value Window.

## Parameters

| Name | Description |
|---|---|
| groupName | Name of a group containing variables/signals that are set to their individual start values. If groupName is equal to "", then all variables/signals contained in the Start Values Window are set to their individual start values. |

## Return Values

—

## Example

```c
on key '3'
{
startValuesUpdateSymbols("Start values group2");
}

on key '4'
{
startValuesUpdateSymbols("");
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 10.0 | 10.0 | 13.0 | — | 14 | 2.2 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | ✔ | N/A |
