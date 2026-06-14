# coTfsNmtStopNode

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsNmtStopNode( void );
long coTfsNmtStopNode( dword broadcastFlag );
```

## Description

This call triggers a NMT message that sets the in DUT Device Under Test to the stopped state. The new state is not checked because SDO transfers are not allowed in stopped mode.

## Parameters

| Name | Description |
|---|---|
| broadcastFlag | !=0: NMT message is sent to all nodes (broadcast) |

## Return Values

Error code

## Example

```c
if ( coTfsNmtStopNode() != 1) {
  write("stop node failed");
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
