# coTfsNmtEnterPreOperational

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsNmtEnterPreOperational
long coTfsNmtEnterPreOperational( dword broadcastFlag);
```

## Description

This call triggers a NMT message that sets the DUT Device Under Test into the pre-operational state.

The set state is checked with heartbeat and guarding mechanisms.

For this, there is first an attempt to configure a heartbeat producer in the DUT (object 0x1017). The heartbeat message contains the current device status. If the DUT should not make a heartbeat producer available, a remote guarding frame is sent to the DUT which responses with the corresponding guarding response. The procedure is repeated again. The second response is evaluated and contains the device status. The CANopen® specification provides that a CANopen® device supports at least one of the two modes.

## Parameters

| Name | Description |
|---|---|
| broadcastFlag | !=0: NMT message is sent to all nodes (broadcast) |

## Return Values

Error code

## Example

```c
if (coTfsNmtEnterPreOperational() != 1) {
  write(" coTfsEnterPreOperational failed, the node is in an unknown state");
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
