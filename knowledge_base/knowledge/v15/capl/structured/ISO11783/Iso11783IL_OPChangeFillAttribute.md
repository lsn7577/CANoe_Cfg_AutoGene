# Iso11783IL_OPChangeFillAttribute

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_OPChangeFillAttribute( dword objectID, dword color, dword type, dword patternID ); // form 1
long Iso11783IL_OPChangeFillAttribute( dbNode implement, dword objectID, dword color, dword type, dword patternID ); // form 2
```

## Description

The function changes the properties of a fill attribute object. A Change Fill Attribute command is sent to the Virtual Terminal.

## Parameters

| Name | Description |
|---|---|
| objectID | Object ID of a fill attribute object |
| color | Color index |
| type | Fill type:0 = do not fill1 = fill with line color2 = fill with fill color3 = fill with pattern from patternID |
| patternID | Object ID of a picture object, which is used as fill pattern |
| implement | Simulation node to apply the function. |

## Example

```c
Iso11783IL_OPChangeFillAttribute( 1100, 12, 2, 0xFFFF );
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.0 | 13.0 | — | — | 2.1 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 2 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1) | ✔ (form 1) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 2) | ✔ (form 2) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 2) | ✔ (form 2) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
