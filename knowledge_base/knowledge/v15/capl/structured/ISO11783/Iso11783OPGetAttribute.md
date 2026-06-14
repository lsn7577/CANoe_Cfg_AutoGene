# Iso11783OPGetAttribute

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783OPGetAttribute( dword ecuHandle, dword objectID, dword attributeID );
```

## Description

The function returns a value of an object attribute from the local object pool. A Get Attribute command is not sent to the Virtual Terminal. The object must exist in the object pool and support the attribute ID.

## Parameters

| Name | Description |
|---|---|
| ecuHandle | Handle of the ECU (must be created with Iso11783CreateECU) |
| objectID | Object identifier of an object in the object pool |
| attributeID | Attribute identifier, see ISO11783-6 |

## Return Values

Integer value of the object.
If a value of 0 is returned, you can check with the function Iso11783GetLastError if the function succeeded.

## Example

```c
LONG objType;
objType = Iso11783OPGetAttribute( handle, 1000, 0 );
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
