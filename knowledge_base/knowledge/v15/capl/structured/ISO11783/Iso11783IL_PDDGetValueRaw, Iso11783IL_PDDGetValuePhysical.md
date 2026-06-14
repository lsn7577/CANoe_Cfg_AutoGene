# Iso11783IL_PDDGetValueRaw, Iso11783IL_PDDGetValuePhysical

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_PDDGetValueRaw(dword ddi, dword elementNumber, long& value); // form 1
long Iso11783IL_PDDGetValueRaw(dbNode implement, dword ddi, dword elementNumber, long& value); // form 2
long Iso11783IL_PDDGetValuePhysical(dword ddi, dword elementNumber, double& value); //form 3
long Iso11783IL_PDDGetValuePhysical(dbNode implement, dword ddi, dword elementNumber, double& value); // form 4
```

## Description

Gets the value of a data entity (process variable) without sending any command.

## Parameters

| Name | Description |
|---|---|
| ddi | Data Dictionary Identifier, 0x0000.0xFFFF. |
| elementNumber | Element number, 0x000.0xFFF. |
| value | Returns the value of the data entity (process variable). |
| implement | Simulation node to apply the function. |

## Example

Example form 2

```c
double currentValue;
long result;
result = Iso11783IL_PDDGetValuePhysical(120, 2, currentValue);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 12.0 SP2 | 13.0 | — | — | 4.0 SP2 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 2, 4 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1, 3) | ✔ (form 1, 3) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 2, 4) | ✔ (form 2, 4) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 2, 4) | ✔ (form 2, 4) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
