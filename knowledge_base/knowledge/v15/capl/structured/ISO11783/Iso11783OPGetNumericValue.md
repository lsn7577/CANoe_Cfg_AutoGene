# Iso11783OPGetNumericValue

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783OPGetNumericValue( dword ecuHandle, dword objectID );
```

## Description

The function returns a numeric value of an object. The object must exist in the object pool and must support a numeric value.

## Parameters

| Name | Description |
|---|---|
| ecuHandle | Handle of the ECU (must be created with Iso11783CreateECU) |
| objectID | Object Identifier of the object |

## Return Values

Integer value of the object.
If a value of 0 is returned, you can check with the function Iso11783GetLastError if the function succeeded.

## Example

```c
LONG val;
val = Iso11783OPGetNumericValue( handle, 1000 );
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
