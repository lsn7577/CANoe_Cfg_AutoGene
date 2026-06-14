# Iso11783IL_OPOnAuxiliaryInput

> Category: `ISO11783` | Type: `function`

## Syntax

```c
void Iso11783IL_OPOnAuxiliaryInput( dword objectID, dword value1, dword value2 );
```

## Description

The function is called by the node layer, if an Auxiliary Input Status is received and a Auxiliary Function in the object pool is assigned.

## Parameters

| Name | Description |
|---|---|
| objectID | Object identifier of the auxiliary function object |
| value1 | Value 1 |
| value2 | Value 2 |

## Return Values

—

## Example

```c
void Iso11783IL_OPOnAuxiliaryInput( dword objectID, dword value1, dword value2 )
{
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.0 | 13.0 | — | — | — |
| Restricted To | — | ISO11783 | ISO11783 | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
