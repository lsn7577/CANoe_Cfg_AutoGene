# Iso11783OPChangeActiveMask

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783OPChangeActiveMask( dword ecuHandle, dword maskID );
```

## Description

This function changes the active data mask. The Change Active Mask command is sent to the Virtual Terminal.

## Parameters

| Name | Description |
|---|---|
| ecuHandle | Handle of the ECU (must be created with Iso11783CreateECU) |
| maskID | Object ID of the data mask object, which should be activated |

## Return Values

0 or error code

## Example

```c
Iso11783OPChangeActiveMask( handle, 1000 );
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
