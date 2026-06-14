# Iso11783PDDObjectPoolDelete

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783PDDObjectPoolDelete( dword ecuHandle );
```

## Description

The function deletes the current device description object pool and sends an Object-pool Delete message to the Task Controller.

Contrary to Iso11783PDDDelete the connection to the Task Controller is not removed.

## Parameters

| Name | Description |
|---|---|
| ecuHandle | Handle of the ECU. The handle must be created with Iso11783CreateECU beforehand or ZERO for general parameters. |

## Return Values

Error code

## Example

```c
if (Iso11783PDDObjectPoolDelete( ecuHandle ) == 0) {
  write("Object pool is deleted and Object-Pool delete message is sent successfully");
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.1 | 13.0 | — | — | — |
| Restricted To | — | ISO11783 | ISO11783 | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
