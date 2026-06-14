# Iso11783OPOnValueChange

> Category: `ISO11783` | Type: `function`

## Syntax

```c
void Iso11783OPOnValueChange( dword ecuHandle, dword objectID );
```

## Description

The function is called by the node layer, if the value of an object is changed (with the command Change String Value or Change Numeric Value). The functions Iso11783OPGetStringValue and Iso11783OPGetNumericValue can be used to get the new value of the object.

## Parameters

| Name | Description |
|---|---|
| ecuHandle | Handle of the ECU |
| objectID | Object Identifier of the changed object |

## Return Values

—

## Example

```c
void Iso11783OPOnValueChange( dword handle, dword objectID )
{
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 6.1 | 13.0 | — | — | — |
| Restricted To | — | ISO11783 | ISO11783 | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
