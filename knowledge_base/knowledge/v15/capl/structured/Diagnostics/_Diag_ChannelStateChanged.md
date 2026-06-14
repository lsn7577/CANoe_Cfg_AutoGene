# _Diag_ChannelStateChanged

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
_Diag_ChannelStateChanged(long newState)
```

## Description

Indicates the state of the diagnostic channel.

## Parameters

| Name | Description |
|---|---|
| 0 | ClosedChannel not opened yet or already closed. |
| 1 | OpenedChannel opened but no request successfully send yet or the attempt to send a request failed. |
| 2 | ConnectedRequest successfully send, no response received yet or expected response missed. |
| 3 | OnlineRequest and response successfully send and received. |
| 4 | ClosePendingClose requested but still pending, state Closed will follow. |
| 5 | ConnectPendingStartCommunication requested but still pending, if succeed state Connected will follow, otherwise state Opened. |

## Return Values

—

## Example

```c
_Diag_ChannelStateChanged(long newState)
{
   gCurrentChannelState = newState;
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.0 | 8.0 | — | — | — | 1.0 |
| Restricted To | Online mode ECU tester | Online mode ECU tester | — | — | — | Online mode ECU tester |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |
