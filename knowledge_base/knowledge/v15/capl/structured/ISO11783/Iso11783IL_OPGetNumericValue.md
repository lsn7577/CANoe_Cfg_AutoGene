# Iso11783IL_OPGetNumericValue

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_OPGetNumericValue( dword objectID, long& value ); // form 1
long Iso11783IL_OPGetNumericValue( dbNode implement, dword objectID, long& value ); // form 2
long Iso11783IL_OPGetNumericValue( dword objectID ); // form 3 deprecated
long Iso11783IL_OPGetNumericValue( dbNode implement, dword objectID ); // form 4 deprecated
```

## Description

The function returns a numeric value of an object. The object must exist in the object pool and must support a numeric value.

## Parameters

| Name | Description |
|---|---|
| objectID | Object Identifier of the object. |
| implement | Simulation node to apply the function. |
| value | Returns the integer value of the object. |

## Example

```c
LONG val, result
result = Iso11783IL_OPGetNumericValue( 1000, value);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.0: form 3 9.0: form 4 12.0 SP2: form 1, 2 | 13.0 | — | — | 2.1 SP2: form 4 4.0 SP2: form 2 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 2, 4 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1, 3) | ✔ (form 1, 3) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 2, 4) | ✔ (form 2, 4) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 2, 4) | ✔ (form 2, 4) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
