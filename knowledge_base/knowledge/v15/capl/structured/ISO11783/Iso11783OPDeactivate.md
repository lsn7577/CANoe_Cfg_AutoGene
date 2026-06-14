# Iso11783OPDeactivate

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783OPDeactivate( dword ecuHandle );
long Iso11783OPDeactivate( dword ecuHandle, dword options );
```

## Description

The function terminates the connection to the Virtual Terminal.

The Delete Object Pool command is executed to log off from the Virtual Terminal. The Maintenance message is not longer sent. The Object Pool API changes to state Not Active.

## Parameters

| Name | Description |
|---|---|
| ecuHandle | Handle of the ECU. The handle must be created with Iso11783CreateECU. |
| options | Options Bit 0 = 1: suppress Delete Object Pool command Bit 1 = 1: delete local object pool |

## Return Values

0 or error code

## Example

```c
Iso11783OPDeactivate( 
 handle );
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
