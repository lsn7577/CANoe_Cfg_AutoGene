# Iso11783IL_OPGetAttribute

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_OPGetAttribute( dword objectID, dword attributeID ); // form 1
long Iso11783IL_OPGetAttribute( dbNode implement, dword objectID, dword attributeID ); // form 2
```

## Description

The function returns a value of an object attribute from the local object pool. A Get Attribute command is not sent to the Virtual Terminal. The object must exist in the object pool and support the attribute ID.

## Parameters

| Name | Description |
|---|---|
| objectID | object identifier of an object in the object pool |
| attributeID | attribute identifier, see ISO11783-6 |
| implement | Simulation node to apply the function. |

## Return Values

Integer value of the object.
If a value of 0 is returned, you can check with the function Iso11783IL_GetLastError if the function succeeded.

## Example

```c
LONG objType;
objType = Iso11783IL_OPGetAttribute( 1000, 0 );
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.0: form 1 9.0: form 2 | 13.0 | — | — | 2.1 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 2 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1) | ✔ (form 1) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 2) | ✔ (form 2) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 2) | ✔ (form 2) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
