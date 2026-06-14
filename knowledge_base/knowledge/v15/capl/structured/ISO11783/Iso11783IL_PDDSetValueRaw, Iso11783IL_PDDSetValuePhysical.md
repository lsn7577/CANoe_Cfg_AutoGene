# Iso11783IL_PDDSetValueRaw, Iso11783IL_PDDSetValuePhysical

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_PDDSetValueRaw(dword ddi, dword elementNumber, long value); // form 1
long Iso11783IL_PDDSetValueRaw(dbNode implement, dword ddi, dword elementNumber, long value); // form 2
long Iso11783IL_PDDSetValuePhysical(dword ddi, dword elementNumber, double value); //form 3
long Iso11783IL_PDDSetValuePhysical(dbNode implement, dword ddi, dword elementNumber, double value); // form 4
```

## Description

Sets the value of a data entity (process variable) without sending any command.

## Parameters

| Name | Description |
|---|---|
| ddi | Data Dictionary Identifier, 0x0000.0xFFFF |
| elementNumber | Element number, 0x000.0xFFF |
| value | New value of the data entity (process variable) |
| implement | Task Controller simulation node to apply the function. |

## Example

Example form 2

Example form 4

```c
SetActualAppRateUsingRawValue()
{
  // section 1: elementNumber = 3
  Iso11783IL_PDDSetValueRaw(Sprayer, 37, 3, 13360);
  // section 2: elementNumber = 4
  Iso11783IL_PDDSetValueRaw(Sprayer, 37, 4, 13950);
}
SetActualAppRateUsingRawValue()
{
  // section 1: elementNumber = 3
  Iso11783IL_PDDSetValuePhysical(Sprayer, 37, 3, 13.360);
  // section 2: elementNumber = 4
  Iso11783IL_PDDSetValuePhysical(Sprayer, 37, 4, 13.950);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 9.0 SP3 | 13.0 | — | — | 2.1 SP3 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 2, 4 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1, 3) | ✔ (form 1, 3) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 2, 4) | ✔ (form 2, 4) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 2, 4) | ✔ (form 2, 4) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
