# coTfsSDOWaitForAbortCode

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsSDOWaitForAbortCode( dword nodeID );
```

## Description

This function waits until either a SDO abort message was received by the selected DUT Device Under Test or a time-out has occurred. After this, the abort code can be read out with coTfsSDOGetAbortCode.

## Parameters

| Name | Description |
|---|---|
| nodeID | Node-ID |

## Return Values

Error code

## Example

```c
if ( coTfsSDOWaitForAbortCode (2) == 1) {
  write("SDO abort message received, use coTfsSdoGetAbortCode to retrieve its data");
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.2 | 13.0 | — | — | 2.1 SP3 |
| Restricted To | — | CANopen | CANopen | — | — | CANopen |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
