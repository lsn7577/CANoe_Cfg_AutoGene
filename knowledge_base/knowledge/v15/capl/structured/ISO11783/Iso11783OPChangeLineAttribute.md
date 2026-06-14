# Iso11783OPChangeLineAttribute

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783OPChangeLineAttribute( dword ecuHandle, dword objectID, dword color, dword width, dword art );
```

## Description

The function changes the properties of a line attribute object. A Change Line Attribute command is sent to the Virtual Terminal.

## Parameters

| Name | Description |
|---|---|
| ecuHandle | Handle of the ECU (must be created with Iso11783CreateECU) |
| objectID | Object ID of a line attribute object |
| color | Color index |
| width | Width of line in pixel |
| art | Bit pattern which is used to draw the line |

## Return Values

0 or error code

## Example

```c
Iso11783OPChangeLineAttributeibute( handle, 1100, 10, 3, 0xaa );
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
