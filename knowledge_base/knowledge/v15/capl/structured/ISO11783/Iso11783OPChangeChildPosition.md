# Iso11783OPChangeChildPosition

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783OPChangeChildPosition( dword ecuHandle, dword parentID, dword objectID, long x, long y );
```

## Description

The function changes the absolute position of an object inside its parent object. A Change Child Position command is sent to the Virtual Terminal.

## Parameters

| Name | Description |
|---|---|
| ecuHandle | Handle of the ECU (must be created with Iso11783CreateECU) |
| parentID | Parent object |
| objectID | Object which should change its position |
| x | Absolute X Position inside the parent object |
| y | Absolute Y Position inside the parent object |

## Return Values

0 or error code

## Example

```c
Iso11783OPChangeChildPosition( handle, 1000, 1200, 10, 10 );
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
