# Iso11783OPChangeChildLocation

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783OPChangeChildLocation( dword ecuHandle, dword parentID, dword objectID, long dx, long dy );
```

## Description

The function moves an object. The object is moved relative inside the parent object. A Change Child Location command is sent to the Virtual Terminal.

## Parameters

| Name | Description |
|---|---|
| ecuHandle | Handle of the ECU (must be created with Iso11783CreateECU) |
| parentID | Parent object |
| objectID | Object ID of the object which should be moved |
| dx | Move X position relative by this value [pixel] |
| dy | Move Y position relative by this value [pixel] |

## Return Values

0 or error code

## Example

```c
// move object 5 pixels to the right
Iso11783OPChangeChildLocation( handle, 1000, 
 1200, 5, 0 );
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
