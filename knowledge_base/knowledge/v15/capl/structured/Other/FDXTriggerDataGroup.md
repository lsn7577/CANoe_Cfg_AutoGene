# FDXTriggerDataGroup

> Category: `Other` | Type: `function`

## Syntax

```c
long FDXTriggerDataGroup (WORD goupID);
```

## Description

This function triggers the transmission of a data group via CANoe FDX protocol.

## Parameters

| Name | Description |
|---|---|
| groupID | ID of the FDX data group that should be transmitted. |

## Example

```c
// CANoe FDX data exchange synchronously to FlexRay cycle
// Whenever slot 5 of the FlexRay cycle will be reached, the FDX data group 10 is transmitted one time 

on frSlot 5
{
   FDXTriggerDataGroup(10);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.6 | 13.0 | — | 14 | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
