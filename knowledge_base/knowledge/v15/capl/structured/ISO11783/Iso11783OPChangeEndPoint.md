# Iso11783OPChangeEndPoint

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783OPChangeEndPoint( dword ecuHandle, dword objectID, dword width, dword height, dword direction );
```

## Description

The function changes the length and alignment of a line object. A Change End Point command is sent to the Virtual Terminal.

## Parameters

| Name | Description |
|---|---|
| ecuHandle | Handle of the ECU (must be created with Iso11783CreateECU) |
| objectID | Object ID of the line object |
| width | Width of the bounding rectangle of the object |
| height | Height of the bounding rectangle of the object |
| direction | Alignment of the line 0: from top/left to bottom/right1: from bottom/left to top/right |

## Return Values

0 or error code

## Example

```c
Iso11783OPChangeEndPoint( handle, 1200, 50, 20, 0 );
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
