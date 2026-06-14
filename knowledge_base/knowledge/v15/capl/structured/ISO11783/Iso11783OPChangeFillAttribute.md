# Iso11783OPChangeFillAttribute

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783OPChangeFillAttribute( dword ecuHandle, dword objectID, dword color, dword type, dword patternID );
```

## Description

The function changes the properties of a fill attribute object. A Change Fill Attribute command is sent to the Virtual Terminal.

## Parameters

| Name | Description |
|---|---|
| ecuHandle | Handle of the ECU (must be created with Iso11783CreateECU) |
| objectID | Object ID of a fill attribute object |
| color | Color index |
| type | Fill type: 0: do not fill 1: fill with line color 2: fill with fill color 3: fill with pattern from patternID |
| patternID | Object ID of a picture object, which is used as fill pattern |

## Return Values

0 or error code

## Example

```c
Iso11783OPChangeFillAttribute( handle, 1100, 12, 2, 0xFFFF );
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
