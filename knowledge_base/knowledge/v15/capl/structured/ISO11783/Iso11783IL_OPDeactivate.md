# Iso11783IL_OPDeactivate

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_OPDeactivate( ); // form 1
long Iso11783IL_OPDeactivate( dword options ); // form 2
long Iso11783IL_OPDeactivate( dbNode implement, dword options ); // form 3
```

## Description

The function terminates the connection to the Virtual Terminal.

The Delete Object Pool command is executed to log off from the Virtual Terminal. The Maintenance message is not longer sent. The Object Pool API changes to state Not Active.

## Parameters

| Name | Description |
|---|---|
| options | Options bit 0 = 1: suppress Delete Object Pool command bit 1 = 1: delete local object pool |
| implement | Simulation node to apply the function. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.0: form 1, 2 9.0: form 3 | 13.0 | — | — | 2.1 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 3 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1, 2) | ✔ (form 1, 2) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 3) | ✔ (form 3) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 3) | ✔ (form 3) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
