# coTfsNmtResetNode

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsNmtResetNode( void );
long coTfsNmtResetNode( dword broadcastFlag );
```

## Description

This call triggers a NMT message that resets the DUT Device Under Test. After sending out the message, the boot-up message of the DUT is awaited. The reliable wait time corresponds to the general wait time, which is set with coTfsSetTimeoutValue.

## Parameters

| Name | Description |
|---|---|
| broadcastFlag | !=0: NMT message is sent to all nodes (broadcast) |

## Return Values

Error code

## Example

```c
if (coTfsNmtResetNode() != 1) {
  write("reset node failed");
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
